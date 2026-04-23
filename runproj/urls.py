from django.urls import path

from runproj.views import RunProjView

urlpatterns = [
    path('runproj/', RunProjView.as_view())
]
