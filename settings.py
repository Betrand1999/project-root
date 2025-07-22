from dotenv import load_dotenv
import os
load_dotenv()

MONGO_URI=os.environ.get('MONGO_URI')
SECRET_KEY=os.environ.get('SECRET_KEY','your_secret_key')
EMAIL_USER=os.environ.get('EMAIL_USER', 'default_email_user')
EMAIL_PASS=os.environ.get('EMAIL_PASS', 'default_email_password')
SMTP_SERVER=os.environ.get('SMTP_SERVER', 'default_smtp_server')
SMTP_PORT=os.environ.get('SMTP_PORT', 587)  # Default SMTP port for TLS
AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION=os.getenv("AWS_REGION")
MONGO_USERNAME=os.getenv('MONGO_USERNAME', "")
MONGO_PASSWORD=os.getenv('MONGO_PASSWORD')
COGNITO_CLIENT_ID = os.getenv("COGNITO_CLIENT_ID")
COGNITO_CLIENT_SECRET = os.getenv("COGNITO_CLIENT_SECRET")

