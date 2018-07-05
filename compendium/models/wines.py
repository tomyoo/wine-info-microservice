import enum

from ..extensions import db


class Brand(db.Model):
    __tablename__ = 'brands'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class WineTypes(enum.Enum):
    red = 'red'
    white = 'white'
    rose = u'rosé'
    sparkling = 'sparkling'


class Classification(db.Model):
    __tablename__ = 'classifications'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.Enum(WineTypes))


class Variety(db.Model):
    __tablename__ = 'varieties'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.Enum(WineTypes))


class Wine(db.Model):
    __tablename__ = 'wines'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
    brand = db.relationship('Brand', foreign_keys=brand_id)

    variety_id = db.Column(db.Integer, db.ForeignKey('varieties.id'))
    variety = db.relationship('Variety', foreign_keys=variety_id)

    classification_id = db.Column(db.Integer,
                                  db.ForeignKey('classifications.id'))
    classification = db.relationship('Classification',
                                     foreign_keys=classification_id)
