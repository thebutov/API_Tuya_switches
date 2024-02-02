from dotenv import load_dotenv
import os

load_dotenv()

list_onoff = {'on': True,
              'off': False}

devices = ['switch01', 'switch02', 'switch03', 'switch04', 'switch05']
actions = ['on', 'off', 'change']

list_devices = {'switch01': 'bfc1b9861a3b9f7d9ferdr',
                'switch02': 'bfc4e907b416cef521c51p',
                'switch03': 'bf888d69c60b557b48zb0q',
                'switch04': 'bfa7b1015c843530b2apqm',
                'switch05': 'bfa8c777902f8c4973911h'}



# list_devices = {'switch01': 'bfc1b9861a3b9f7d9ferdr', угол
#                 'switch02': 'bfc4e907b416cef521c51p',
#                 'switch03': 'bf888d69c60b557b48zb0q',  бабушка
#                 'switch04': 'bfa7b1015c843530b2apqm',  на доме
#                 'switch05': 'bfa8c777902f8c4973911h'}  на столбе


users = os.getenv('USERS')

door_url       = os.getenv('door_url')
door_username  = os.getenv('door_username')
door_password  = os.getenv('door_password')
ACCESS_ID      = os.getenv('ACCESS_ID')
ACCESS_SECRET  = os.getenv('ACCESS_SECRET')
UID            = os.getenv('UID')
ENDPOINT_URL   = os.getenv('ENDPOINT_URL')

token          = os.getenv('token')
chat_id        = os.getenv('chat_id')