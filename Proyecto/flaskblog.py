from flask import Flask, render_template
app = Flask(__name__)
#dummy data
posts = [
    {
        'author': 'Benjamin Reynoso',
        'title': 'Funny how we live',
        'content':'First post',
        'date': '19/12/2020'
    },
    {
        'author': 'Noe Reynoso',
        'title': 'Forza nocta',
        'content':'Drake`s new album',
        'date': '18/01/2020'
    }
]


#multiples decoradores para una vista
@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',title='about')

#el debugger permitira renderizar cambios sin tener que reinicciar el servidor    
if __name__ == '__main__':
    app.run(debug=True)