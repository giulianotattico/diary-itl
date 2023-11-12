# Import
from flask import Flask, render_template,request, redirect
# Collegare la libreria del database
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Connettere SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creare il DB
db = SQLAlchemy(app)
# Creare la tabella

class Card(db.Model):
    # Creazione delle colonne
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Titolo
    title = db.Column(db.String(100), nullable=False)
    # Sottotitolo
    subtitle = db.Column(db.String(300), nullable=False)
    # Testo
    text = db.Column(db.Text, nullable=False)

    # Visualizzazione dell'oggetto e dell'id
    def __repr__(self):
        return f'<Card {self.id}>'
    

#Consegna #2. Creare la tabella User









# Running the content page
@app.route('/', methods=['GET','POST'])
def login():
        error = ''
        if request.method == 'POST':
            form_login = request.form['email']
            form_password = request.form['password']
            
            #Assignment #4. Implement authorisation
            


            
        else:
            return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        login= request.form['email']
        password = request.form['password']
        
        #Assignment #3. Make it so that the user's data is recorded to the database
        

        
        return redirect('/')
    
    else:    
        return render_template('registration.html')


# Running the content page
@app.route('/index')
def index():
    # Displaying the databaase entries
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Running the page with the entry
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Running the entry creation page
@app.route('/create')
def create():
    return render_template('create_card.html')

# The entry forn
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Creating an object that will be sent to the DB
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')





if __name__ == "__main__":
    app.run(debug=True)
