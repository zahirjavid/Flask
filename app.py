import gspread
from flask import Flask, render_template, request

gc = gspread.service_account(filename = 'flask-profile.json')
sh = gc.open('flask-profile')

shProfile = sh.get_worksheet(0)
shContacts = sh.get_worksheet(1)


app= Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
   if request.method == 'POST':
      shContacts.append_row([request.form['name'], request.form['email'], request.form['message']])

   profile = {
        'About' : shProfile.acell('B1').value,
        'Interests' : shProfile.acell('B2').value,
        'Experience' : shProfile.acell('B3').value,
        'Education' : shProfile.acell('B4').value,
   }
   return render_template("index.html", profile = profile)

@app.route('/contact')  
def contact():
   return render_template("contacts.html")

if __name__ == "__main__":
    app.run(debug=True) 

