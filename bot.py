import logging
import os
from ultralytics import YOLO
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

API_TOKEN = '6742490786:AAG_0ukyrnIM-zAUIIJ0y8Q5AHK5TtLbKw4'

# Ініціалізація бота і диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Обробник команди /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Створення клавіатури
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_text = "Flowers"
    keyboard.add(button_text)

    # Відправка повідомлення разом з клавіатурою
    await message.answer("Hello", reply_markup=keyboard)


@dp.message_handler(text="Flowers")
async def send_welcome(message: types.Message):

    await message.answer("Send me flower")
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    # Accessing the first photo in the list
    photo = message.photo[0]
    model = YOLO('runs/classify/train/weights/best.pt')  # load a custom model
    photo_path = os.path.join('prepared/res', f"{photo.file_id}.jpg")
    await photo.download(destination=photo_path)
    # Predict with the model
    results = model('prepared/res/'f"{photo.file_id}.jpg", )  # predict on an image
    if results[0].probs.top1 == 0:
        await message.answer_photo(photo=photo.file_id, caption="daisy")
    elif results[0].probs.top1 == 1:
        await message.answer_photo(photo=photo.file_id, caption="dandelion")
    elif results[0].probs.top1 == 3:
        await message.answer_photo(photo=photo.file_id, caption="sunflower")
    else:
        await message.answer_photo(photo=photo.file_id, caption="rose")


if __name__ == '__main__':
    executor.start_polling(dp, )
