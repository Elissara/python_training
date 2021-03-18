# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="fifstname1", lastname="lastname1", nickname="nickname1"),
    Contact(firstname="fifstname2", lastname="lastname2", nickname="nickname2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


testdata = [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20), nickname=random_string("nickname", 20))
    for name in range(5)
]