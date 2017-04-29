import os
from datetime import datetime

import FastLSH as lsh

def calCandidate(para_set):


    f = open("./FastLSH/core/logs/" + para_set["run_name"], 'a')

    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Starting Engine\n")
    l = lsh.LSH(para_set["N"], para_set["Q"], para_set["D"], para_set["L"], para_set["K"], para_set["W"], para_set["T"])

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