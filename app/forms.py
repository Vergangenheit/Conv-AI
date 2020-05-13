from wtforms import (Form, TextField, validators, SubmitField)

class ReusableForm(Form):

    seed = TextField("Type a message...", validators=[validators.InputRequired()])

    #submit button
    button = SubmitField("Enter")
