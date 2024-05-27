#biblioteca externa
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import re
import csv
import schedule

#Função para agendar a execução do script a cada 1 semana
def agendar_execucao():
    schedule.every().sunday.at("12:10").do(principal)
    while True:
        schedule.run_pending()

#Obtenção dos Dados
def obter_dados_jogo():
    driver = webdriver.Chrome()
    driver.get('https://www.xbox.com/pt-br/promotions/sales/sales-and-specials?xr=shellnav')
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    jogos = soup.find_all('div', class_='m-panes-product-placement-item')
    return jogos

#Extrair informações dos jogos
def extrair_info_jogo(jogos):
    catalogo = []
    for jogo in jogos:
        div_titulo = jogo.find('h3', class_='c-heading-4')
        div_preco = jogo.find('div', class_='c-price')

        if div_titulo and div_preco:
            titulo = div_titulo.text
            div_preco_original = div_preco.find('s')
            if div_preco_original:
                preco_original = div_preco_original.text
            else:
                preco_original = "Preço original não encontrado"
            preco_atual = div_preco.text
            catalogo.append([titulo, preco_original, preco_atual])
        else:
            print("Título ou preço não encontrado para um jogo")
    return catalogo

#Escrever os dados obtidos em um arquivo csv
def escrever_para_csv(nome_arquivo, cabecalho, dados): #arquivo csv
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo: 
        escritor = csv.writer(arquivo)
        escritor.writerow(cabecalho)
        for linha in dados:
            escritor.writerow(linha)

def limpar_dados_preco(df): # tratamento de dados para nao ficar baguncado
    df['Current Price'] = df['Current Price'].apply(lambda x: re.findall(r'R\$\d+.\d+', x)[-1] if re.findall(r'R\$\d+.\d+', x) else 'N/A')
    df = df[['Title', 'Current Price']]
    df.to_csv('jogos_xbox.csv', index=False)
    return df

def obter_imagens(jogos):
    imagens = []
    for jogo in jogos:
        img = jogo.find('img')
        if img:
            imagens.append([img['src']])
        else:
            imagens.append(["Imagem não encontrada"])
    return imagens

def principal(): #funcao principal, onde todos os dados fornecidos acima sao executados nessa linha...
    jogos = obter_dados_jogo()
    catalogo = extrair_info_jogo(jogos)
    escrever_para_csv('jogos_xbox.csv', ["Title", "Original Price", "Current Price"], catalogo)
    df = pd.read_csv('jogos_xbox.csv', encoding='ISO-8859-1')
    df = limpar_dados_preco(df)
    print(df)
    imagens = obter_imagens(jogos)
    escrever_para_csv('imagens_xbox.csv', [], imagens)
    time.sleep(2)

#Tratamento dos Dados Obtidos
#excluir a primeira linha do arquivo de imagens imagens_xbox.csv

def excluir_primeira_linha():
    with open('imagens_xbox.csv', 'r') as arquivo:
        linhas = arquivo.readlines()
    with open('imagens_xbox.csv', 'w') as arquivo:
        arquivo.writelines(linhas[1:])

if __name__ == "__main__":
    principal()