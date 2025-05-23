from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import ContactoForm

app= Flask(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/agenda_contactos'
app.config['SECRET_KEY'] = 'clave_secreta'
db = SQLAlchemy(app)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_contactos():
    form= ContactoForm()

    return render_template('agregar.html')

@app.route('/')
def listar_contactos():
    return render_template('listar.html')