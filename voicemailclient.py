import twilio.twiml
import requests
import sys

from flask import Flask, render_template, redirect
from twilio.util import TwilioCapability
from form import ContactForm
 
app = Flask(__name__)
app.config.from_pyfile('client.cfg')
app.debug=True

'''
This client allow to feed a contact API through a form
'''

url = app.config['API_URL']

@app.route('/', methods=('GET', 'POST'))
def index():
    form = ContactForm()
    return render_template('client.html', form=form)

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = ContactForm()
    if form.validate_on_submit():
        requests.post(url, data = form.data)
        return redirect('/')
    return render_template('client.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
