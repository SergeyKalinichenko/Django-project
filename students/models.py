# models.py
# coding: utf-8

from __future__ import unicode_literals
from django.db import models

class Student(models.Model):

    # Student Model
    first_name = models.CharField(max_length=256, blank=False, verbose_name=u"Имя")

    last_name = models.CharField(max_length=256, blank=False, verbose_name=u"Фамилия")

    middle_name = models.CharField(max_length=256, blank=True, verbose_name=u"Отчество", default='')

    birthday = models.DateField(blank=False, verbose_name=u"Дата народження", null=True)

    photo = models.ImageField(blank=True, verbose_name=u"Фото", null=True)

    ticket = models.CharField(max_length=256, blank=False, verbose_name=u"Білет")

    notes = models.TextField(blank=True, verbose_name=u"Додаткові нотатки")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    class Meta(object):
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенты"

    first_name = models.CharField(max_length=256, blank=False, verbose_name=u"Имя")



