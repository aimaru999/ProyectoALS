
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
##Handler Comments Form
class CommentsFormHandler(webapp2.RequestHandler):


    #Inserts the hidden fields needed data into the form when recieving a get petition
    def get(self):

        recipe_id=self.request.get("id")
        user = users.get_current_user()

        map={
            "id":recipe_id,
            "user":user.nickname()
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("commentsForm.html",**map))


app = webapp2.WSGIApplication([
    ('/commentsForm', CommentsFormHandler)
], debug=True)