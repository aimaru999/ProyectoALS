
import webapp2
from webapp2_extras import jinja2

from model.recipe import Recipe
from model.comments import Comment
from webapp2_extras.users import users
import time
from resources import login

#Handler of the RecipeView

class RecipeViewHandler(webapp2.RequestHandler):

    #Loads Recipe View and comments when a get petition is recieved
    def get(self):
        login.logging_user(self)
        recetas = Recipe.query()

        recipe_id=self.request.get("id")

        receta_actual =None
        for receta in recetas:
            if str(receta.key.id()) == recipe_id:
                receta_actual=receta

        comentarios = Comment.query(Comment.recipe_id==str(recipe_id))

        template_values = {
            'receta_actual': receta_actual,
            'comentarios': comentarios
        }


        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("recipeView.html",**template_values))


    #Loads Recipe View and comments when a post petition is recieved and inserts comments into DataStore when the data recived is suitable
    def post(self):
        login.logging_user(self)

        recetas = Recipe.query()

        recipe_id=self.request.get("id")

        comments_author=self.request.get("author")

        comments_content=self.request.get("content")

        comments_title=self.request.get("title-commment")

        if comments_author!="" and comments_content!="" and recipe_id!="" and comments_title!="":
            comentario=Comment(author=comments_author,comment=comments_content, recipe_id=recipe_id,title=comments_title)
            comentario.put()
            time.sleep(0.5)

        comentarios = Comment.query(Comment.recipe_id == str(recipe_id))



        receta_actual =None
        for receta in recetas:
            if str(receta.key.id()) == recipe_id:
                receta_actual=receta




        template_values = {
            'receta_actual': receta_actual,
            'comentarios':comentarios
        }




        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("recipeView.html",**template_values))






app = webapp2.WSGIApplication([
    ('/recipeView', RecipeViewHandler)
], debug=True)