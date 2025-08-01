# Chatbot Terminal com Groq e LLaMA3

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Um chatbot de terminal simples que utiliza a API da Groq com o modelo LLaMA3-8b para gerar respostas em tempo real.

![Image](https://github.com/user-attachments/assets/854fc553-91a0-4fac-99a4-c11d271c89c2)

## Funcionalidades

- Interface de conversa em terminal simples e intuitiva
- Utiliza o poderoso modelo LLaMA3-8b da Meta via Groq
- Streaming de respostas em tempo real
- Configuração de temperatura para controle de criatividade
- Tratamento de erros e comandos para sair

## Pré-requisitos

- Python 3.7+
- Conta na [Groq](https://console.groq.com/) (para obter uma API key)
- Variável de ambiente com sua API key

## Instalação

```bash
1. Clone o repositório:

git clone https://github.com/lucasolisouza/chatbot-ai.git
cd chatbot-ai

2. Crie e ative um ambiente virtual (recomendado):

python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Crie um arquivo .env no diretório principal (/chatbot-ai) com sua API key:

GROQ_API_KEY=sua_chave_aqui

5 Execute o chatbot:

python src/main.py
