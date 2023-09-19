Flask Email Sender
A simple Flask application to send emails.

Features
* Web-based email sending form.
* Allows sending emails to custom recipients.
* Simple and user-friendly UI.

Setup and Installation
Prerequisites
* Python 3.x
* pip

Steps
1. Clone the Repository
git clone <repository-url>
cd <repository-directory>
2. Setup a Virtual Environment (optional, but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
python app.py

Once running, the application will be accessible at http://127.0.0.1:5000/send_email.

Usage
1. Navigate to http://127.0.0.1:5000/send_email.
2. Fill in the recipient's email, subject, and message.
3. Click "Send Email" to send the email.

Customization
* The SMTP settings can be customized in app.py. Make sure to use secure and valid credentials.
* You can adjust the look and feel of the application by modifying the styles in templates/email_form.html.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
This project is open-source. Feel free to use and distribute.
