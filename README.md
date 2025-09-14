# Sabor Express | Curso "Python: Desenvolvendo sua primeira aplicação"

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=yellow)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Projeto de um aplicativo de gerenciamento de restaurantes em modo console, desenvolvido como parte do curso **"Python: Desenvolvendo sua primeira aplicação"** da [Alura](https://www.alura.com.br). O foco principal do projeto é aplicar os conceitos fundamentais da linguagem Python, como tipos de dados, laços de repetição, condicionais e funções.

## 🚀 Sobre o Projeto

O Sabor Express é uma aplicação de console que permite ao usuário interagir com um menu para gerenciar restaurantes. Ele permite cadastrar novos restaurantes, listar os já existentes e atribuir avaliações. O projeto foi estruturado para praticar a lógica de programação e a organização de código em Python de forma clara e funcional.

### ✨ Funcionalidades

* Exibição de um menu de opções para o usuário.
* Cadastro de novos restaurantes, incluindo nome, categoria e status.
* Listagem de todos os restaurantes cadastrados com suas informações.
* Alternância do estado de ativação de um restaurante.
* Atribuição de notas para os restaurantes.

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal para toda a lógica da aplicação.

## 🧠 Principais Aprendizados e Conceitos Aplicados

Este projeto foi essencial para construir minha base em programação com Python. Os principais tópicos abordados e praticados foram:

#### 1. **Variáveis e Tipos de Dados**
   - Utilização de variáveis para armazenar dados como nomes de restaurantes, categorias e notas.
   - Aplicação de diferentes tipos de dados, como `string` para textos, `int` e `float` para números, e `boolean` para o status de ativação.

#### 2. **Estruturas de Dados**
   - Uso de **listas** para armazenar a coleção de restaurantes.
   - Emprego de **dicionários** para representar cada restaurante de forma estruturada, com pares de chave-valor (ex: `'nome': 'Cantina Italiana'`).

#### 3. **Controle de Fluxo**
   - Implementação de laços de repetição `for` para percorrer a lista de restaurantes e exibi-los.
   - Uso de estruturas condicionais `if`, `elif` e `else` para criar a lógica do menu de opções e validar as escolhas do usuário.

#### 4. **Funções**
   - Criação de funções para modularizar o código e evitar repetição (princípio DRY - Don't Repeat Yourself).
   - Cada funcionalidade principal (cadastrar, listar, etc.) foi encapsulada em sua própria função, tornando o código mais organizado e legível.

#### 5. **Boas Práticas de Código**
   - Utilização da função `os.system('cls')` ou `'clear'` para limpar o console e melhorar a experiência do usuário.
   - Adoção de padrões de nomenclatura claros para variáveis e funções.
   - Organização do código para que o fluxo principal da aplicação (no `if __name__ == '__main__':`) seja fácil de entender.

## 📂 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o Sabor Express em sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Lucas-Fiche/alura-python-saborexpress.git
    cd alura-python-saborexpress
    ```

2.  **Execute a aplicação:**
    Não é necessário instalar dependências. Basta ter o Python instalado em sua máquina e executar o arquivo principal.
    ```bash
    python app.py 
    ```
    *Observação: Se o seu arquivo principal tiver outro nome, como `main.py`, altere o comando acima.*

3.  **Interaja com a aplicação:**
    O menu de opções será exibido no seu terminal. Siga as instruções para usar o programa.

## 👨‍💻 Autor

Projeto desenvolvido por **Lucas Fiche** como parte dos estudos na plataforma Alura.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/lucas-fiche-76aa24201)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Lucas-Fiche)