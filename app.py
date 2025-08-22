from flask import Flask

#Cria uma instância da aplicação Flask e guarda em app.

#__name__ é o nome do módulo Python atual. O Flask usa esse valor para:
app = Flask(__name__)

# @app.route('/') diz: “quando alguém acessar o caminho / (a raiz), chame a função logo abaixo”.
@app.route('/')

#Função que será executada quando a rota / for acessada.
def home():
    return 'Hello World!'

#garante que o código dentro só rode quando você executar este arquivo diretamente
if __name__ == "__main__":

#Inicia o servidor de desenvolvimento embutido do Flask
    app.run()