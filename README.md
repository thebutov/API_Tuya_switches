### Общие вызовы API
###

#### Выключение устройства powercontrol `curl "http://127.0.0.1:5000/powercontrol?device_name=switch04&action=off" `
#### Открытие двери `curl "http://127.0.0.1:5000/open_the_door" `
#### Управление дверью и освещением `curl "http://127.0.0.1:5000/door_and_light" `
#### Включение всех устройств `curl "http://127.0.0.1:5000/poweron_all" `
#### Выключение всех устройств `curl "http://127.0.0.1:5000/poweroff_all" `
#### Изменение состояния устройства `curl "http://127.0.0.1:5000/changestate?device_name=switch04" `
 

### Дашборд
Адрес дашборда: `http://127.0.0.1:5000/dashboard`

`curl "http://127.0.0.1:5000/dashboard" `

