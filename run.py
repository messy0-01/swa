from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

# Create a database connection

app = Flask(__name__)
app.secret_key = "flash message"

app.config['MYSQL_HOST'] ="localhost"
app.config['MYSQL_USER'] ="root"
app.config['MYSQL_PASSWORD'] =""
app.config['MYSQL_DB'] ="qsasa"

mysql = MySQL(app)


@app.route('/')
def list_participants():
    #Retrieve the list of participants from the database
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    user = cur.fetchall()
    cur.close()
    return render_template('index.html', participant=user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        telephon = request.form['telephon']

        #Save the participant's information to the database
        cur = mysql.connection.cursor()

        # Insérer les données dans la table 'produit'
        cur.execute("INSERT INTO user (nom, prenom, email, telephon) VALUES (%s, %s, %s, %s)", (nom, prenom, email,telephon))

        # Valider la transaction
        mysql.connection.commit()

        # Fermer la connexion à la base de données
        cur.close()

        return redirect(url_for('list_participants'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)