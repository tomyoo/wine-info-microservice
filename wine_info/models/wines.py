import enum

from ..extensions import db


class Brand(db.Model):
    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class WineTypes(enum.Enum):
    red = 'red'
    white = 'white'
    rose = u'rosé'
    sparkling = 'sparkling'


class Classification(db.Model):
    __tablename__ = 'classifications'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.Enum(WineTypes))


class Variety(db.Model):
    __tablename__ = 'varieties'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.Enum(WineTypes))


class Wine(db.Model):
    __tablename__ = 'wines'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
    brand = db.relationship('Brand', foreign_keys=brand_id)

    variety_id = db.Column(db.Integer, db.ForeignKey('varieties.id'))
    variety = db.relationship('Variety', foreign_keys=variety_id)

    classification_id = db.Column(db.Integer,
                                  db.ForeignKey('classifications.id'))
    classification = db.relationship('Classification',
                                     foreign_keys=classification_id)
