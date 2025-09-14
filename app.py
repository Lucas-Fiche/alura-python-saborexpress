import os

lista_restaurantes = ['Taikan', 'Mc Donalds', 'Burguer King', 'Giraffas']

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

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal...')
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def escolher_opcao():
    try:
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
                opcao_invalida()
    except:
        opcao_invalida()
    
def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de Novos Restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    lista_restaurantes.append(nome_restaurante)
    print(f'\nRestaurante {nome_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Lista de Restaurantes')

    for restaurante in lista_restaurantes:
        print('-', restaurante)
        
    print('\n')
    voltar_ao_menu_principal()

def ativar_restaurante():
    print('Ativar Restaurante\n')
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Finalizando app...')

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def main():
    os.system('clear')
    exibir_menu_programa()
    escolher_opcao()

if __name__ == '__main__':
    main()
