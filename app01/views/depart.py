from django.shortcuts import render, redirect
from app01 import models

from app01.utils.pagination import Pagination
from app01.utils.form import UserModelForm, PrettyModelForm, PrettyEditModelForm


def depart_list(request):



    queryset = models.Department.objects.all()

    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):

    if request.method == "GET":
        return render(request, 'depart_add.html')


    title = request.POST.get("title")

    models.Department.objects.create(title=title)


    return redirect("/depart/list/")


def depart_delete(request):

    # get ID http://127.0.0.1:8000/depart/delete/?nid=1
    nid = request.GET.get('nid')


    models.Department.objects.filter(id=nid).delete()

    return redirect("/depart/list/")


def depart_edit(request, nid):
    """ updatedepart """
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {"row_object": row_object})


    title = request.POST.get("title")


    models.Department.objects.filter(id=nid).update(title=title)


    return redirect("/depart/list/")

