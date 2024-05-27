import asyncio
from aiogram import Bot
import csv
import schedule
import os  # Importe o módulo os

# agenda a execução da função principal para todos os domingos às 12:30
def agenndar_mandar_promocao():
    schedule.every().sunday.at("12:30").do(main)
    while True:
        schedule.run_pending()

# função para enviar mensagem de promoção
async def enviar_mensagem_promocao(bot, chat_id, mensagem):
    await bot.send_message(chat_id=chat_id, text=mensagem)

# função para ler arquivo csv
def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pular o cabeçalho
        return [linha[0] for linha in leitor]  # Retornar o primeiro campo de cada linharestante do arquivo

# função para enviar promoções
async def enviar_promocoes(bot, chat_id, arquivo_jogos, arquivo_imagens):
    img_urls = ler_arquivo_csv(arquivo_imagens)
    with open(arquivo_jogos, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pular o cabeçalho
        for linha, img_url in zip(leitor, img_urls):
            if len(linha) < 2:  # Ignorar linhas vazias ou com menos de dois campos
                continue
            titulo, preco = linha   
            legenda = f"🔥PROMOÇÃO! {titulo}🔥\n\n💰POR APENAS {preco}!💰"
            await bot.send_photo(chat_id=chat_id, photo=img_url, caption=legenda)

# função principal
async def main():
    bot_token = os.getenv('BOT_TOKEN')  # Obtenha o token do bot da variável de ambiente
    if bot_token is None:
        raise Exception('Token não definido. Por favor, defina a variável de ambiente BOT_TOKEN.')
    bot = Bot(token=bot_token)
    chat_id = '7002586722'
    mensagem = '---------------🔥PROMOÇÕES DE JOGOS!🔥\n\n🎮XBOX🎮/PLAYSTATION DA SEMANA -------------------'
    await enviar_mensagem_promocao(bot, chat_id, mensagem)
    await enviar_promocoes(bot, chat_id, 'jogos_xbox.csv', 'imagens_xbox.csv')
    await enviar_promocoes(bot, chat_id, 'jogos_playstation.csv', 'imagens_playstation.csv')

asyncio.run(main())