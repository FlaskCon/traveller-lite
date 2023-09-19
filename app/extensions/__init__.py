import os

from flask_imp import Imp
from flask_sqlalchemy import SQLAlchemy
from .email_service import EmailServiceSettings, EmailService

imp = Imp()
db = SQLAlchemy()
email_settings = EmailServiceSettings(
    os.environ.get("EMAIL_USERNAME"),
    os.environ.get("EMAIL_PASSWORD"),
    os.environ.get("EMAIL_SERVER"),
    int(os.environ.get("EMAIL_PORT")),
)

__all__ = ["email_settings", "EmailService", "db", "imp"]
