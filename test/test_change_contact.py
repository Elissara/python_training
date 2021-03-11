from model.contact import Contact
from random import randrange


def test_change_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Misha"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Ivan", lastname="Ivanoff", nickname="Vanya")
    contact.id = old_contacts[0].id
    app.contact.modify_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    old_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

