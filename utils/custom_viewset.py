from rest_framework import viewsets
from rest_framework.response import Response


class ReturnMsg:
    def __init__(self,msg='成功',errors=None,data=None,status=200):
        self.status = status
        self.msg = msg
        self.errors = {} if errors is None else errors
        self.data = [] if data is None else data

    def dict(self):
        return {
            'data': self.data,
            'meta': {
                'msg': self.msg,
                'errors': self.errors,
                'status': self.status
            }
        }


class CustomModelViewSet(viewsets.ModelViewSet):
    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save() # 逻辑删除

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data,status=response.status_code).dict(),status=response.status_code)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data,status=response.status_code).dict(),status=response.status_code)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data,status=response.status_code).dict(),status=response.status_code)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data,status=response.status_code).dict(),status=response.status_code)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data,status=response.status_code).dict(),status=response.status_code)

