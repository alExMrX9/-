import python_weather, requests, pprint
from aiogram import Dispatcher, Bot, types, executor
from googletrans import Translator

key, bot_token = "2ffd2e47dc26e40d491274a3c7051be7", "5906792428:AAGwbA3c2lR8EPwhm0IR-sImcmo5httlghg"
ttrans = Translator()


bot = Bot(bot_token)
dp = Dispatcher(bot)
name = ""


@dp.message_handler()
async def text(message: types.Message):
    file = open("cloup.png", "rb")
    await bot.send_photo(chat_id=message.chat.id, caption=pogoda(api=key, city=message.text), photo=file)
    file.close()


def pogoda(api, city):
    global name
    
    message1 = ttrans.translate(text=city, dest="en").text
    url = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message1}&appid={api}").json()
    per_weather_0 = url["weather"][0]['main']
    per_name_0 = url["name"]
    per_temp = int(url['main']["temp"]  - 273.15)


    per_weather_1 = ttrans.translate(text=per_weather_0, dest="ru").text
    per_name_1 = ttrans.translate(text=per_name_0, dest="ru").text 
    got = f"{per_name_1} {per_weather_1} {per_temp}"
    
    if per_weather_1.lower() == "облака":
        name = "облака"
    return got


executor.start_polling(dp)