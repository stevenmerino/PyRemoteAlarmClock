#! /usr/local/bin/python3.6

import serverclientsocket as scs
import jsonalarms as ja
import sys

if __name__ == "__main__":
    c = scs.ClientSocket()
    alarms = ja.Alarms("alarms.json")
    alarms.create(name = "Alarm 1", msg = "Wake up!", time = [9,0], repeat = [0,1,2,3,4,5,6])
    alarms.save()

    if sys.argv[-1] == "send":
        c.send(alarms.to_json())
    else:
        c.send(sys.argv[-1])

# Copyright 2017 Steven Merino
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
