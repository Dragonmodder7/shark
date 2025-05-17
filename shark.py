import os
import time
import smtplib
import requests
from colorama import Fore, Style, init
from email.mime.text import MIMEText

init(autoreset=True)

def banner():
    os.system("clear")
    print(Fore.BLUE + Style.BRIGHT + """
░██████╗██╗░░██╗░█████╗░██████╗░██╗░░██╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██║░██╔╝
╚█████╗░███████║███████║██████╔╝█████═╝░
░╚═══██╗██╔══██║██╔══██║██╔══██╗██╔═██╗░
██████╔╝██║░░██║██║░░██║██║░░██║██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
""" + Fore.CYAN + "🦈 SHARK SPAMMER TOOL\n📱By Jhon Lamderberguer\n🐲 Família Flodder Techno 🌐\n")

def gerar_email_temporario():
    nome = f"shark{int(time.time())}"
    return f"{nome}@1secmail.com"

def enviar_email(smtp_server, smtp_port, smtp_user, smtp_pass, alvo, assunto, msg, fake_from):
    mime = MIMEText(msg)
    mime["Subject"] = assunto
    mime["From"] = fake_from
    mime["To"] = alvo

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_user, smtp_pass)
            server.send_message(mime)
        return True
    except Exception as e:
        print(Fore.RED + f"Erro: {e}")
        return False

def menu():
    print(Fore.YELLOW + "==== ☛ MENU SHARK ☚ ====")
    to = input(Fore.LIGHTWHITE_EX + "Alvo (email): ")
    assunto = input("Assunto: ")
    mensagem = input("Mensagem: ")
    amount = int(input("Quantidade: "))

    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    smtp_user = input(Fore.LIGHTBLUE_EX + "\nSeu Gmail (com senha de app): ")
    smtp_pass = input("Senha do App Gmail: ")

    print(Fore.LIGHTGREEN_EX + "\n[+] Enviando...\n")

    for i in range(1, amount + 1):
        fake = gerar_email_temporario()
        status = enviar_email(smtp_server, smtp_port, smtp_user, smtp_pass, to, assunto, mensagem, fake)
        if status:
            print(Fore.GREEN + f"[{i}] Enviado como {fake}")
        else:
            print(Fore.RED + f"[{i}] Falhou")
        time.sleep(1)

    print(Fore.MAGENTA + "\n✔️ Concluído!")

if __name__ == "__main__":
    banner()
    menu()
