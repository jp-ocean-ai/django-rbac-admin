"""giraffe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.documentation import include_docs_urls

from giraffe.routers import routee
from giraffe.settings import MEDIA_ROOT
from menus.routers import route
from menutwo.routers import rou
from register.views import RegisterView
from testaddress.routers import rou_testaddress
from testproj.routers import roucc

schema_view = get_schema_view(
    openapi.Info(
        title="人力窝测开项目openapi文档",
        default_version='k1',
        description='人力窝openapi接口文档',
        # 外网访问地址信息
        terms_of_service='http://www.rlw.com/wangyang',
        contact=openapi.Contact(email='wangyang@shun178.com'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    #权限类 任何人都可访问
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("users.urls")),
    path('',include("identy.urls")),
    path('api/',include('rest_framework.urls')),
    path('register/',RegisterView.as_view()),
    path('',include("runproj.urls")),

    re_path(r'docs/',include_docs_urls(title='接口文档')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.with_ui(cache_timeout=0)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
]

urlpatterns += route.urls
urlpatterns += rou.urls
urlpatterns += rou_testaddress.urls
urlpatterns += routee.urls
urlpatterns += roucc.urls
