# -*- coding: utf-8 -*-
from model import project

def test_del_first_project(app):
    #app.session.login("administrator","1111")
    #assert app.session.is_logged_in_as("administrator")
    app.project.del_first_project()

