import subprocess
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import time
import os
from django import forms
import core.flExec.lshExecution as lsh
import psutil
import platform
from requests import get

# Create your views here.


def index(request):
    return render(request, 'FastLSH/home.html')


def dbIndex(request):
    return render(request, 'FastLSH/dashboard/index.html')

def para_form(request):
    return render(request, 'FastLSH/dashboard/parameter_form.html')

def my_machine(request):
    mach_info = dict()

    mach_info["p_count_l"] = psutil.cpu_count()
    mach_info["p_count"] = psutil.cpu_count(logical=False)
    mach_info["m_size"] = "%.2f" % (psutil.virtual_memory().total/(1024.0**3))
    mach_info["disk_free"] = "%.2f" %(psutil.disk_usage('/').free/(1024.0**3))
    mach_info["os"] = platform.linux_distribution()[0] + " " + platform.linux_distribution()[1]
    mach_info["p_type"] = platform.processor()
    mach_info["ex_ip"] = get('https://ipapi.co/ip/').text


    return render(request, 'FastLSH/dashboard/my_machine.html', mach_info)

def instruction(request):
    return render(request, 'FastLSH/dashboard/instruction.html')

def ab_prj(request):
    return render(request, 'FastLSH/dashboard/about_project.html')

def ab_tm(request):
    return render(request, 'FastLSH/dashboard/about_team.html')

def ab_sc(request):
    return render(request, 'FastLSH/dashboard/about_source_code.html')

def dp_high_dim_viz(request):
    return render(request, 'FastLSH/dashboard/dp_high_dim_viz.html')

def parameterSet(request):
    return render(request, 'FastLSH/parameterSet.html')

def execution(request):
    return render(request, 'FastLSH/execution.html')

def contact(request):
    return render(request, 'FastLSH/basic.html' , {'content': ['if you would','fsdaf']})



def submit(request):

    dir_path = os.path.dirname(os.path.realpath(__file__))

    time_stamp = time.strftime("%Y%m%d%H%M%S")

    para_set = dict()

    para_set["run_name"] = "first run" if request.POST["RunName"]=="" else request.POST["RunName"]
    para_set["N"] =  1000 if request.POST["phN"]=="" else int(request.POST["phN"])
    para_set["Q"] =  1000 if request.POST["phQ"]=="" else int(request.POST["phQ"])
    para_set["D"] =  56 if request.POST["phD"]=="" else int(request.POST["phD"])
    para_set["L"] =  200 if request.POST["phL"]=="" else int(request.POST["phL"])
    para_set["K"] =  1 if request.POST["phK"]=="" else int(request.POST["phK"])
    para_set["W"]=  1.2 if request.POST["phW"]=="" else float(request.POST["phW"])
    para_set["T"] =  100 if request.POST["phT"]=="" else int(request.POST["phT"])
    para_set["compute_mode"] = request.POST["computeMode"]
    para_set["thread_mode"] = request.POST["threadMode"]
    para_set["input_path_N"] = "./dataset1000NoIndex.csv" if request.POST["ipathN"]=="" else request.POST["ipathN"]
    para_set["input_path_Q"] = "./dataset1000NoIndex.csv" if request.POST["ipathQ"]=="" else request.POST["ipathQ"]
    para_set["output_path"] = "candidate.csv" if request.POST["opath"]=="" else request.POST["opath"]

    reply = lsh.calCandidate(para_set)

    #
    # s = subprocess.check_output(["./FastLSH/core/cExec/FastLSH"])
    # s = s.replace("\n","<br>")
    return render(request, 'FastLSH/execution.html', {'content': reply})
#    return HttpResponse(s)
#    return HttpResponse('Hello World!')


def download(request):
    f = open('/home/peter/FYP/SimPointSite/FastLSH/cExec/output/candidate.csv', 'r')
    response = HttpResponse(f, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="candidate.csv"'
    f.close()
    return response

# def hello(request):
#     return HttpResponse('Hello World!')
#
# def home(request):
#     return render_to_response('index.html', {'variable': 'world'})
