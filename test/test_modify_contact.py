# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Masha"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New_firstname")
    app.contact.modify_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    old_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname="Kotova"))
#    app.contact.modify_first_contact(Contact(lastname="New_lastname"))
#    old_contacts = app.contact.get_contact_list()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)





