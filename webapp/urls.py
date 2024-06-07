from webapp import views
from django.urls import path

urlpatterns=[
    path('',views.homepage,name='home'),
    path('about/',views.aboutpage,name='about'),
    path('contact/',views.contactpage,name='contact'),
    path('product/',views.productpage,name='product'),
    path('saveproduct/',views.saveproduct,name='saveproduct'),
    path('filtered/<cat_name>/',views.filtered,name='filtered'),
    path('singleproduct/<int:pro_name>/', views.singleproduct, name='singleproduct'),
    path('registerpage/', views.registerpage, name='registerpage'),
    path('saveregister/', views.saveregister, name='saveregister'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('logout/', views.logout, name='logout'),
    path('cartsave/', views.cartsave, name='cartsave'),
    path('cartpage/', views.cartpage, name='cartpage')

]