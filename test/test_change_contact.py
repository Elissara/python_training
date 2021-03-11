from model.contact import Contact


def test_change_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Misha"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", lastname="Ivanoff", nickname="Vanya")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact
    old_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

