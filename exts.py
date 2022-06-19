from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from utils.alidayu import AlidayuAPI

mail = Mail()
db = SQLAlchemy()
alidayu = AlidayuAPI()


