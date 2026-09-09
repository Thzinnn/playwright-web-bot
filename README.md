# Playwright Web Bot

Automação web em Python utilizando **Playwright** para realização de login automatizado com validação de credenciais, controle de variáveis de ambiente e captura de screenshots para auditoria.

---

## 📌 Funcionalidades

- **Navegação Automatizada:** Acesso à página de login via Chromium.
- **Preenchimento de Credenciais:** Entrada de dados a partir de variáveis de ambiente (`.env`).
- **Validação de Login:** Verificação do status de autenticação através de mensagens de alerta da página.
- **Auditoria Visual:** Geração automática de screenshots dos resultados (`login_sucedido.png` ou `login_falha.png`) na pasta `auditoria/`.

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.8+](https://www.python.org/)
- [Playwright](https://playwright.dev/python/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina.

### 2. Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd playwright-web-bot
```

### 3. Criar e Ativar o Ambiente Virtual (Opcional, mas recomendado)

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar as Dependências

```bash
pip install -r requirements.txt
playwright install
```

### 5. Configurar as Variáveis de Ambiente

Copie o arquivo de exemplo `.env.example` para `.env`:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e defina suas credenciais:

```env
APP_USER=tomsmith
APP_PASSWORD=SuperSecretPassword!
```

> **Nota:** Para o site de testes (*The Internet Herokuapp*), as credenciais padrão válidas são:
> - **Usuário:** `tomsmith`
> - **Senha:** `SuperSecretPassword!`

### 6. Executar o Bot

```bash
python bot.py
```

---

## 📁 Estrutura do Projeto

```text
playwright-web-bot/
├── auditoria/          # Armazenamento de screenshots gerados pela automação
├── .env.example        # Modelo de variáveis de ambiente
├── .gitignore          # Arquivos e pastas ignorados pelo Git
├── bot.py              # Script principal de automação
├── README.md           # Documentação do projeto
└── requirements.txt    # Dependências do projeto
```

---

## 📄 Licença

Este projeto é de livre uso para fins educacionais e de estudo.
