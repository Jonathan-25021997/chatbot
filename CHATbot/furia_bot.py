import telebot

#seu token do BotFather
TOKEN = '7591241787:AAHPTXwd4s0Q0fJFIQTOdlkavZ8r2_avKGE'
bot = telebot.TeleBot(TOKEN)

# Respostas pré-definidas
def get_response(message):
    text = message.lower()

    if "quando" in text and "furia" in text and "criada" in text:
        return "A FURIA Esports foi fundada em 2017 por Jaime Pádua, Cris Guedes e André Akkari. 🔥🐆"

    elif "quais jogos" in text or "jogos a furia joga" in text:
        return ("A FURIA compete em diversos jogos:\n"
                "- Counter-Strike 2 (CS2)\n"
                "- Valorant\n"
                "- League of Legends\n"
                "- Rocket League\n"
                "- Rainbow Six Siege\n"
                "- PUBG")

    elif "campeonatos" in text or "títulos" in text or "ganhou" in text:
        return ("🏆 Principais Títulos conquistados pela FURIA:\n"
                "- ESL Pro League Season NA (2020)\n"
                "- DreamHack Masters Spring NA, DreamHack Open Summer NA (2020)\n"
                "- CBCS Elite League (2021)\n"
                "E ótimas campanhas em Majors!")

    elif "jogadores" in text or "time cs" in text:
        return ("🎯 Line-up atual titular do CS2 da FURIA:\n"
                "- KSCERATO\n"
                "- yuurih\n"
                "- YEKINDAR\n"
                "- molodoy\n"
                "- fallen")

    elif "major" in text:
        return ("✅ A FURIA já participou de diversos Majors de CS, como:\n"
                "- PGL Major Stockholm 2021\n"
                "- IEM Rio Major 2022")
    
    
    elif "o ultimo campeonato de valorant" in text:
        return "O ultimo campeonato na qual a Furia participou no valorant foi o torneio VCT 2025: Americas Stage 1. 🔥🐆"
    
    elif "ola" in text:
        return "Ola tudo bem Fvrioso? Me faça uma pergunta e te deixarei super atualizado sobre as informações da Fvria.🐆"
    
    elif "/start" in text:
        return "Seja bem vindo ao chat da Fvria, aqui você pode encontrar as principais informações e se atualizar sobre nossa org"

    else:
        return "Desculpe, não entendi sua pergunta 😕. Pergunte algo como: 'Quando a FURIA foi criada?' ou 'Quais títulos a FURIA já ganhou?'"


# Recebe e responde mensagens de texto
@bot.message_handler(func=lambda msg: True)
def responder_mensagem(message):
    resposta = get_response(message.text)
    bot.reply_to(message, resposta)

print("Bot rodando... Ctrl+C para parar.")
bot.infinity_polling()


bot.infinity_polling()