from django.urls import path
from backend import views


urlpatterns=[
    path('categorypage/',views.categorypage,name='categorypage'),
    path('savecategory/', views.savecategory, name='savecategory'),
    path('displaycategory/', views.displaycategory, name='displaycategory'),
    path('editcategory/<int:cid>/', views.editcategory, name='editcategory'),
    path('updatecategory/<int:cid>/', views.updatecategory, name='updatecategory'),
    path('deletecategory/<int:cid>/', views.deletecategory, name='deletecategory'),

    path('indexdata/',views.indexdata,name='indexdata'),
    path('adddata/', views.adddata, name='adddata'),
    path('savedata/',views.savedata,name='savedata'),
    path('displaydata/', views.displaydata, name='displaydata'),
    path('editdata/<int:eleid>/', views.editdata, name='editdata'),
    path('updatedata/<int:eleid>/', views.updatedata, name='updatedata'),
    path('deletedata/<int:eleid>/', views.deletedata, name='deletedata'),



    path('loginpage/', views.loginpage, name='loginpage'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('logout/', views.logout, name='logout'),



    path('displaycontact/',views.displaycontact,name='displaycontact'),
    path('deletecontact/<int:proid>/', views.deletecontact, name='deletecontact')

]