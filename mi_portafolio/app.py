from flask import Flask, render_template, request, flash, redirect, url_for
# from flask_mail import Mail, Message  # Comentado por ahora

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # ¡Importante! Cambia esto por algo seguro

# Configuración de Flask-Mail (comentado por ahora)
# app.config['MAIL_SERVER'] = 'smtp.example.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'tu_correo@example.com'
# app.config['MAIL_PASSWORD'] = 'tu_contraseña'
# mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre_mi')
def sobre_mi():
    return render_template('sobre_mi.html')

@app.route('/proyectos')
def proyectos():
    lista_proyectos = [
        {
            'nombre': 'ARKANOID',
            'descripcion': 'Versión del clásico juego Arkanoid con pygame',
            'tecnologias': 'Python, Pygame',
            'enlace_codigo': 'https://github.com/Alvaroprz/ARKANOID',
            'enlace_demo': None
        },
        {
            'nombre': 'Pong',
            'descripcion': 'Versión del clásico juego Pong hecho con Python y pygame.',
            'tecnologias': 'Python, Pygame',
            'enlace_codigo': 'https://github.com/Alvaroprz/pong',
            'enlace_demo': None
        },
        {
            'nombre': 'Este Portafolio Web',
            'descripcion': 'Un portafolio personal desarrollado con Python y Flask para mostrar mis habilidades y proyectos.',
            'tecnologias': 'Python, Flask, HTML, CSS',
            'enlace_codigo': 'https://github.com/Alvaroprz/Portafolio',
            'enlace_demo': None
        },
        {
            'nombre': 'Cursus 42 Telefónica',
            'descripcion': 'Aqui tengo varios proyectos, como una libreria propia.',
            'tecnologias': 'C',
            'enlace_codigo': 'https://github.com/Alvaroprz/Personal_cursus42',
            'enlace_demo': None
        }
        # Añade más proyectos aquí con su información
    ]
    return render_template('proyectos.html', proyectos=lista_proyectos)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        print(f"Nuevo mensaje de: {nombre} <{email}>")
        print(f"Mensaje: {mensaje}")
        flash('¡Gracias por tu mensaje! Te responderé pronto.', 'success')
        return redirect(url_for('contacto'))  # Redirigimos a la misma página
    return render_template('contacto.html')

@app.route('/estudios')
def estudios():
    return render_template('estudios.html')

if __name__ == '__main__':
    app.run(debug=True)