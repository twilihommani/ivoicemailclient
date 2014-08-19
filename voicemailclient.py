import twilio.twiml

from flask import Flask, render_template, request
 
app = Flask(__name__)
api_url = "your API url goes here" # To replace
app.debug=True

"""
This app illustrate the capability to call anyone from a browser.
"""
@app.route('/client', methods=['GET', 'POST'])
def client():
    return render_template('client.html', url = api_url)
 
if __name__ == "__main__":
    app.run(debug=True)
