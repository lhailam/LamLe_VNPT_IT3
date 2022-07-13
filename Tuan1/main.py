import telegram

key ='5528322312:AAGZXoUdjxxsEe7nNrIbjvKsVINEHl-FrsI'
path = "sieunhan.gif"
print("Bot start...")

def send_message(photo=path):
    try:
        bot = telegram.Bot(token=key)
        bot.sendPhoto(chat_id="-775780902", photo=open(photo, "rb"), caption="Gọi siêu nhân vàng!!!")

    except Exception as ex:
        print(ex)
    print("send sucess!!!")

send_message()