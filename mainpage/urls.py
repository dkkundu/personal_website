from django.urls import path
from mainpage.views import ProjectListAndFormView

urlpatterns = [
    path('', ProjectListAndFormView.as_view(), name='main')
]
