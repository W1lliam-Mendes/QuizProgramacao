from flask import Flask, render_template, request

app = Flask(__name__)

simbolos = "!@#$%^&*()-_=+[{]};:'\",<.>/?|\\"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enviar', methods=["POST"])

def processarQuiz():
    respostaP1 = request.form.get("pergunta1")
    respostaP2 = request.form.get("pergunta2")
    respostaP3 = request.form.get("pergunta3")
    respostaP4 = request.form.get("pergunta4")
    respostaP5 = request.form.getlist("pergunta5")
    respostaP6 = request.files.get("pergunta6")
    respostaP7 = request.form.get("pergunta7")
    respostaP8 = request.form.get("pergunta8")
    pontos = 0

    if respostaP1 == "HTML" or respostaP1 == "html":
        pontos = pontos + 1

    if respostaP2 == "dominio" or respostaP2 == "Dominio":
        pontos = pontos + 1

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    if respostaP3:
        for caractere in respostaP3:
            if caractere.isupper():
                tem_maiuscula = True
            elif caractere.islower():
                tem_minuscula = True
            elif caractere.isdigit():
                tem_numero = True
            elif caractere in simbolos:
                tem_especial = True

    if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        pontos = pontos + 1

    if respostaP4 and "1991" in respostaP4:
        pontos = pontos + 1

    if "Python" in respostaP5 and "JavaScript" in respostaP5 and len(respostaP5) == 2:
        pontos = pontos + 1

    if respostaP6: 
        pergunta6 = respostaP6.filename
        if pergunta6.lower().endswith('.html'):
            pontos = pontos + 1


    if respostaP7 == "Type" or respostaP7 == "type":
        pontos = pontos + 1

    if respostaP8 == "java" or respostaP8 == "Java":
        pontos = pontos + 1

    return render_template('enviar.html', pontos=pontos)

if __name__ == '__main__':
    app.run(debug=True)