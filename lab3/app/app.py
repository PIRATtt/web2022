from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

login=LoginManager()

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

login.init_app(app)
login.login_view = 'login'
login.login_message = 'Вам нужно авториоваться!'
login.login_message_category='warning'

def get_user():
    return [{'user_id': '1', 'login': 'user', 'password': 'qwerty'}]

class User(UserMixin):
    def __init__(self, user_id, login):
        super().__init__()
        self.id=user_id
        self.login = login

@login.user_loader
def load_user(user_id):
    for user in get_user():
        if user['user_id'] == user_id:
            return User(**user)
    return None


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

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        remember = request.form.get('remember') == 'on'
        if login and password:
            for user in get_user():
                if user['login'] == login and user['password'] == password:
                    user_object = User(**user)
                    login_user(user_object, remember=remember)
                    flash('Вы успешно зашли!', 'success')
                    next= request.args.get('next')

                    return redirect(next or url_for('base'))
        flash('Введены неверные данные!', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base'))

@app.route('/secret')
@login_required
def secret():
    return render_template('secret.html')