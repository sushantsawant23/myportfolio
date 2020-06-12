from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as csvfile:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Something went wrong. Try again!"


#@app.route('/index.html')
#def home():
#    return render_template('index.html')

#@app.route('/about.html')
#def about():
#    return render_template('about.html')

#@app.route('/works.html')
#def works():
#    return render_template('works.html')

#@app.route('/work.html')
#def work():
#    return render_template('work.html')

#@app.route('/contact.html')
#def contact():
#    return render_template('contact.html')

