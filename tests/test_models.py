#!/usr/bin/env python
#coding:utf-8

import sys
sys.path.append('../sixcms')
from sixcms import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


def test_create():
    p = Person()
    p.first_name = "Donald"
    assert p.first_name == "Donald"


def test_create_and_get():
    Person.objects.create(first_name="Donald", last_name="Duck")
    p = Person.objects.get(last_name="Duck")
    assert p.first_name == "Donald"
