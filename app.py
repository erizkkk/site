from flask import Flask, render_template

app = Flask(__name__)

# Mensagens que você quer mostrar (coloque as suas aqui)
mensagens = [
    "oque é um ponto vermelho no oceano? um redMoinho",
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "ainda não sei oque digitar aqui",
    "n tanko meu azar com as maquinas qnd to ctg",
    "segredo: acho fofo quando oc sorri"
]

@app.route('/')
def home():
    return render_template('index.html', mensagens=mensagens)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

