from datetime import datetime
from tg_send import bot, chat_id
from flask import render_template, jsonify, request
import requests
import tuya_control
from settings import door_url, devices, actions, door_username, door_password

# #######################        Домашняя страница        ########################
def home():
    button_color = get_button_colors()
    return render_template('index.html', button_color=button_color)

def get_button_colors():
    global is_on
    button_color = []
    for device in devices:
        response = tuya_control.device_getpowerstatus(device)
        # print('RESPONCE: ', response)
        for item in response:
            if item['code'] == 'switch_1':
                is_on = item['value']
                break
        # print('is_on: ', is_on)
        color = 'yellow' if is_on else 'default'
        button_color.append(color)
    print('COLORS:', button_color)
    return button_color


# #######################        Управление питанием реле        ########################
def powercontrol():
    device_name = request.args.get('device_name')
    action = request.args.get('action')
    user = request.headers.get('user')

    if device_name in devices and action in actions:
        tuya_control.device_powercontrol(device_name, action, user)
        return jsonify({f'{device_name}': 'is okay'})
    else:
        return jsonify({f'{device_name}': 'ERROR'})


# #######################        Изменить состояние реле        ########################
def changestate():
    device_name = request.args.get('device_name')
    user = request.headers.get('user')
    print('USER FROM HEADERS:', user)

    if device_name in devices:
        tuya_control.device_changestate(device_name, user)
        return jsonify({f'{device_name}': 'is okay'})
    else:
        return jsonify({f'{device_name}': 'ERROR'})


def poweroff_all():
    user = request.headers.get('user')
    tuya_control.devices_poweroff_all(user)
    return jsonify({'Complete': 'True'})

def poweron_all():
    user = request.headers.get('user')
    tuya_control.devices_poweron_all(user)
    return jsonify({'Complete': 'True'})

def open_the_door(user=None):
    user = request.headers.get('user')
    session = requests.Session()
    session.auth = (door_username, door_password)
    door_response = session.get(door_url)

    if door_response.status_code == 200:
        print("Запрос выполнен успешно")
        print(door_response.text)
        tg_msg_source = str(datetime.now()) + '\n' + f"🔓 Калитка открыта \n🧍 user: {user}"
        print('\n==============\n', tg_msg_source, '\n==============\n')
        bot.send_message(chat_id, tg_msg_source)
        return jsonify({'Complete': 'True'})
    else:
        print("Ошибка выполнения запроса")
        print(door_response.status_code)
        tg_msg_source = str(datetime.now()) + '\n' + f"🚩 Ошибка открытия калитки \n🧍 user: {user}"
        print('\n==============\n', tg_msg_source, '\n==============\n')
        bot.send_message(chat_id, tg_msg_source)
        return jsonify({'Complete': 'False'})

def door_and_light():
    open_the_door()
    tuya_control.devices_poweron_all()
    return jsonify({'Complete': 'True'})


def sendmessage(tg_msg_source='empty message'):
    bot.send_message(chat_id, tg_msg_source)
