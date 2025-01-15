import os

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb+srv://hermit:7-rKCT%40u3CeFGPz@cluster0.juugp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = os.getenv("BOT_TOKEN", "6356338633:AAEoDegBXOsAmx12d-Vdr-28eFqRBADlLZY")
OWNER_ID = int(os.getenv("OWNER_ID", 1630507023))
CHANNELS = os.getenv("CHANNELS", "@testkl17,@terab0xdl").split(',')
PAYMENT_CHANNEL = os.getenv("PAYMENT_CHANNEL", "@testkl17")
TOKEN = os.getenv("TOKEN", "TRON")

DAILY_BONUS = int(os.getenv("DAILY_BONUS", 1))
MINI_WITHDRAW = float(os.getenv("MINI_WITHDRAW", 0.5))
PER_REFER = float(os.getenv("PER_REFER", 0.0001))

REQUEST_CHANNELS = ['-1002269604986', '-1002421703830']
JOIN_REQUEST = True