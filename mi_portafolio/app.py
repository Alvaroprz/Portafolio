from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre_mi')
def sobre_mi():
    return render_template('sobre_mi.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/estudios')
def estudios():
    return render_template('estudios.html')

if __name__ == '__main__':
    app.run(debug=True)