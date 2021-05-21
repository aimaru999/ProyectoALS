#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import webapp2
from google.appengine.ext import ndb
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.recipe import Recipe
from resources import login
import time
##Handler Of the Main Page

class MainHandler(webapp2.RequestHandler):

    #Inserts Recipes into the DataStore when recieved a post petition with proper data and loads the list view
    def post(self):
        login.logging_user(self)

        title_last = self.request.get("rtitle")
        ingr_last = self.request.get("ringredientes")
        prep_last = self.request.get("rpreparacion")

        if title_last != "" and ingr_last != "" and prep_last != "":
            currentUser=users.get_current_user().nickname();
            aux = Recipe(parent=ndb.Key("Recipe",
                                        title_last or "*notitle*"),
                         title=title_last, ingredients=ingr_last, directions=prep_last, author=currentUser)

            aux.put()
            time.sleep(0.5)

        recetas = Recipe.query()

        template_values = {
            'recetas': recetas

        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("index.html", **template_values))

    #Loads The listView when recieved a get petition
    def get(self):
        login.logging_user(self)

        recetas = Recipe.query()

        template_values = {
            'recetas': recetas

        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("index.html", **template_values))



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
