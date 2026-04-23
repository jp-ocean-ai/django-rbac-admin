from django.urls import path

from identy.views import IdentyView, PhoneView, GenValidIdenty, CnameView, EmailView

urlpatterns = [
    path('identy/',IdentyView.as_view()),
    path('phone/',PhoneView.as_view()),
    path('valididenty/',GenValidIdenty.as_view()),
    path('cname/',CnameView.as_view()),
    path('email/',EmailView.as_view()),
]