import ctypes

import FastLSH as lsh

def calCandidate(para_set):

    l = lsh.LSH(para_set["N"], para_set["Q"], para_set["D"], para_set["L"], para_set["K"], para_set["W"], para_set["T"])

    #
    l.loadSetN(str(para_set["input_path_N"]),0)
    l.loadSetQ(str(para_set["input_path_Q"]),0)
    #
    l.setThreadMode(1)
    l.setComputeMode(1)

    print l.reportStatus()

    result = l.getCandidateSet()

    return result