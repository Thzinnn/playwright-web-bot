from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()



def executar_login(usuario, senha):
    with sync_playwright() as p:
        browser = None
        os.makedirs("auditoria", exist_ok=True)
        try:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://the-internet.herokuapp.com/login")
            print(page.title())
            page.locator("#username").fill(usuario)
            page.locator("#password").fill(senha)
            page.locator("button[type='submit']").click()
            alerta = page.locator("#flash").inner_text()
            if " You logged into a secure area!" in alerta:
                print("Sucesso ao logar")
                page.screenshot(path='auditoria/login_sucedido.png')
                return True
            else:
                print("Falha ao logar, credenciais inválidas")
                page.screenshot(path='auditoria/login_falha.png')
                return False
   
            
        finally:
            if browser:
                browser.close()
        
if __name__ == "__main__":
    usuario = os.getenv("APP_USER")
    senha = os.getenv("APP_PASSWORD")
    status = executar_login(usuario, senha)
    print(f"Status retornado: {status}")
    
