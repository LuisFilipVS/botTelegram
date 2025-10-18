import telebot

API_TOKEN = '7390416479:AAH0selpTQcHho7jHMLKMPWj5BQbrPErwDc'
bot = telebot.TeleBot(API_TOKEN)

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
bot.polling()
