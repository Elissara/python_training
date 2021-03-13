# -*- coding: utf-8 -*-
from model.contact import Contact
import time
import pytest
import random
import string



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


testdata = [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20), nickname=random_string("nickname", 20))
    for name in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    time.sleep(3)
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    old_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
