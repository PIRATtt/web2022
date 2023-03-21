from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import login_required
from mysql_db import MySQL
import mysql.connector as connector

from test import *

# login=LoginManager()

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

mysql=MySQL(app)
from auth import bp as auth_bp, init_login_manager

init_login_manager(app)
app.register_blueprint(auth_bp)


def load_roles():
    cursor=mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT id, name FROM roles2;')
    roles=cursor.fetchall()
    cursor.close()
    return roles

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/visits')
def visits():
    if session.get('visits'):
        session['visits'] += 1
    else:
        session['visits']=1
    return render_template('visits.html')

@app.route('/users')
def users():
    cursor=mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT users2.*, roles2.name as role_name FROM users2 LEFT OUTER JOIN roles2 ON users2.role_id = roles2.id;')
    users=cursor.fetchall()
    cursor.close()
    return render_template('users/index.html', users=users)

@app.route('/users/<int:user_id>')
@login_required
def show(user_id):
    cursor=mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM users2 WHERE id = %s', (user_id,))
    user=cursor.fetchone()
    cursor.execute('SELECT * FROM users2 WHERE id = %s', (user.role_id,))
    role=cursor.fetchone()
    cursor.close()
    return render_template('users/show.html', user=user, role=role)

@app.route('/users/new')
@login_required
def new():
    return render_template('users/new.html', user={}, roles=load_roles())

@app.route('/users/<int:user_id>/edit')
@login_required
def edit(user_id):
    cursor=mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM users2 WHERE id = %s;', (user_id,))
    user=cursor.fetchone()
    cursor.close()
    return render_template('users/edit.html', user=user, roles=load_roles())

@app.route('/users/create', methods=['POST'])
@login_required
def create():
    login = request.form.get('login') or None
    password = request.form.get('password') or None
    first_name = request.form.get('first_name') or None
    last_name = request.form.get('last_name') or None
    middle_name = request.form.get('middle_name') or None
    role_id = request.form.get('role_id') or None
    query='''
        INSERT INTO users2 (login, password_hash, first_name, last_name, middle_name, role_id)
        VALUES (%s, SHA2(%s, 256), %s, %s, %s, %s);
    '''
    if check_login(str(login))==True:
        if check_pas(str(password))==False:
            cursor=mysql.connection.cursor(named_tuple=True)
            try:
                cursor.execute(query, (login, password, first_name, last_name, middle_name, role_id))
            except connector.errors.DatabaseError:
                flash(f'Введены некорректные данные', 'danger')
                user= {
                    'login': login,
                    'password': password,
                    'first_name': first_name,
                    'last_name': last_name,
                    'middle_name': middle_name,
                    'role_id': role_id
                }
                return render_template('/users/new.html', user=user, roles=load_roles())
            mysql.connection.commit()
            flash(f'Пользователь {login} был успешно создан!', 'success')
            cursor.close()
            return redirect(url_for('users'))
        else:
            flash(f'{check_pas(str(password))}', 'danger')
            user= {
                'login': login,
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
                'middle_name': middle_name,
                'role_id': role_id
            }
            return render_template('/users/new.html', user=user, roles=load_roles())
    else:
        flash(f'{check_login(str(login))}', 'danger')
        user= {
            'login': login,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'role_id': role_id
        }
        return render_template('/users/new.html', user=user, roles=load_roles())  

@app.route('/users/<int:user_id>/update')
@login_required
def update(user_id):
    login = request.form.get('login') or None
    first_name = request.form.get('first_name') or None
    last_name = request.form.get('last_name') or None
    middle_name = request.form.get('middle_name') or None
    role_id = request.form.get('role_id') or None
    query='''
        UPDATE users2 SET login=%s, first_name=%s, last_name=%s, middle_name=%s, role_id=%s
        WHERE id=%s;
    '''

    cursor=mysql.connection.cursor(named_tuple=True)
    try:
        cursor.execute(query, (login, first_name, last_name, middle_name, user_id))
    except connector.errors.DatabaseError:
        flash(f'Введены некорректные данные', 'danger')
        user= {
            'id': user_id,
            'login': login,
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'role_id': role_id
        }
        return render_template('/users/edit.html', user=user, roles=load_roles())
    mysql.connection.commit() #После запроса комитить
    flash(f'Пользователь {login} был успешно обновлён!', 'success')
    cursor.close()
    return redirect(url_for('users'))

@app.route('/users/<int:user_id>/delete', methods=['POST', 'GET'])
@login_required
def delete(user_id):
    with mysql.connection.cursor(named_tuple=True) as cursor:
        try:
            cursor.execute('DELETE FROM users2 WHERE id = %s;', (user_id,))
        except connector.errors.DatabaseError as err:
            flash('Не удалось удалить данные', 'danger')
            return redirect(url_for('users'))
        mysql.connection.commit()
        flash('Успешно удалено!', 'success')
    return redirect(url_for('users'))