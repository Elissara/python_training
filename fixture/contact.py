from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_create_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_create_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.open_home_page()
        self.contact_cache = None

    def change(self):
        self.change_by_index(0)

    def change_by_index(self, contact, index):
        wd = self.app.wd
        self.open_home_page()
        # submit deletion
        wd.find_element_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # self.open_home_page()
        # select first group
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # self.open_home_page()
        # select first group
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        # select first contact
        self.open_home_page()
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, contact, id):
        wd = self.app.wd
        # select first contact
        self.open_home_page()
        # open modification form
        wd.find_element_by_xpath("//a[contains(@href, 'edit.php?id=%s')]/img" % id).click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit modification
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_home_page()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, all_phones_from_homepage=all_phones,
                                                 all_emails_from_homepage=all_emails, address=address))
        return list(self.contact_cache)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, address=address,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       secondaryphone=secondaryphone)

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(contact.id)
        wd.find_element_by_name("to_group").click()
        for is_group in wd.find_elements_by_xpath("//select[@name='to_group']//option"):
            if is_group.get_attribute("value") == group.id:
                is_group.click()
                wd.find_element_by_name("add").click()
        self.open_home_page()
        self.contact_cache = None

    def del_contact_from_group(self, contact, group):
        wd = self.app.wd
        for contact_group in wd.find_elements_by_xpath("//select[@name='group']//option"):
            if contact_group.get_attribute("value") == group.id:
                wd.find_element_by_name("group").click()
                contact_group.click()
                break
        self.select_contact_by_id(contact.id)
        wd.find_element_by_name("remove").click()
        self.open_home_page()
        self.contact_cache = None


