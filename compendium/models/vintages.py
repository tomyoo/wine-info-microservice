from sqlalchemy.orm import composite

from ..extensions import db


class Vintage(db.Model):
    __tablename__ = 'vintages'

    id = db.Column(db.Integer, primary_key=True)
