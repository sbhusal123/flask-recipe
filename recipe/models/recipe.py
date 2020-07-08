from orator import Model


class Recipe(Model):
    """
    Defining Model: https://orator-orm.com/docs/0.9/orm.html#defining-a-model
    Model attributes: https://orator-orm.com/docs/0.9/orm.html#defining-fillable-attributes-on-a-model
    """
    __table__ = 'recipes'
    __fillable__ = ['name', 'description']
    __timestamps__ = False