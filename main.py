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
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates%s' % '/form')
        self.response.write(template.render({'title': 'CONTACT'}))

    def post(self):
        user = self.request.get('username')
        pw = self.request.get('password')
        if pw == 'pass' and user == 'Colleen':
            template = JINJA_ENVIRONMENT.get_template('templates%s' % '/contact')
            self.response.write(template.render({'title': 'CONTACT'}))
        else:
            logging.info('Invalid credentials: user='+user+' pw='+pw)
            template = JINJA_ENVIRONMENT.get_template('templates%s' % '/form')
            self.response.write(template.render({'title': 'CONTACT'}))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        try:
            path = self.request.path
            template = JINJA_ENVIRONMENT.get_template('templates%s' % path)
            if path == "/index":
                self.response.write(template.render({'title': 'HOME'}))
            elif path == "/about":
                self.response.write(template.render({'title': 'ABOUT'}))
            elif path == "/artwork":
                self.response.write(template.render({'title': 'ARTWORK'}))
            elif path == "/experience":
                self.response.write(template.render({'title': 'EXPERIENCE'}))
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index')
            self.response.write(template.render({'title': 'HOME'}))


app = webapp2.WSGIApplication([
    ('/form', ContactHandler),
    ('/contact', ContactHandler),
    ('/.*', MainHandler)
    ], debug=True)

