import os

lista_restaurantes = [{'nome':'Praça', 'categoria': 'Japonesa', 'ativo': False},
                      {'nome': 'Pizza Suprema', 'categoria': 'Pizza Italiana', 'ativo': True},                  
                      {'nome': 'Mexican', 'categoria': 'Mexicano', 'ativo': True}]

def exibir_menu_programa():
        ''' Essa função é responsável por exibir o menu do programa'''
        print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        
    ₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌
    𝟭. 𝗖𝗮𝗱𝗮𝘀𝘁𝗿𝗮𝗿 𝗥𝗲𝘀𝘁𝗮𝘂𝗿𝗮𝗻𝘁𝗲
    𝟮. 𝗟𝗶𝘀𝘁𝗮𝗿 𝗥𝗲𝘀𝘁𝗮𝘂𝗿𝗮𝗻𝘁𝗲
    𝟯. 𝗔𝗹𝘁𝗲𝗿𝗮𝗿 𝗘𝘀𝘁𝗮𝗱𝗼 𝗱𝗼 𝗥𝗲𝘀𝘁𝗮𝘂𝗿𝗮𝗻𝘁𝗲
    𝟰. 𝗦𝗮𝗶𝗿
    ₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌₌
    """)

def voltar_ao_menu_principal():
    ''' Essa função é responsável por voltar ao menu principal'''
    input('Digite uma tecla para voltar ao menu principal...')
    main()

def exibir_subtitulo(texto):
    ''' Essa função é responsável por exibir o subtitulo de cada página'''
    os.system('clear')
    linha = '*' * (len(texto)) 
    print(linha)
    print(texto)
    print(linha)
    print()

def alternar_estado_restaurante():
    ''' Essa função é responsável por alterar o estado de um restaurante'''
    exibir_subtitulo('Alternando Estado do Restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in lista_restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado =  True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi encontrado e ativado!\n' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com suecesso!\n'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado. \n')

    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Essa função é responsável por escolher a opção que será executada'''
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
    except ValueError:
        opcao_invalida()
    
def cadastrar_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de Novos Restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite o nome da Categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    lista_restaurantes.append(dados_restaurante)
    print(f'\nRestaurante {nome_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurante():
    ''' Essa função é responsável por listar os restaurantes'''
    exibir_subtitulo('Lista de Restaurantes')

    print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)} |')
    for restaurante in lista_restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'

        print(f'-> | {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante.ljust(20)} |')
       
    print('\n')
    voltar_ao_menu_principal()

def ativar_restaurante():
    ''' Essa função é responsável por ativar um restaurante'''
    print('Ativar Restaurante\n')
    alternar_estado_restaurante()
    voltar_ao_menu_principal()

def finalizar_app():
    ''' Essa função é responsável por finalizar o app'''
    exibir_subtitulo('Finalizando app...')

def opcao_invalida():
    ''' Essa função é responsável por indicar uma opção incorreta escolhida pelo usuário'''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def main():
    os.system('clear')
    exibir_menu_programa()
    escolher_opcao()

if __name__ == '__main__':
    main()
