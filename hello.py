from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World<h1>'

@app.route('/user/<name>')
def user(name):
    #al importar el objeto request podemos obtener atributos de este
    #en esta sentencia request es una variable global
    user_agent = request.headers.get('User-Agent')
    #Permite formataear la cadena en cierto lugar como el lenguaje C.
    return '<h1>Hello, %s!, %s</h1>' % (name, user_agent)

print(app.url_map)




if __name__ == '__main__':
    app.run(debug=True)