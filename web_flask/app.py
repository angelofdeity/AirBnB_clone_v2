from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
HBNB_MYSQL_USER = 'hbnb_dev'
HBNB_MYSQL_PWD = 'hbnb_dev_pwd'
HBNB_MYSQL_HOST = 'localhost'
HBNB_MYSQL_DB = 'hbnb_dev_db'
# HBNB_MYSQL_PORT = getenv('HBNB_MYSQL_PORT')
HBNB_ENV = 'dev'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Place model
class Place(db.Model):
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    city_id = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'<Place id={self.id} name={self.name} city_id={self.city_id} user_id={self.user_id}>'

# Define a simple route to test the app
@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
