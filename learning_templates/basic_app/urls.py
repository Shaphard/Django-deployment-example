from django.urls import path
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    path ('other/',views.other,name='other'),
    path ('relative/',views.relative,name='relative'),
]
