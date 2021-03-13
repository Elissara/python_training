# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Group_group")
    group.id = old_groups[0].id
    app.group.modify_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    old_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="test"))
#    app.group.modify_first_group(Group(header="Header_header"))
#    old_groups = app.group.get_group_list()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
