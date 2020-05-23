from flask import Flask
from flask import render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.fields import StringField
from wtforms.widgets import TextArea

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'

class UploadForm(FlaskForm):
    file = FileField()
    body = StringField(u'Text', widget=TextArea())

@app.route('/', methods=['GET', 'POST'])
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        filename = form.file.data.filename
        form.file.data.save('uploads/' + filename)
        ucapan = form.body.data
        ucapans = {}
        names = open('uploads/names.txt', "r")
        for name in names:
            result = ucapan.replace('Name', name.strip('\n'));
            ucapans[name] = result 
        print(ucapans)
        return render_template('result.html', ucapans=ucapans) 

    return render_template('index.html', form=form)
