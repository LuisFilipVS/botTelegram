# 🤖 Bot Básico de Comandos e Interação no Telegram

Um bot simples para o Telegram desenvolvido em Python, utilizando a biblioteca `pyTelegramBotAPI` (telebot). Este projeto serve como um **ponto de partida** para a criação de bots com respostas a comandos estáticos.

## 🌟 Funcionalidades

O bot está configurado para responder aos seguintes comandos e a qualquer mensagem de texto genérica:

| Comando | Função |
| :--- | :--- |
| `/help` | Exibe a lista de comandos disponíveis e uma mensagem de boas-vindas. |
| `/order` | Instruções sobre como iniciar um novo pedido (Ponto de partida para a lógica de pedidos). |
| `/status` | Instruções para verificar o status de um pedido. |
| `/cancel` | Instruções para cancelar um pedido. |
| **Qualquer Texto** | Responde com uma mensagem de boas-vindas e a lista de comandos. |

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **`pyTelegramBotAPI`** (biblioteca `telebot`)

## 🚀 Como Rodar o Bot Localmente

Siga estas etapas para configurar e executar o bot em seu ambiente local.

### 1. Pré-requisitos

* Python 3 instalado.
* Uma conta no Telegram e o **Token de API** do seu bot (obtido via **@BotFather**).

### 2. Instalação de Dependências

Instale a biblioteca `pyTelegramBotAPI`:

```bash
pip install pyTelegramBotAPI