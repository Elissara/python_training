from model.group import Group
from model.contact import Contact
import random
import time


def test_contact_in_group(app, ormdb):
    if len(ormdb.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="Test_firstname", lastname="Test_lastname"))
    if len(ormdb.get_group_list()) == 0:
        app.group.create(
            Group(name="Test_name"))
    contact = random.choice(ormdb.get_contact_list())
    group = random.choice(ormdb.get_group_list())
    time.sleep(1)
    app.contact.add_contact_to_group(contact, group)
    time.sleep(1)
    assert group in ormdb.get_groups_for_contact(contact)


def test_contact_out_group(app, ormdb):
    if len(ormdb.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="Test_firstname", lastname="Test_lastname"))
    if len(ormdb.get_group_list()) == 0:
        app.group.create(
            Group(name="Test_name"))
    contact = random.choice(ormdb.get_contact_list())
    list_groups_for_contact = ormdb.get_groups_for_contact(contact)
    if (len(list_groups_for_contact)) == 0:
        group = random.choice(ormdb.get_group_list())
        app.contact.add_contact_to_group(contact, group)
    else:
        index = random.randrange(len(list_groups_for_contact))
        group = list_groups_for_contact[index]
        app.contact.del_contact_from_group(contact, group)
    assert group not in ormdb.get_groups_for_contact(contact)
