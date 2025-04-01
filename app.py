# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/warehouse')
def warehouse():
    return render_template('warehouse.html')

@app.route('/crowd')
def crowd():
    return render_template('crowd.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Here you would typically:
        # 1. Save this to a database
        # 2. Send an email notification
        # 3. Process the data as needed
        
        # For now we'll just print the data (in a real app, you'd handle this properly)
        print(f"Contact form submission: {name}, {email}, {subject}, {message}")
        
        # Redirect back to home with a success parameter
        return redirect(url_for('home', contact_success=True))

if __name__ == '__main__':
    app.run(debug=True)