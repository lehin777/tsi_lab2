from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "some_secret_key"

def send_email_via_smtp(subject, message, to_email):
    sender_email = "rigafortest@gmail.com"
    sender_password = "riga1234"

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to_email, msg.as_string())
    server.quit()

@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        recipient = request.form['recipient']
        subject = request.form['subject']
        message = request.form['message']
        try:
            send_email_via_smtp(subject, message, recipient)  
            flash('Email sent successfully!', 'success')
        except:
            flash('Failed to send email. Try again later.', 'error')
        return redirect(url_for('send_email'))
    
    return render_template('email_form.html')


if __name__ == "__main__":
    app.run(debug=True)
