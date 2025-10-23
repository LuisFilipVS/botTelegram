import telebot
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

SOURCE_CHANNEL = int(os.getenv("SOURCE_CHANNEL"))
TARGET_CHANNEL = int(os.getenv("TARGET_CHANNEL"))
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

bot = telebot.TeleBot(API_TOKEN)
notification_bot = telebot.TeleBot(API_TOKEN)

KEYWORDS = ["Placa de Vídeo", "Smartphone", "Notebook", "Monitor", "Tablet", "Smart TV", "Câmera", "Fone de Ouvido", "Console de Videogame"]

client = TelegramClient('promo_monitor', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler_new_message(event):
    message = event.message.message

    if any(keyword.lower() in message.lower() for keyword in KEYWORDS):
        notification_text = f"🔥 **PROMOÇÃO ENCONTRADA!** 🔥\n\n{message}"

        #notification_bot.send_message(TARGET_CHANNEL, notification_text)
        
        try:
            await client.send_message(TARGET_CHANNEL, notification_text)
            print("Promoção enviada para o canal de destino.")
        except Exception as e:
            print(f"Erro ao enviar mensagem para o canal de destino: {e}")


def start_bot():
    with client:
        print("Bot de monitoramento iniciado.")
        client.run_until_disconnected()
    
def verify_commands(message=""):
    return True

@bot.message_handler(commands=['help'])
def help_command(message):
    text=f"""
    {message.from_user.first_name}, Aqui estão os comandos disponíveis:
    /start - Iniciar o bot
    /help - Obter ajuda
    /order - Fazer um pedido
    /status - Verificar o status do pedido
    /cancel - Cancelar um pedido
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['order'])
def order_command(message):
    text = """
    Para fazer um pedido, por favor forneça os detalhes do seu pedido.
    """
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['status'])
def status_command(message):
    texto = """
    Para verificar o status do seu pedido, por favor forneça o número do pedido.
    """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['cancel'])
def cancel_command(message):
    text = """
    Para cancelar um pedido, por favor forneça o número do pedido.
    """
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    text = """
    Olá! Eu sou o bot de pedidos. Você pode usar os seguintes comandos:
    /start  - Iniciar o bot
    /help   - Obter ajuda
    /order  - Fazer um pedido
    /status - Verificar o status do pedido
    /cancel - Cancelar um pedido
    """
    bot.send_message(message.chat.id, text)

# Start polling
# bot.polling()

if __name__ == "__main__":
    print("Iniciando o bot de monitoramento de promoções...")
    start_bot()

