import vk_api #Для работы с VK
import datetime #Для перевода времени Unix
import time
import random

#Вход в аккаунт по токену
Token = input("Введите свой токен VK: ")
vk_session = vk_api.VkApi(token=Token) #сюда вбивать ваш токен с доступом к сообщениям
vk = vk_session.get_api()

#ID VK
Myid = int(input("Введите свой VK ID: "))
My_id = Myid #ваше id
PID = int(input("Введите VK ID человека с которым будет работать бот: "))
P_id = PID #id с кем работает бот

#Функция перевода времени из юникса в часы
def unixtime(unix):
    value = datetime.datetime.fromtimestamp(unix)
    return int((value.strftime('%H')))

#Функция отправления сообщения
def send_message(user_id, message):
    vk.messages.send(user_id = user_id, peer_ids = True, message = message, random_id = random.randint(0, 1000000))
    print("Сообщение отправлено успешно.")


def work():
     while unixtime(time.time()) != 0: #0 это час, в который отправляется сообщение
         print("Час не настал, начинаю ожидание (1час)")
         time.sleep(3600)
     else:
         massive_message_info = vk.messages.search(q="Спокойной ночи", peer_id=P_id)
         massive_message_info = massive_message_info["items"]
         for x in range(3):
             massive_message = massive_message_info[x]
             print(massive_message)
             if massive_message["from_id"] == My_id and time.time() - int(massive_message["date"]) < 14400:
                 print("Сообщение уже было отправлено сегодня, начинаю ожидание(10 часов)")
                 time.sleep(36000)
             elif massive_message["from_id"] == My_id and time.time() - int(massive_message["date"]) > 72000:
                 #time.sleep(random.randint(0,3000)) #А то палево отправлять в одинаковое время каждый день
                 send_message(P_id, "Спокойной ночи❤❤❤")
                 time.sleep(360)

while True:
    work()
