# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse


# Views for Students

def students_list(request):
    students = (
        {'id': 1,
            'first_name': u'Виталий',
            'last_name': u'Подоба',
            'ticket': 235,
            'image': 'img/2.GIF'},
        {'id': 2,
            'first_name': u'Короста',
            'last_name': u'Андрей',
            'ticket': 2123,
            'image': 'img/1.jpg'},
        {'id': 3,
            'first_name': u'Андрий',
            'last_name': u'Притула',
            'ticket': 5332,
            'image': 'img/3.jpg'}
            )
    return render(request, 'students_list.html', {'students': students}) # В качестве значения передали переменную картежа с элементами словаря

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Students %s</h1>' % sid)

# Views for Groups

def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s<h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
