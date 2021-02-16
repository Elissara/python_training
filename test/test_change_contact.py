from model.contact import Contact


def test_change_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.change(Contact(firstname="Ivan", lastname="Ivanoff", nickname="Vanya"))
    app.session.logout()
