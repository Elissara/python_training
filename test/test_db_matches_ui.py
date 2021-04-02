from model.group import Group
from model.contact import Contact
import re


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_list = sorted(db.get_contact_list(), key=Contact.id_or_max)
    i = 0
    for item in ui_list:
        assert item.all_phones_from_homepage == merge_phones_like_on_home_page(db_list[i])
        assert item.all_emails_from_homepage == merge_emails_like_on_home_page(db_list[i])
        assert item.address == db_list[i].address
        assert item.lastname == db_list[i].lastname.strip()
        assert item.firstname == db_list[i].firstname.strip()
        i += 1


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.workphone, contact.mobilephone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))