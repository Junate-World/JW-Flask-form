from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

# Model to store user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15))
    address = db.Column(db.String(200))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zip_code = db.Column(db.String(10))
    country = db.Column(db.String(50))
    occupation = db.Column(db.String(50))
    company = db.Column(db.String(100))
    comment = db.Column(db.String(200))

with app.app_context():
    db.create_all()

# Route to collect user information
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user_info = User(
            name=request.form['name'],
            email=request.form['email'],
            phone=request.form['phone'],
            address=request.form['address'],
            city=request.form['city'],
            state=request.form['state'],
            zip_code=request.form['zip_code'],
            country=request.form['country'],
            occupation=request.form['occupation'],
            company=request.form['company'],
            comment=request.form['comment']
        )
        db.session.add(user_info)
        db.session.commit()
        return redirect(url_for('view_users'))

    return render_template('form.html')

# Route to view and edit users
@app.route('/users')
def view_users():
    users = User.query.all()
    return render_template('users.html', users=users)

# Route to edit user information
@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.phone = request.form['phone']
        user.address = request.form['address']
        user.city = request.form['city']
        user.state = request.form['state']
        user.zip_code = request.form['zip_code']
        user.country = request.form['country']
        user.occupation = request.form['occupation']
        user.company = request.form['company']
        user.comment = request.form['comment']

        db.session.commit()
        return redirect(url_for('view_users'))

    return render_template('form.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
