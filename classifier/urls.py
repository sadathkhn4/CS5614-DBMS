from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('streamlit/', views.streamlit_app),
    path('streamlit2/', views.streamlit_app2),
]