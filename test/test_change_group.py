from model.group import Group
import random


def test_change_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    isGroup = random.choice(old_groups)
    group = Group(name="New_name", header="New_header", footer="New_footer")
    app.group.change_by_id(group, isGroup.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

