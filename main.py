import discord
from discord.ext import commands
import requests

# Configurações
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# Quando o bot ligar
@bot.event
async def on_ready():
    print(f"🌳 FlorestaViva online como {bot.user}")


# Comando principal
@bot.command()
async def FlorestaViva(ctx):

    await ctx.send(
        "🌳 FlorestaViva\n\n"
        "Olá! Sou o FlorestaViva, um bot criado para ajudar "
        "a conscientizar sobre a importância da natureza! 🌎\n\n"
        "Comandos:\n"
        "🌎 !PorqueNatureza — Por que cuidar da natureza?\n"
        "🌱 !CuidarNatureza — Como cuidar da natureza?\n"
        "⚠️ !ProblemaNature — Principais problemas ambientais.\n"
        "🌤️ !Previsao [cidade] — Previsão do tempo."
    )


# Por que cuidar da natureza?
@bot.command()
async def PorqueNatureza(ctx):

    await ctx.send(
        "🌎 Por que cuidar da natureza?\n\n"
        "A natureza é essencial para nossa vida. Ela fornece "
        "água, alimentos, oxigênio e abriga milhares de espécies. "
        "Preservá-la ajuda a manter o equilíbrio do planeta e "
        "garante um futuro melhor para todos. 🌱"
    )


# Como cuidar da natureza?
@bot.command()
async def CuidarNatureza(ctx):

    await ctx.send(
        "🌱 Como cuidar da natureza?\n\n"
        "♻️ Recicle e evite desperdícios.\n"
        "💧 Economize água.\n"
        "💡 Economize energia.\n"
        "🚯 Não jogue lixo na natureza.\n"
        "🌳 Proteja árvores e áreas verdes.\n"
        "🐾 Respeite os animais e seus habitats."
    )


# Problemas ambientais
@bot.command()
async def ProblemaNature(ctx):

    await ctx.send(
        "⚠️ Principais problemas da natureza:\n\n"
        "🌳 Desmatamento\n"
        "🌡️ Mudanças climáticas\n"
        "🗑️ Poluição\n"
        "🐾 Extinção de espécies\n"
        "🌊 Poluição dos oceanos\n\n"
        "Todos esses problemas podem prejudicar os ecossistemas "
        "e a vida no planeta."
    )


# Previsão do tempo
@bot.command()
async def Previsao(ctx, *, cidade=None):

    if not cidade:
        await ctx.send(
            "🌤️ Digite uma cidade!\n"
            "Exemplo: !Previsao São Paulo"
        )
        return

    try:
        # Busca o clima da cidade
        url = f"https://wttr.in/{cidade}?format=j1"

        resposta = requests.get(url, timeout=10)
        dados = resposta.json()

        clima = dados["current_condition"][0]

        temperatura = clima["temp_C"]
        umidade = clima["humidity"]
        vento = clima["windspeedKmph"]
        condicao = clima["weatherDesc"][0]["value"]

        await ctx.send(
            f"🌤️ Previsão para {cidade}\n\n"
            f"🌡️ Temperatura: {temperatura}°C\n"
            f"💧 Umidade: {umidade}%\n"
            f"💨 Vento: {vento} km/h\n"
            f"☁️ Condição: {condicao}"
        )

    except Exception as erro:

        print(f"Erro na previsão: {erro}")

        await ctx.send(
            "❌ Não consegui encontrar essa cidade."
        )


# Inicia o bot
bot.run("Token!")
