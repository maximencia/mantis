

def test_login_web(app):
    #app.session.login("administrator","1111")
    p=1
    assert app.session.is_logged_in_as("administrator")
