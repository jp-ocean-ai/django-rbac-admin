# from datetime import datetime
import json
import random
import datetime

from django.http import JsonResponse
from faker import Faker
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

from utils.identity import IdNumber


class IdentyView(View):
    def post(self,request):
        f = Faker(locale='zh_CN')
        return JsonResponse(dict(data=f.ssn(),status=201))

class PhoneView(View):
    def post(self,request):
        f = Faker(locale='zh_CN')
        return JsonResponse(dict(data=f.phone_number(), status=201))

class CnameView(View):
    def post(self,request):
        f = Faker(locale='zh_CN')
        return JsonResponse(dict(data=f.name(), status=201))

class EmailView(View):
    def post(self,request):
        f = Faker(locale='zh_CN')
        return JsonResponse(dict(data=f.email(), status=201))

class GenValidIdenty(View):
    def post(self,request):
        json_data = request.body.decode()
        dict_data = json.loads(json_data)
        random_sex = dict_data['sex']
        # random_sex = random.randint(0,1)
        id_no = IdNumber.generate_id(random_sex)
        return JsonResponse(dict(data=id_no,status=201))
