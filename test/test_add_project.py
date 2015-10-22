__author__ = 'Maxim.Rumyantsev'
from model import project

def test_add_project(app):
    #app.session.login("administrator","1111")
    #assert app.session.is_logged_in_as("administrator")
    app.project.create()

