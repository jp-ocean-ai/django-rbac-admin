
from rest_framework.views import exception_handler

from django.core.exceptions import PermissionDenied
from django.http import Http404

from rest_framework import exceptions, status
from rest_framework.response import Response
from django.db import connections

def set_rollback():
    for db in connections.all():
        if db.settings_dict['ATOMIC_REQUESTS'] and db.in_atomic_block:
            db.set_rollback(True)

def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        # if isinstance(exc.detail, (list, dict)):
        #     data = exc.detail
        # else:
        #     data = {'detail': exc.detail}

        if isinstance(exc.detail, (list, dict)):
            if isinstance(exc.detail,list):
                errors = exc.detail
            else:
                errors = {k: v[0] for k, v in exc.detail.items()}
        else:
            errors = exc.detail

        set_rollback()
        # return Response(data, status=exc.status_code, headers=headers)
        return Response({'code':0,'msg':'失败','errors':errors,'data':[]}, status=exc.status_code, headers=headers)

    return None