from django.http import JsonResponse
from django.views import View

import os
# Create your views here.


class RunProjView(View):
    def get(self,request):
        cur_dir = os.getcwd()
        os.chdir(r'/Users/jupiter/uinew/yml_check/')
        run_dir = os.getcwd()
        print(f"当前目录：{cur_dir}\n运行目录：{run_dir}")
        # os.system('python run_main_flow.py')
        os.system('python run_mail.py')
        return JsonResponse(dict(data="success"), status=201)

    def post(self, request):
        # 进入到运行目录 /Users/jupiter/uinew/yml_check/run_main_flow.py
        # 运行run_main_flow.py
        cur_dir = os.getcwd()
        os.chdir(r'/Users/jupiter/uinew/yml_check/')
        run_dir = os.getcwd()
        print(f"当前目录：{cur_dir}\n运行目录：{run_dir}")
        os.system('python run_main_flow.py')
        return JsonResponse(dict(data="success"), status=201)