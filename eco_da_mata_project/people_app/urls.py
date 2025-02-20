from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllPeoples),
    path('<int:people_id>/', views.getPeople),
    path('<int:people_id>/update/', views.updatePeople),
    path('<int:people_id>/delete/', views.deletePeople),
    path('create/', views.createPeople, name='createPeople'),
    path('create/subcategory', views.createSubcategory),
    path('subcategory/update/<int:subcategory_id>/', views.updateSubcategory),
    path('subcategory/delete/<int:subcategory_id>/', views.deleteSubcategory)
]
