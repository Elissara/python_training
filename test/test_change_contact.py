from model.contact import Contact


def test_change_first_contact(app):
    app.contact.change(Contact(firstname="Ivan", lastname="Ivanoff", nickname="Vanya"))

