from flask import Flask, request, render_template, url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/')
def inicio():
    app.logger.info(f'mensaje a nivel debug{request.path}')
    return 'Nueva aplicacion 2022'


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre}'

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es {edad}'

@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='juan'))

@app.route('/salir')
def salir():
    return abort(404)










if __name__ == '__main__':
  app.run(debug=True)