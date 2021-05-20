from google.appengine.ext import ndb

class Comment(ndb.Model):
    author = ndb.TextProperty(required=True)
    comment = ndb.TextProperty(required=True)
    recipe_id=ndb.StringProperty(required=True)
    title=ndb.TextProperty(required=True)