import json
from api.database import db
from sqlalchemy import Column, String, Integer

"""
Drink
a persistent drink entity, extends the base SQLAlchemy Model
"""


class Drink(db.Model):
    __tablename__ = "drinks"
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    title = Column(String(80), nullable=False, unique=True)
    recipe = db.relationship("Recipe", backref="drink")

    """
    short()
        short form representation of the Drink model
    """

    def short(self):
        return {"id": self.id, "title": self.title}

    '''
    long()
        long form representation of the Drink model
    '''
    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'recipe': json.loads(self.recipe)
        }

    """
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.insert()
    """

    def insert(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    """
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.delete()
    """

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    """
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink.query.filter(Drink.id == id).one_or_none()
            drink.title = 'Black Coffee'
            drink.update()
    """

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())
