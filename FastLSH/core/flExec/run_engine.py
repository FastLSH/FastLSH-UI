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


import sys
from datetime import datetime
import FastLSH as lsh
import os.path


f = open( "./FastLSH/core/logs/" + sys.argv[1]+".log", 'a', 0)

f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Starting Engine\n")

l = lsh.LSH(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]),
                                    int(sys.argv[6]), float(sys.argv[7]), int(sys.argv[8]))

print sys.argv[1]
if os.path.exists(str(sys.argv[11])):
    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Loading data set N from "+sys.argv[11]+ "\n")
    l.loadSetN(str(sys.argv[11]),0)
else:
    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Data Set N file not exist in  " + sys.argv[11] + "\n")
    sys.exit(0)

if os.path.exists(str(sys.argv[12])):
    f.write(
        datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Loading data set Q from " + sys.argv[12] + "\n")
    l.loadSetQ(str(sys.argv[12]),0)
else:
    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Data Set Q file not exist in  " + sys.argv[12] + "\n")
    sys.exit(0)

l.setThreadMode(int(sys.argv[10].split("-")[0]))
f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Set Thread Mode to " + sys.argv[10] + "\n")


l.setComputeMode(int(sys.argv[9].split("-")[0]))
f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Set Compute Mode to  " + sys.argv[9] + "\n")


f.write(
    datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Starting Engine \n")
result = l.getCandidateSet()

f.write(
    datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Calculation  Complete \n")

l.saveCandidateSet(sys.argv[13])

f.write(
    datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  Saving Candidate Set to " + sys.argv[13] + "\n")

f.close()

l.clear()

l.__swig_destroy__




