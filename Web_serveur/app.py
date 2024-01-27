# serveur/app.py

from flask import Flask, render_template, request

app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/')
def index():   
    return render_template('index.html')


# Route pour la page avec formulaire

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
