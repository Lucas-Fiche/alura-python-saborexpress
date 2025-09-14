import os

def exibir_menu_programa():
        print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        
    ₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌
    1. 𝘾𝙖𝙙𝙖𝙨𝙩𝙧𝙖𝙧 𝙍𝙚𝙨𝙩𝙖𝙪𝙧𝙖𝙣𝙩𝙚
    2. 𝙇𝙞𝙨𝙩𝙖𝙧 𝙍𝙚𝙨𝙩𝙖𝙪𝙧𝙖𝙣𝙩𝙚
    3. 𝘼𝙩𝙞𝙫𝙖𝙧 𝙍𝙚𝙨𝙩𝙖𝙪𝙧𝙖𝙣𝙩𝙚
    4. 𝙎𝙖𝙞𝙧
    ₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌
    """)

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: \n'))

    match opcao_escolhida:
        case 1:
            cadastrar_restaurante()
        case 2:
            listar_restaurante()
        case 3:
            ativar_restaurante()
        case 4:
            finalizar_app()
        case _:
            print('Opção Inválida')

def cadastrar_restaurante():
    print('Cadastrar Restaurante')

def listar_restaurante():
    print('Listar Restaurante')

def ativar_restaurante():
    print('Ativar Restaurante')

def finalizar_app():
    os.system('clear')
    print('Finalizando app...')
    
def main():
    exibir_menu_programa()
    escolher_opcao()

if __name__ == '__main__':
    main()
