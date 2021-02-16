from model.group import Group


def test_change_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.change(Group(name="New_name", header="New_header", footer="New_footer"))
    app.session.logout()

