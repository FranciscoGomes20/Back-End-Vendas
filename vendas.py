import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:'+os.getenv("PASSWORD")+'@'+os.getenv("HOST")+':'+os.getenv("PORT")+'/'+os.getenv("DB")
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

from app import routes, models

if __name__ == '__main__':
    app.run()
