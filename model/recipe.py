from google.appengine.ext import ndb

class Recipe(ndb.Model):
    title=ndb.TextProperty(required=True)
    ingredients = ndb.TextProperty(required=True)
    directions = ndb.TextProperty(required=True)
    author=ndb.TextProperty(required=True)