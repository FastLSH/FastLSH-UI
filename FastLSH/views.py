import subprocess

from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import time
import os
import core.flExec.lshExecution as lsh
import psutil
import platform
from requests import get
from multiprocessing import Pool
from threading import Thread

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

def db_submit(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    time_stamp = time.strftime("%Y%m%d%H%M%S")

    print dir_path
    para_set = dict()

    para_set["run_name"] = "first run" if request.POST["RunName"] == "" else request.POST["RunName"]

    f = open(dir_path+"/core/logs/" + para_set["run_name"], 'wb')
    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Parameter Received\n")

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

    t = Thread(target=lsh.calCandidate, args=(para_set,))
    t.start()


    # reply = lsh.calCandidate(para_set)
    return HttpResponse("wqer")
    #return render(request, 'FastLSH/dashboard/execution.html', {} )

def get_log(request):
    run_name = "first run" if request.POST["RunName"] == "" else request.POST["RunName"]
    with open("./FastLSH/core/logs/"+run_name) as f:
        response = f.read()

    return HttpResponse(response)

def run_model(request):

    cpu_num = psutil.cpu_count()

    cpu_html = ""
    for c in range(1,cpu_num+1):
        cpu_html = cpu_html+'<div class="widget_summary"><div class="w_left w_25"><span>CPU '+str(c)+'</span></div>' \
        '<div class="w_center w_55"><div class="progress"><div class="progress-bar bg-green" role="progressbar" ' \
        'id = "cpu_'+str(c)+'" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 80%;"><span class="sr-only"></span>' \
        '</div></div></div><div class="w_right w_20"><span id = "cpu_'+str(c)+'_p"></span></div><div class="clearfix"></div></div>'

    return render(request, 'FastLSH/dashboard/run_model.html', {'cpu_html':cpu_html})


def execution_d(request):
    # reply = lsh.calCandidate(para_set)
    return render(request, 'FastLSH/dashboard/execution.html')

def ram_status(request):
    #psutil.cpu_percent(percpu=True)
    response = psutil.virtual_memory().percent

    return HttpResponse(response)

def cpu_status(request):
    percent = psutil.cpu_percent(percpu=True)
    response = ""
    response = response + str(psutil.cpu_count()) + " "
    for p in percent:
        response =  response +str(p) +" "
    return HttpResponse(response)


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

    f = open ("./FastLSH/core/logs/"+para_set["run_name"],'wb')
    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"  Parameter Received\n")

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

    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Passing Parameter to the Engine\n ")
    f.close()

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
