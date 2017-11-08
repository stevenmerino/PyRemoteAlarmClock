#! /usr/bin/python3.6

import serverclientsocket as scs
import json
import jsonalarms as ja
import jsonalarmsutils as jau


if __name__ == "__main__":
    s = scs.ServerSocket()

    try:
        a = ja.Alarms("alarms.json").load()      # Permission error on RasPi need to use direct path '/home/pi/alarm.json'
    except:
        a = ja.Alarms("alarms.json")             # Permission error on RasPi need to use direct path '/home/pi/alarm.json'
        print("Created new Alarms file.")
    else:
        print("Alarms loaded from file.")

    while True:
        jau.check_alarms(a)
        a.save()
        if s.msg is not None:
            try:
                alarms = json.loads(s.msg)
            except json.decoder.JSONDecodeError:
                pass
            else:
                print("Got JSON:", s.msg)
                a.save_new(alarms)
                a.load()
                s.msg = None

            if s.msg == "stop":
                jau.stop_trigger()
                s.msg = None
            elif s.msg == "quit":
                break
            else:
                s.msg = None

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
