from flask import Flask, render_template, request, make_response

app = Flask(__name__)
application = app
    

def number_processing(number):
    count = 0
    msg = None
    flag = 1
    for i in number:
        if i.isdigit():
            count += 1
    print(number, count)
    if count != 10 and count != 11:
        return make_response(render_template('phone.html', flag=0, msg="1 Недопустимый ввод. Неверное количество цифр."))
    if count == 11:
        if not number.startswith('+7') and not number.startswith('8'):
            return make_response(render_template('phone.html', flag=0, msg="2 Недопустимый ввод. Неверное количество цифр."))
    number = number.replace('+', '').replace('(', '').replace(')', '').replace('-', '').replace('.', '').replace(' ', '')
    try:
        int(number)
    except ValueError:
        return make_response(render_template('phone.html', flag=0, msg="Недопустимый ввод. В номере телефона встречаются недопустимые символы."))
    number = f'8-{number[-10]}{number[-9]}{number[-8]}-{number[-7]}{number[-6]}{number[-5]}-{number[-4]}{number[-3]}-{number[-2]}{number[-1]}'
    return make_response(render_template('phone.html', flag=1, msg=number))
    
    

@app.route('/')
def index():
    url = request.url
    return render_template('index.html')

@app.route('/args')
def args():
    return render_template('args.html')

@app.route('/headers')
def headers():
    return render_template('headers.html')

@app.route('/cookies')
def cookies():
    response = make_response(render_template('cookies.html'))
    if request.cookies.get('name') is None:
        response.set_cookie('name', '11')
    else:
        response.set_cookie('name', '11', expires=0)
    return response

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    result = None
    error_msg = None
    if request.method == 'POST':
        try:
            operand1 = float(request.form.get('operand1'))
            operand2 = float(request.form.get('operand2'))
            operation = request.form.get('operation')
            if operation == '+':
                result = operand1 + operand2
            if operation == '-':
                result = operand1 - operand2
            if operation == '*':
                result = operand1 * operand2
            if operation == '/':
                result = operand1 / operand2
        except ValueError:
            error_msg = 'Вводите только числа'
        except ZeroDivisionError:
            error_msg = 'На ноль делить нельзя'
    response = make_response(render_template('calc.html', result=result, error_msg=error_msg))
    return response

@app.route('/phone', methods=['GET', 'POST'])
def phone():
    if request.method == 'POST':
        number = request.form.get('number')
        response = number_processing(number)
    if request.method == 'GET':
        response = make_response(render_template('phone.html'))
    return response
    
