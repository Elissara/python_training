from model.group import Group


def test_change_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.change(Group(name="New_name", header="New_header", footer="New_footer"))
