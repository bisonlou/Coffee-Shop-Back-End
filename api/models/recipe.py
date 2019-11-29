import json
from api.database import db
from sqlalchemy import Column, String, Integer


"""
recipe
a persistent drink recipe entity, extends the base SQLAlchemy Model
"""


class Recipe(db.Model):
    __tablename__ = "recipes"
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    name = Column(String(80), nullable=False)
    color = Column(String(80), nullable=False)
    parts = Column(String(180), nullable=False)
    drink_id = Column(Integer, db.ForeignKey("drinks.id"), nullable=False)

    """
    short()
        short form representation of the Drink model
    """

    def short(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "parts": self.parts,
            "drink": self.drink_id,
        }

    def __repr__(self):
        return json.dumps(self.short())
