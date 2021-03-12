from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, id=None, address=None,
                 homephone=None, mobilephone=None, workphone=None,  secondaryphone=None, all_phones_from_homepage=None,
                 email=None, email2=None, email3=None, all_emails_from_homepage=None):

        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_homepage = all_emails_from_homepage
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
