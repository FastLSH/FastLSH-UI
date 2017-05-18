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


import os
from datetime import datetime

import FastLSH as lsh

def calCandidate(para_set):


    f = open("./FastLSH/core/logs/" + para_set["run_name"]+".log", 'a')

    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Starting Engine\n")
    l = lsh.LSH(para_set["N"], para_set["Q"], para_set["D"], para_set["L"], para_set["K"], para_set["W"], para_set["T"])

    print para_set["run_name"]
    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Loading data set N from "+para_set["input_path_N"]+ "\n")
    l.loadSetN(str(para_set["input_path_N"]),0)
    f.write(
        datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Loading data set Q from " + para_set["input_path_Q"] + "\n")
    l.loadSetQ(str(para_set["input_path_Q"]),0)


    l.setThreadMode(int(para_set["thread_mode"].split("-")[0]))
    l.setComputeMode(int(para_set["compute_mode"].split("-")[0]))

    # f.write(
    #     datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Engine Status" + l.reportStatus() + "\n")

    f.write(
        datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Starting Engine \n")
    result = l.getCandidateSet()

    f.write(
        datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Calculation  Complete \n")

    l.saveCandidateSet(para_set["output_path"])

    f.write(
        datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Saving Candidate Set to " + para_set["output_path"] + "\n")

    f.close()

    l.clear()

    l.__swig_destroy__


    return result