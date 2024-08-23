# Chatbot Flask com LLM

Este projeto é um chatbot simples implementado em Flask, que utiliza um modelo de linguagem para responder às mensagens dos usuários. Abaixo estão as instruções para configurar e executar o projeto.

## Estrutura do Projeto

- `main.py`: Arquivo principal que define as rotas do Flask e lida com as requisições.
- `model.py`: Contém a lógica para interagir com o modelo de linguagem LLM.
- `templates/home.html`: Arquivo HTML para a interface do chatbot.

## Pré-requisitos

Certifique-se de ter o Python 3.8 ou superior instalado. Também será necessário instalar as dependências do projeto.

## Instalação

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA_DO_REPOSITORIO>
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

   As dependências incluem Flask e langchain_community.

## Configuração

1. **Modelo de Linguagem**: Este projeto utiliza o modelo `llama3` da biblioteca `langchain_community`. Certifique-se de ter as intalado o modelo correto para executar o código.

## Executando o Projeto

Para iniciar o servidor Flask, execute:

```bash
python main.py
```

O servidor estará disponível em `http://127.0.0.1:5000/`.

## Utilização

1. Abra o navegador e vá para `http://127.0.0.1:5000/`.
2. Envie uma mensagem no campo de entrada e clique em "Enviar" ou pressione Enter.
3. O chatbot responderá com base no modelo de linguagem.

## Estrutura dos Arquivos

### `main.py`

Define as rotas principais do Flask:

- `/`: Renderiza a página inicial.
- `/get_response`: Recebe uma mensagem do usuário e retorna uma resposta do modelo de linguagem.

### `model.py`

Contém a lógica para formatar o prompt e obter a resposta do modelo de linguagem `llama3`.

### `templates/home.html`

Interface HTML para o chatbot, incluindo o estilo e a lógica JavaScript para interatividade.

## Contribuições

Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request com suas melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Sinta-se à vontade para ajustar qualquer seção conforme necessário!