# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New_firstname"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="New_lastname"))





