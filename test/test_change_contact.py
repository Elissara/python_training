from model.contact import Contact


def test_change_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Misha"))
    app.contact.change(Contact(firstname="Ivan", lastname="Ivanoff", nickname="Vanya"))


