import twilio.twiml
import sys

from flask import Flask, render_template, request
from twilio.util import TwilioCapability
 
app = Flask(__name__)
app.config.from_pyfile('client.cfg')
app.debug=True

'''
This client allow to feed a contact API through a form
'''
@app.route('/', methods=['GET', 'POST'])
def client():
    return render_template('client.html', url = app.config['API_URL'])
 
if __name__ == "__main__":
    app.run(debug=True)
