from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from mysql_db import MySQL
import mysql.connector as connector
import re 
import hashlib




login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = 'Для доступа к данной странице необходимо пройти процедуру аутентификации'
login_manager.login_message_category = 'warning'
app = Flask(__name__)
application = app
app.config.from_pyfile('config.py')

login_manager.init_app(app)

mysql = MySQL(app)

CREATE_PARAMS = ['login', 'password', 'first_name', 'last_name', 'middle_name', 'role_id']
UPDATE_PARAMS = ['first_name', 'last_name', 'middle_name', 'role_id']

def getPassErrors(password):
    password_error_list = set()
    if password==None:
        password_error_list.add('Поле не может быть пустым')
    else:
        if len(password) > 128 or len(password) < 8:
            password_error_list.add('Пароль должен быть длинной больше 8 и меньше 128 символов')
        if not any(c.islower() for c in password):
            password_error_list.add('Пароль должен содержать строчную букву')
        if not any(c.isupper() for c in password):
            password_error_list.add('Пароль должен содержать заглавную букву')
        if not any(c.isdigit() for c in password):
            password_error_list.add('Пароль должен содержать цифру')
        for i in password:
            if i.isalpha():
                if not (bool(re.search('[а-яА-Я]', i)) or bool(re.search('[a-zA-Z]', i))):
                    password_error_list.add('Допустимы только латинские или кириллические буквы')
            elif i.isdigit():
                pass
            else:
                if i == ' ':
                    password_error_list.add('Недопустимо использовать пробел')
                if i not in '''~ ! ? @ # $ % ^ & * _ - + ( ) [ ] { } > < / \ | " ' . , : ;'''.split():
                    password_error_list.add('Недопустимые символы')
    if len(password_error_list) != 0:
        return password_error_list
    
def getLoginErrors(login):
    login_error_list = set()
    if login==None:
        login_error_list.add('Поле не может быть пустым')
    else:
        if len(login) < 5:
            login_error_list.add('Логин должен содержать больше 5 символов')
        for i in login:
            if not (bool(re.search('[a-zA-Z]', i)) or i.isdigit()):
                login_error_list.add('Допустимы только латинские буквы и цифры')
    if len(login_error_list) != 0:
        return login_error_list

def getLastNameErrors(last_name):
    last_name_error_list = set()
    if last_name==None:
        last_name_error_list.add('Поле не может быть пустым')
    if len(last_name_error_list) != 0:
        return last_name_error_list

def getFirstNameErrors(first_name):
    first_name_error_list = set()
    if first_name==None:
        first_name_error_list.add('Поле не может быть пустым')
    if len(first_name_error_list) != 0:
        return first_name_error_list

def request_params(params_list):
    params = {}
    for param_name in params_list:
        params[param_name] = request.form.get(param_name) or None
    return params

def load_roles():
    with mysql.connection.cursor(named_tuple=True) as cursor:
        cursor.execute('SELECT id, name FROM roles;')
        roles = cursor.fetchall()
    return roles

class User(UserMixin):
    def __init__(self, user_id, login):
        super().__init__()
        self.id = user_id
        self.login = login


@login_manager.user_loader
def load_user(user_id):
    with mysql.connection.cursor(named_tuple=True) as cursor:
        cursor.execute('SELECT * FROM users WHERE id=%s;', (user_id, ))
        db_user = cursor.fetchone()
    if db_user:
        return User(user_id=db_user.id, login=db_user.login)
    return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_ = request.form.get('login')
        password = request.form.get('password')
        remember_me = request.form.get('remember_me') == 'on'
        with mysql.connection.cursor(named_tuple=True) as cursor:
            cursor.execute(
                'SELECT * FROM users WHERE login=%s AND password_hash=SHA2(%s, 256);',
                (login_, password)
            )
            db_user = cursor.fetchone()
        if db_user:
            login_user(User(user_id=db_user.id, login=db_user.login), remember=remember_me)
            flash('Вы усепшно прошли процедуру аутентификации.', 'success')
            return redirect(url_for('index'))
        flash('Были введены неверные данные', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/users')
def users():
    with mysql.connection.cursor(named_tuple=True) as cursor:
        cursor.execute('SELECT users.*, roles.name as role_name FROM users LEFT JOIN roles ON users.role_id=roles.id;')
        users = cursor.fetchall()
    return render_template('users/index.html', users=users)

@app.route('/users/new')
@login_required
def new():
    return render_template('users/new.html', user={}, roles=load_roles())

@app.route('/users/create', methods=['POST'])
@login_required
def create():
    params = request_params(CREATE_PARAMS)
    params['role_id'] = int(params['role_id']) if params['role_id'] else None
    password_error_list = getPassErrors(params.get('password'))
    login_error_list = getLoginErrors(params.get('login'))
    last_name_error_list = getLastNameErrors(params.get('last_name'))
    first_name_error_list = getFirstNameErrors(params.get('first_name'))
    if password_error_list or login_error_list or last_name_error_list or first_name_error_list:
        flash('Введены некоректные данные. Повторите попытку', 'danger')
        return render_template('users/new.html', user=params, roles=load_roles(), password_error_list=password_error_list,
         login_error_list=login_error_list, last_name_error_list=last_name_error_list, first_name_error_list=first_name_error_list)
    with mysql.connection.cursor(named_tuple=True) as cursor:
        try:
            cursor.execute(('INSERT INTO users (login, password_hash, last_name, first_name, middle_name, role_id)'
            'VALUES (%(login)s, SHA2(%(password)s, 256), %(last_name)s, %(first_name)s, %(middle_name)s, %(role_id)s);'),
            params
            )
            mysql.connection.commit()
        except connector.Error:
            flash('Введены некоректные данные. Ошибка сохранения', 'danger')
            return render_template('users/new.html', user=params, roles=load_roles())
    flash(f'Пользователь {params.get("login")} был успешно создан!', 'success')
    return redirect(url_for('users'))

@app.route('/users/<int:user_id>')
def show(user_id):
    with mysql.connection.cursor(named_tuple=True) as cursor:
        cursor.execute('SELECT * FROM users WHERE id=%s;', (user_id, ))
        user = cursor.fetchone()
    return render_template('users/show.html', user=user)

@app.route('/users/<int:user_id>/edit')
@login_required
def edit(user_id):
    with mysql.connection.cursor(named_tuple=True) as cursor:
        cursor.execute('SELECT * FROM users WHERE id=%s;', (user_id, ))
        user = cursor.fetchone()
    return render_template('users/edit.html', user=user, roles=load_roles())

@app.route('/users/<int:user_id>/update', methods=['POST'])
@login_required
def update(user_id):
    params = request_params(UPDATE_PARAMS)
    params['role_id'] = int(params['role_id']) if params['role_id'] else None
    params['id'] = user_id
    with mysql.connection.cursor(named_tuple=True) as cursor:
        try:
            cursor.execute(('UPDATE users SET last_name=%(last_name)s, first_name=%(first_name)s, middle_name=%(middle_name)s, role_id=%(role_id)s WHERE id = %(id)s;'), params)
            mysql.connection.commit()
        except connector.Error:
            flash('Введены некоректные данные. Ошибка сохранения', 'danger')
            return render_template('users/edit.html', user=params, roles=load_roles())
    flash('Пользователь был успешно обновлён!', 'success')
    return redirect(url_for('show', user_id=user_id))

@app.route('/users/<int:user_id>/delete', methods=['POST'])
@login_required
def delete(user_id):
    with mysql.connection.cursor(named_tuple=True) as cursor:
        try:
            cursor.execute(('DELETE FROM users WHERE id=%s'), (user_id,))
            mysql.connection.commit()
        except connector.Error:
            flash('Ну удалось удалить пользователя!', 'danger')
            return redirect(url_for('users'))
    flash('Пользователь был успешно удалён!', 'success')
    return redirect(url_for('users'))

@app.route('/chenge_password', methods=['POST', 'GET'])
def chenge_password():   
    if request.method == 'GET':
        return render_template('chenge_password.html')
    else:
        now_pass = request.form.get('nowPassword')
        byte = bytes(now_pass, encoding = 'utf-8')
        print(hashlib.sha256(byte).hexdigest())
        with mysql.connection.cursor(named_tuple=True) as cursor:
            cursor.execute('SELECT password_hash FROM users WHERE id=%s;', (current_user.get_id(), ))
            response = cursor.fetchone()
            print(response.password_hash)
        if hashlib.sha256(byte).hexdigest() == response.password_hash:
            new_pass = request.form.get('newPassword')
            password_error_list = getPassErrors(new_pass)
            print(password_error_list)
            if password_error_list:
                return render_template('chenge_password.html', password_error_list=password_error_list)
            repeat_pass = request.form.get('repeatPassword')
            if new_pass == repeat_pass:
                if now_pass != new_pass:
                    with mysql.connection.cursor(named_tuple=True) as cursor:
                        try:
                            cursor.execute(('UPDATE users SET PASSWORD_HASH=SHA2(%s, 256) WHERE id=%s;'), (new_pass, current_user.get_id(), ))
                            mysql.connection.commit()
                        except connector.Error:
                            flash('Ну удалось изменить пароль!', 'danger')
                            return redirect(url_for('chenge_password'))
                    flash('Пароль был успешно иизменён!', 'success')
                    return redirect(url_for('index'))
                else:
                    flash('Старый и новый пароли не должны совпадать', 'danger')
                    return redirect(url_for('chenge_password'))
            else:
                flash('Пароли должны совпадать', 'danger')
                return redirect(url_for('chenge_password'))
        else:
            flash('Неверный пароль', 'danger')
            return redirect(url_for('chenge_password'))




