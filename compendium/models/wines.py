from sqlalchemy.orm import composite

from ..extensions import db


class Wine(db.Model):
    __tablename__ = 'wines'

    id = db.Column(db.Integer, primary_key=True)
