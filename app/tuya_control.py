import tuyacloud as tuyacloud
from datetime import datetime
from tg_send import bot, chat_id
from settings import door_url, devices, actions, door_username, door_password, list_devices, list_onoff, ACCESS_ID, ACCESS_SECRET, UID, ENDPOINT_URL

tcc = tuyacloud.TuyaCloudClientNicer(
    ACCESS_ID=f'{ACCESS_ID}',
    ACCESS_SECRET=f'{ACCESS_SECRET}',
    UID=f'{UID}',
    ENDPOINT_URL=f'{ENDPOINT_URL}'
)

def changedevicestate_error(params=None, path=None, response_tuyacloud=None):
    print('\n')
    print(datetime.now(), response_tuyacloud)
    tg_msg_source = str(datetime.now()) + '\n\n' + str(params) + '\n\n' + str(path) + '\n\n' + str(response_tuyacloud)
    bot.send_message(chat_id, tg_msg_source)
    print(datetime.now(), f"Ошибка какая-то")


############## Погасить весь свет ##############
def devices_poweroff_all(user='default'):
    for device in list_devices:
        response_tuyacloud = device_powercontrol(device, 'off', user, True)
    tg_msg_source = str(datetime.now()) + f'\n 🌑 Выключить все реле \n🧍user: {user}'
    bot.send_message(chat_id, tg_msg_source)
    print('\n==============\n', tg_msg_source, '\n==============\n')


############## Зажечь весь свет ##############
def devices_poweron_all(user='default'):
    for device in list_devices:
        response_tuyacloud = device_powercontrol(device, 'on', user, True)
    tg_msg_source = str(datetime.now()) + f'\n 🌕 Включить все реле \n🧍user: {user}'
    bot.send_message(chat_id, tg_msg_source)
    print('\n==============\n', tg_msg_source, '\n==============\n')


def device_changestate(device, user):
    response = device_getpowerstatus(device)
    # print(response)
    for item in response:
        if item['code'] == 'switch_1':
            is_on = item['value']
            break
    if is_on == True:
        device_powercontrol(device, 'off', user, False)
    else:
        device_powercontrol(device, 'on', user, False)



###### Управление релюхой ######
def device_powercontrol(device_name=None, action=None, user='default', silent_notiff=False):
    device_uuid = list_devices.get(device_name)
    commands = []
    commands.append({
        "code": 'switch_1',  # ТУТ НОМЕР РЕЛЕ В УСТРОЙСТВЕ
        "value": list_onoff.get(action)
    })
    exec_result = tcc.exec_device_command(device_uuid, {"commands": commands})
    tg_msg_source = str(datetime.now()) + f'\n 🚦device name: {device_name} \n 📍action: {action} \n 🧍user: {user}'
    if silent_notiff == False:
        bot.send_message("176090858", tg_msg_source)
    print('\n==============\n', tg_msg_source, '\n==============\n')

    return exec_result

# ##### Получение статуса реле ######
def device_getpowerstatus(device_name):
    device_uuid = list_devices.get(device_name)
    exec_result = tcc.get_device_status(device_uuid)
    print(exec_result)
    for entry in exec_result:
        # print(device_uuid, entry["value"])
        print(device_uuid)
        # if entry["code"] == "switch_1":
            # print(device_uuid, entry["value"])
            # print(entry["value"])
            # break

    return exec_result
    # print(device_uuid, exec_result)




print('\n\n==================================')
print(str(datetime.now()))
print('НАЧАЛЬНАЯ ПРОВЕРКА СТАТУСОВ РЕЛЕ:')
print('111111111111111111')
device_getpowerstatus('switch01')
print('22222222222222222222')
device_getpowerstatus('switch02')
print('33333333333333333333333333')
device_getpowerstatus('switch03')
print('4444444444444444444444')
device_getpowerstatus('switch04')
print('==================================\n')

tg_msg_source = str(datetime.now()) + '\n✳️ Сервер управления светом запущен'
print('\n==============\n', tg_msg_source, '\n==============\n')
bot.send_message(chat_id, tg_msg_source)


