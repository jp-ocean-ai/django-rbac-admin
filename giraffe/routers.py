from rest_framework import routers

from upload.views import UploadViewSet

routee = routers.DefaultRouter()

routee.register(prefix=r'upload', viewset=UploadViewSet,basename='upload')