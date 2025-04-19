from django.urls import re_path, path
from . import views

urlpatterns = [
    #url(r'^$', views.import_sheet, name="import_sheet"),
    path('', views.homepage, name='homepage'),
    re_path('questions/'+r'(?P<question_id>[0-9]+)/$', views.question, name='question'),
    path('questions/error.html', views.error, name='error'),
    path('questions/index.html', views.homepage, name='homepage'),
    re_path('questions/'+r'(?P<question_id>[0-9]+)/(?P<answer>yes|no)/result.html$', views.result, name='result'),
    path('questions/promo.html', views.promo, name='promo'),
]
