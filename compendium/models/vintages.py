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

vintages_grapes = db.Table('vintages_grapes',
                           db.Column('grape_id', db.Integer,
                                     db.ForeignKey('grapes.id')),
                           db.Column('vintage_id', db.Integer,
                                     db.ForeignKey('vintages.id')))


class Taste(db.Model):
    __tablename__ = 'tastes'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Pairing(db.Model):
    __tablename__ = 'pairings'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Trait(db.Model):
    __tablename__ = 'traits'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    
    
class Grape(db.Model):
    __tablename__ = 'grapes'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Region(db.Model):
    __tablename__ = 'regions'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    parent_id = db.Column(db.Integer, nullable=True)


class Vintage(db.Model):
    __tablename__ = 'vintages'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    abv = db.Column(db.Float)

    tasting_note = db.Column(db.Text)
    short_tasting_note = db.Column(db.Text)

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
    grapes = db.relationship('Grape', secondary=vintages_grapes)

    wine_id = db.Column(db.Integer, db.ForeignKey('wines.id'))
    wine = db.relationship('Wine', foreign_keys=wine_id)
