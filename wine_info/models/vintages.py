import enum

from sqlalchemy.orm import composite

from ..extensions import db


vintages_tastes = db.Table('vintages_tastes',
                           db.Column('vintage_id', db.Integer,
                                     db.ForeignKey('vintages.id')),
                           db.Column('taste_id', db.Integer,
                                     db.ForeignKey('tastes.id')))


vintages_pairings = db.Table('vintages_pairings',
                             db.Column('vintage_id', db.Integer,
                                       db.ForeignKey('vintages.id')),
                             db.Column('pairing_id', db.Integer,
                                       db.ForeignKey('pairings.id')))

vintages_traits = db.Table('vintages_traits',
                           db.Column('trait_id', db.Integer,
                                     db.ForeignKey('traits.id')),
                           db.Column('vintage_id', db.Integer,
                                     db.ForeignKey('vintages.id')))


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


class Vintage(db.Model):
    __tablename__ = 'vintages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    year = db.Column(db.Integer)
    abv = db.Column(db.Float)

    body = db.Column(db.Integer)
    fruit = db.Column(db.Integer)
    earth = db.Column(db.Integer)
    tannin = db.Column(db.Integer)
    oak = db.Column(db.Integer)
    acidity = db.Column(db.Integer)

    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    region = db.relationship('Region', foreign_keys=region_id)

    tastes = db.relationship('Taste', secondary=vintages_tastes)
    pairings = db.relationship('Pairing', secondary=vintages_pairings)
    traits = db.relationship('Trait', secondary=vintages_traits)
    stats = db.relationship('WineStat', secondary='wine_stats_vintages')
    similar_wines = db.relationship('SimilarWine',
                                    order_by='SimilarWine.cluster_match')

    wine_id = db.Column(db.Integer, db.ForeignKey('wines.id'))
    wine = db.relationship('Wine', foreign_keys=wine_id)
