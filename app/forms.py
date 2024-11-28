from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, SelectField
from wtforms.validators import DataRequired
import re

class SearchForm(FlaskForm):
    city = StringField("Stadt")
    postal_code = StringField("Postleitzahl")
    submit = SubmitField("Suchen")
    amount = SelectField(
        'Anzahl',
        choices=[
            ('5', '5'),
            ('10', '10'),
            ('15', '15'),
            ('20', '20')
        ],
        default='5',
        validators=[DataRequired()]
    )
    
    def validate_postal_code(self, field):
        postal_code = field.data
        
        if postal_code and not re.fullmatch(r'\d{5}', postal_code):
            raise ValidationError("Die Postleitzahl muss genau 5 Ziffern enthalten.")
    
    def validate(self, extra_validators=None):
        if not super(SearchForm, self).validate(extra_validators=extra_validators):
            return False
        
        if not self.city.data and not self.postal_code.data:
            self.city.errors.append("Entweder Stadt oder Postleitzahl muss angegeben werden.")
            self.postal_code.errors.append("Entweder Stadt oder Postleitzahl muss angegeben werden.")
            return False

        return True