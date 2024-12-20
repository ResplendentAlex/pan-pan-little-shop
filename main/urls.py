from django.urls import path
from main.views import show_main, add_product, add_product_ajax, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, edit_product, delete_product
from main.views import create_product_flutter
    
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add/', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit/<uuid:id>/', edit_product, name='edit_product'),
    path('delete/<uuid:id>/', delete_product, name='delete_product'),
    path('add-product-ajax', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]

