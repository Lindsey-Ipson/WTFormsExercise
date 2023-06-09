from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField(
        'Pet Name',
        validators=[InputRequired()]
        )
    
    species = SelectField(
        'Species',
        choices=[('dog', 'Dog'), ('cat', 'Cat'), ('rabbit', 'Rabbit'), ('fish', 'Fish')]
        )
    
    photo_url = StringField(
        'Pet Image URL',
        validators=[Optional(), URL()]
        )

    age = IntegerField(
        'Age',
        validators=[Optional(), NumberRange(min=0, max=30)]
        )
    
    notes = TextAreaField(
        'Comments',
        validators=[Optional(), Length(min=10)]
        )
    
class EditPetForm(FlaskForm):
    """Form for editing pet"""

    photo_url = StringField(
        'Pet Image URL',
        validators=[Optional(), URL()]
        )
    
    notes = TextAreaField(
        'Comments',
        validators=[Optional(), Length(min=10)]
        )
    
    avail = BooleanField(
        'Available',
        )

    




