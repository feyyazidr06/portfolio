from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notes", views.notes, name="notes"),
    path("note/<int:id>/delete", views.deletenote, name="deletenote"),
    path("note/<int:id>/edit", views.editnote, name="editnote"),
    path("note/<int:id>", views.note, name="note"),
    path("note/add", views.addnote, name="addnote"),
    path("list", views.liste, name="list"),
    path("search", views.search, name="search"),
    path("add", views.add, name="add"),
    path("<int:id>", views.customer, name="customer"),
    path("<int:id>/delete", views.delete, name="delete"),
    path("<int:id>/finished", views.finished, name="finished"),
    path("company", views.company, name="company"),
    path("doc", views.doc, name="doc"),
    path("warranty/<int:id>", views.warranty, name="warranty"),
]