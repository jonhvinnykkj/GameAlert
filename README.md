# GameAlert

## Introdução

No cenário atual dos jogos eletrônicos, o mercado digital de games para plataformas como PlayStation e Xbox tem crescido exponencialmente, oferecendo uma grande quantidade de títulos e promoções aos consumidores. No entanto, acompanhar essas ofertas pode ser desafiador devido à quantidade de informações dispersas e à frequência com que as promoções são atualizadas.

O **GameAlert** é um programa desenvolvido em Python que captura automaticamente as promoções de jogos das plataformas PlayStation e Xbox. Todas as segundas-feiras, às 12h, o GameAlert posta no Telegram uma lista atualizada das melhores promoções da semana, garantindo que os usuários estejam sempre informados sobre as ofertas mais recentes.

## Objetivos

### Objetivo Geral
Desenvolver um sistema automatizado que capture, organize e divulgue semanalmente as promoções de jogos das plataformas PlayStation e Xbox.

### Objetivos Específicos
- Desenvolver um scraper em Python para coletar dados de promoções de jogos.
- Implementar uma base de dados para armazenar as informações coletadas.
- Criar um bot para o Telegram que publique semanalmente as promoções.
- Garantir a atualização semanal das promoções.
- Testar e validar o sistema para assegurar a precisão dos dados capturados.

## Metodologia

Utilizou-se a metodologia SCRUM, com as seguintes etapas:

1. **Levantamento de Requisitos:** Identificação das necessidades dos usuários.
2. **Desenvolvimento do Scraper:** Uso das bibliotecas Pandas, Requests, BeautifulSoup e Selenium.
3. **Implementação da Base de Dados:** Armazenamento em arquivo CSV.
4. **Desenvolvimento do Bot do Telegram:** Utilização da API do Telegram.
5. **Configuração de Cronograma:** Funções agendadas para captura e publicação de dados.
6. **Testes e Validação:** Testes unitários e de integração para verificar o funcionamento do sistema.

## Funcionalidades

- Captura automática das promoções de jogos.
- Armazenamento das promoções em arquivo CSV.
- Publicação automática no Telegram todas as segundas-feiras às 12h.
- Filtro de jogos com valores abaixo de cinquenta reais.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:** Pandas, Requests, BeautifulSoup, Selenium, Aiogram
- **Banco de Dados:** Arquivo CSV
- **Automação:** Cron jobs

## Como Instalar e Rodar o Projeto

### Pré-requisitos

- Python 3.7+
- Bibliotecas: Pandas, Requests, BeautifulSoup, Selenium, Aiogram

### Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/usuario/GameAlert.git
    cd GameAlert
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure o token do bot do Telegram em uma variável de ambiente:
    ```bash
    export TELEGRAM_BOT_TOKEN='seu-token-aqui'
    ```

### Execução

1. Execute o script de captura de dados:
    ```bash
    python scraper_playstation.py
    python scraper_xbox.py
    ```

2. Execute o script do bot do Telegram:
    ```bash
    python bot_telegram.py
    ```

### Agendamento

Configure cron jobs para execução semanal:
```cron
0 12 * * 1 /caminho/para/python /caminho/para/GameAlert/scraper_playstation.py
0 12 * * 1 /caminho/para/python /caminho/para/GameAlert/scraper_xbox.py
30 12 * * 0 /caminho/para/python /caminho/para/GameAlert/bot_telegram.py
```
## Como Contribuir

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:
    ```bash
    git checkout -b feature/nome-da-feature
    ```
3. Commit suas alterações:
    ```bash
    git commit -am 'Adiciona nova feature'
    ```
4. Faça um push para a branch:
    ```bash
    git push origin feature/nome-da-feature
    ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Considerações Finais

O projeto GameAlert demonstrou ser uma solução eficaz para o acompanhamento de promoções de jogos. Com o uso de tecnologias robustas e a automação de processos, criamos uma ferramenta prática para os consumidores de games. Os testes confirmaram a precisão e eficiência do sistema. Planejamos futuras expansões para incluir outras plataformas de jogos e continuaremos a melhorar o sistema.

## Referências Bibliográficas

1. Python Software Foundation. Python Documentation. 2024. Disponível em: [https://docs.python.org/3/](https://docs.python.org/3/).
2. Telegram. Telegram Bot API. 2024. Disponível em: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api).
3. Selenium. Selenium Documentation. 2024. Disponível em: [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/).
4. BeautifulSoup Documentation. BeautifulSoup: We called him Tortoise because he taught us. 2024. Disponível em: [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
5. McCallum, A. Aiogram Documentation. 2024. Disponível em: [https://docs.aiogram.dev/en/latest/](https://docs.aiogram.dev/en/latest/).
6. Mitchell, R. Web Scraping with Python: Collecting More Data from the Modern Web. 2. ed. Sebastopol: O'Reilly Media, 2018.
7. McKinney, W. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython. Sebastopol: O'Reilly Media, 2017.

