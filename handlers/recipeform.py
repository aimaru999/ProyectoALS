
import webapp2
from webapp2_extras import jinja2



class RecipeFormHandler(webapp2.RequestHandler):

    def post(self):


        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("recipeForm.html"))



    def get(self):


        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("recipeForm.html"))

app = webapp2.WSGIApplication([
    ('/recipeForm', RecipeFormHandler)
], debug=True)