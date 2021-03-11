# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Masha"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New_firstname")
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    old_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname="Kotova"))
#    app.contact.modify_first_contact(Contact(lastname="New_lastname"))
#    old_contacts = app.contact.get_contact_list()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)





