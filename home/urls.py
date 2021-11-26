from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product_details/<int:id>/<slug:slug>', views.product_details, name='product_details'),
    path('category_product/<int:id>/<slug:slug>',views.category_product, name='category_product'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
]
