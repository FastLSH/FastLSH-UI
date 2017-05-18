#   Copyright 2017 Peter XU Yaohai
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

from datetime import datetime
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import os
import psutil
import platform
from requests import get
import csv
from subprocess import Popen

def index(request):
    return render(request, 'FastLSH/dashboard/home/index.html')


def instruction(request):
    return render(request, 'FastLSH/dashboard/home/instruction.html')


def my_machine(request):
    mach_info = dict()
    mach_info["p_count_l"] = psutil.cpu_count()
    mach_info["p_count"] = psutil.cpu_count(logical=False)
    mach_info["m_size"] = "%.2f" % (psutil.virtual_memory().total/(1024.0**3))
    mach_info["disk_free"] = "%.2f" %(psutil.disk_usage('/').free/(1024.0**3))
    mach_info["os"] = platform.linux_distribution()[0] + " " + platform.linux_distribution()[1]
    mach_info["p_type"] = platform.processor()
    mach_info["ex_ip"] = get('https://ipapi.co/ip/').text
    return render(request, 'FastLSH/dashboard/home/my_machine.html', mach_info)


def run_model(request):

    cpu_num = psutil.cpu_count()

    cpu_html = ""
    for c in range(1,cpu_num+1):
        cpu_html = cpu_html+'<div class="widget_summary"><div class="w_left w_25"><span>CPU '+str(c)+'</span></div>' \
        '<div class="w_center w_55"><div class="progress"><div class="progress-bar bg-green" role="progressbar" ' \
        'id = "cpu_'+str(c)+'" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 80%;"><span class="sr-only"></span>' \
        '</div></div></div><div class="w_right w_20"><span id = "cpu_'+str(c)+'_p"></span></div><div class="clearfix"></div></div>'

    return render(request, 'FastLSH/dashboard/run_the_engine/run_model.html', {'cpu_html':cpu_html})


def db_submit(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    print dir_path
    para_set = dict()

    para_set["run_name"] = "first run" if request.POST["RunName"] == "" else request.POST["RunName"]

    # create log file
    f = open(dir_path + "/core/logs/" + para_set["run_name"] + ".log", 'wb')
    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Parameter Received\n")

    # get parameters from form
    para_set["N"] = 1000 if request.POST["phN"] == "" else int(request.POST["phN"])
    para_set["Q"] = 1000 if request.POST["phQ"] == "" else int(request.POST["phQ"])
    para_set["D"] = 56 if request.POST["phD"] == "" else int(request.POST["phD"])
    para_set["L"] = 200 if request.POST["phL"] == "" else int(request.POST["phL"])
    para_set["K"] = 1 if request.POST["phK"] == "" else int(request.POST["phK"])
    para_set["W"] = 1.2 if request.POST["phW"] == "" else float(request.POST["phW"])
    para_set["T"] = 100 if request.POST["phT"] == "" else int(request.POST["phT"])
    para_set["compute_mode"] = request.POST["computeMode"]
    para_set["thread_mode"] = request.POST["threadMode"]
    para_set["input_path_N"] = "./dataset1000NoIndex.csv" if request.POST["ipathN"] == "" else request.POST["ipathN"]
    para_set["input_path_Q"] = "./dataset1000NoIndex.csv" if request.POST["ipathQ"] == "" else request.POST["ipathQ"]
    para_set["output_path"] = "candidate.csv" if request.POST["opath"] == "" else request.POST["opath"]

    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Passing Parameter to the Engine\n")
    f.close()

    p = Popen(["python", dir_path + "/core/flExec/run_engine.py", str(para_set["run_name"]), str(para_set["N"]),
               str(para_set["Q"]), str(para_set["D"]), str(para_set["L"]), str(para_set["K"]), str(para_set["W"]),
               str(para_set["T"]),
               str(para_set["compute_mode"]), str(para_set["thread_mode"]), str(para_set["input_path_N"]),
               str(para_set["input_path_Q"]), str(para_set["output_path"])])

    return HttpResponse("Success")

def get_log(request):
    run_name = "first run" if request.GET["RunName"] == "" else request.GET["RunName"]
    with open("./FastLSH/core/logs/"+run_name + ".log") as f:
        response = f.read()
    return HttpResponse(response)


def ram_status(request):
    response = psutil.virtual_memory().percent
    return HttpResponse(response)


def cpu_status(request):
    percent = psutil.cpu_percent(percpu=True)
    response = ""
    response = response + str(psutil.cpu_count()) + " "
    for p in percent:
        response = response +str(p) +" "
    return HttpResponse(response)


def dp_high_dim_viz(request):
    return render(request, 'FastLSH/dashboard/data_presentation/dp_high_dim_viz.html')


def get_data_series(request):
    data_type = request.GET.get('data_type', '')

    data = []

    if data_type =="iris":
        with open('./FastLSH/vis_data/Iris.csv', 'rb') as f:
            reader = csv.reader(f)
            data = list(reader)

    if data_type == "glass":
        with open('./FastLSH/vis_data/glass.csv', 'rb') as f:
            reader = csv.reader(f)
            data = list(reader)

    if data_type == "cancer":
        with open('./FastLSH/vis_data/breast_cancer.csv', 'rb') as f:
            reader = csv.reader(f)
            data = list(reader)

    if data_type == "author":
        with open('./FastLSH/vis_data/author.csv', 'rb') as f:
            reader = csv.reader(f)
            data = list(reader)

    response = process_data(data)

    return JsonResponse(response)


def process_data(ori_data):
    feature_names = ori_data[0][2:]
    feature_num = len(feature_names)

    ori_data = ori_data[1:]

    data = []
    class_set = []

    for i in ori_data:
        res = [None] * len(i)
        res[0] = i[0] + "-" + i[1]
        if i[1] not in class_set:
            class_set.append(i[1])
        res[1] = class_set.index(i[1])
        res[2:] = i[2:]
        data.append(res)

    response = {}

    response["f_names"] = feature_names
    response["f_num"] = feature_num
    response["data"] = data

    return response


def ab_prj(request):
    return render(request, 'FastLSH/dashboard/about/about_project.html')


def ab_tm(request):
    return render(request, 'FastLSH/dashboard/about/about_team.html')


def ab_sc(request):
    return render(request, 'FastLSH/dashboard/about/about_source_code.html')
