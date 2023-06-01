"""Pet Adoption Flask Application."""

from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "TopSecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)

with app.app_context():
    db.create_all()

@app.route('/')
def show_homepage():
    """Show list of pets"""
    pets = Pet.query.all()
    return render_template('pets-list.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Show form for adding pet; handle adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or 'https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif'
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f'Success! Added {species} {name} to the adoption center')
        return redirect('/')

    else:
        return render_template('pet-add-form.html', form=form)
    
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet(pet_id):
    """Show pet details and form for editing pet; handle form submission"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data or 'https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif'
        pet.notes = form.notes.data
        pet.avail = form.avail.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('show_homepage'))
    
    else:
        return render_template("pet-details.html", form=form, pet=pet)

