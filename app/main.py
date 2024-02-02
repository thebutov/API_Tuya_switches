import functools
import methods
from flask import Flask, jsonify, request
from settings import users

app = Flask(__name__)

def check_user_authentication(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get('user') in users:
            return f(*args, **kwargs)
        else:
            methods.sendmessage(f'🚩 Мутный запрос:\n\n{request.headers} \n{request}')
            response = jsonify({'Please': 'say the password'})
            response.status_code = 403
            return response
    return decorated_function


@app.route('/dashboard', methods=['GET'])
# @check_user_authentication
def methods_home():
    return methods.home()

@app.route('/changestate', methods=['GET'])
@check_user_authentication
def methods_changestate():
    return methods.changestate()

@app.route('/powercontrol', methods=['GET'])
@check_user_authentication
def methods_powercontrol():
    return methods.powercontrol()

@app.route('/poweroff_all', methods=['GET'])
@check_user_authentication
def methods_poweroff_all():
    return methods.poweroff_all()

@app.route('/poweron_all', methods=['GET'])
@check_user_authentication
def methods_poweron_all():
    return methods.poweron_all()

@app.route('/open_the_door', methods=['GET'])
@check_user_authentication
def methods_open_the_door():
    return methods.open_the_door()

@app.route('/door_and_light', methods=['GET'])
@check_user_authentication
def methods_door_and_light():
    return methods.door_and_light()


#test
if __name__ == '__main__':
    app.run(host='0.0.0.0')

