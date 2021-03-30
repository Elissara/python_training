from model.contact import Contact
import random


def test_change_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Misha"))
    old_contacts = db.get_contact_list()
    isContact = random.choice(old_contacts)
    contact = Contact(firstname="Ivan", lastname="Ivanoff", nickname="Vanya")
    app.contact.modify_contact_by_id(contact, isContact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)

