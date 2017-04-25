import subprocess
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import time
import os
from django import forms
import core.flExec.lshExecution as lsh

# Create your views here.


def index(request):
    return render(request, 'FastLSH/home.html')


def dbIndex(request):
    return render(request, 'FastLSH/dashboard/index.html')

def para_form(request):
    return render(request, 'FastLSH/dashboard/parameter_form.html')

def my_machine(request):
    return render(request, 'FastLSH/dashboard/my_machine.html')

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
