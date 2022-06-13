from telegram import ReplyKeyboardMarkup

startBatton = ReplyKeyboardMarkup([
    ["📝 Textni audioga o'zgartirish 🔊"],
    ["🙋‍♂️Foydalanuvchilar soni 💁‍♂️","🤖 Fikr qoldirish 📌"],
    ["👨‍💻 Dasturchi 📞"]
],resize_keyboard=True)

backBattton = ReplyKeyboardMarkup([
    ["🔙 Orqaga 🔙"]
],resize_keyboard=True)

backAkbar = ReplyKeyboardMarkup([
    ["🚫 Orqaga qaytish🚫"]
],resize_keyboard=True)

akbarBatton = ReplyKeyboardMarkup([
    ["🤖 Bot Foydalanuvchilari 🤖"],
    ["❇️ Reklama 🌉","🔙 Orqaga 🔙"],
],resize_keyboard=True)

sonlar = {
    '0' : "0️⃣",
    '1' : "1️⃣",
    '2' : "2️⃣",
    '3' : "3️⃣",
    '4' : "4️⃣",
    '5' : "5️⃣",
    '6' : "6️⃣",
    '7' : "7️⃣",
    '8' : "8️⃣",
    '9' : "9️⃣",
}


rus = ["й","ц","у","к","ф","қ","ь","т","м","д","л","г","н","з","ж"]