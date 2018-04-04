from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Sup3r$3cretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://fabgcikbqoicpw:b8747586a30a12b2 96b53c1c164f97d06174960f03d360f27da9a1cb9ff80d51@ec2-54-235-146-51.compute-1.amazonaws.com:5432/dcvckb782jc0ct 
"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config.from_object(__name__)
db = SQLAlchemy(app)

# Config Values
# location where file uploads will be stored
UPLOAD_FOLDER = './app/static/uploads'
# needed for session security, the flash() method in this case stores the message
# in a session
SECRET_KEY = 'Sup3r$3cretkey'



from app import views