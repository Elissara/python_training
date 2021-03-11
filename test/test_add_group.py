# -*- coding: utf-8 -*-
from model.group import Group
import time


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="12345", header="123456", footer="1234567")
    app.group.create(group)
    time.sleep(3)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

