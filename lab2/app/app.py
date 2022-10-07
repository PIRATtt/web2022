from flask import Flask, request, render_template, make_response

app = Flask(__name__)
application = app

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/url')
def url():
    return render_template('url.html')

@app.route('/headers')
def headers():
    return render_template('headers.html')

@app.route('/cookies')
def cookies():
    resp = make_response(render_template('cookies.html'))
    if 'username' in request.cookies:
        resp.set_cookie('username', 'some name', expires=0)
    else:
        resp.set_cookie('username', 'some name')
    return resp

@app.route('/form', methods=['POST', 'GET'])
def form():
    return render_template('form.html')

@app.route('/telefon', methods=['GET', 'POST'])
def telefon():
    number = str(request.form.get('numb'))
    result=None
    for a in ['(', ')', '+', '-', '.']:
        number=number.replace(a, '')
    if 9<len(number)<12 and number.isdigit()==True:
        if len(number)==10:
            number='7'+number
        elif len(number)==11:
            pass
        result = True
    else:
        result = False
    return render_template('telefon.html', result=result, number=number)