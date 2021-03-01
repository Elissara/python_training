# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Masha"))
    app.contact.modify_first_contact(Contact(firstname="New_firstname"))


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Kotova"))
    app.contact.modify_first_contact(Contact(lastname="New_lastname"))





