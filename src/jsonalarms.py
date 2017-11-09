#! /usr/local/bin/python3.6

import json
import datetime
import typefield    # Needs Python 3.6 to work.

# Alarm class that requires respective data types and serialize to list.
class Alarm:
    name = typefield.Type(str)
    msg = typefield.Type(str)
    time = typefield.Type(list)
    repeat = typefield.Type(list)

    def __init__(self, id_int, name, msg, time, repeat):
        self.id = id_int            # An int identifier
        self.name = name            # String to identify alarm
        self.msg = msg              # String to display when alarm goes off
        self.time = time            # Tuple representing time of day the alarm goes off
        self.repeat = repeat        # List of datetime.date.weekday() ints that the alarm should repeat
        self.thread = None          # The thread that is responsible for running this Alarm

    def to_list(self):
        return [self.id, {"name": self.name, "msg": self.msg, "time": self.time, "repeat": self.repeat, "thread": str(self.thread)}]

# Alarms class keeps a dictionary of Alarm instances that can be saved or loaded with json
# Alarms Class is also responsible for creating the Alarm instance
class Alarms:
    def __init__(self, filepath):
        self.filepath = filepath
        self.alarms = {}
        self.alarms['Alarms'] = []

    def create(self, name, msg, time, repeat):
        self.alarms['Alarms'].append(Alarm( len(self.alarms['Alarms']), name = name, msg = msg, time = time, repeat = repeat))

    def save(self):
        json_alarms = {}
        json_alarms['Alarms'] = []
        for alarm in self.alarms['Alarms']:
            json_alarms['Alarms'].append(alarm.to_list())
        with open(self.filepath, 'w') as outfile:       # Permission error on RasPi need to use direct path '/home/pi/alarm.json'
            json.dump(json_alarms, outfile, indent = 5)

    def save_new(self, injson):
        json_alarms = {}
        json_alarms['Alarms'] = []
        for alarm in injson['Alarms']:
            json_alarms['Alarms'].append(alarm)
        with open(self.filepath, 'w') as outfile:        # Permission error on RasPi need to use direct path '/home/pi/alarm.json'
            json.dump(json_alarms, outfile, indent = 5)

    def load(self):
        with open(self.filepath) as infile:         # TODO: If no file exists, create one
            self.alarms = {}
            self.alarms['Alarms'] = []
            for alarm in json.load(infile)['Alarms']:
                self.create(alarm[1]['name'], alarm[1]['msg'], alarm[1]['time'], alarm[1]['repeat'])
        return self

    def to_json(self):
        json_alarms = {}
        json_alarms['Alarms'] = []
        for alarm in self.alarms['Alarms']:
            json_alarms['Alarms'].append(alarm.to_list())
        return json.dumps(json_alarms)

# Funtion that returns the string weekday from the int datetime.date.weekday()
def weekday_to_string(weekday_int):
    return {
        0: "Monday",
        1: "Tuesday",
        2: "Wednsday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }.get(weekday_int, default = "Error")    # Error if weekday_int not found

if __name__ == "__main__":
    pass
    #alarms = Alarms("alarms.json")
    # alarms.load("alarms.json")
    # print(type(alarms.alarms['Alarms']))
    # print(len(alarms.alarms['Alarms']))
    # print(alarms.alarms)
    #alarms.create(name = "Alarm 1", msg = "Wake up!", time = [17,10], repeat = [0,1,2,3,4,5,6])
    #alarms.create(name = "Alarm 2", msg = "Wake up!", time = [17,10], repeat = [0,1,2,3,4,5,6])
    # print(type(alarms.alarms['Alarms']))
    # print(len(alarms.alarms['Alarms']))
    # print(alarms.alarms)
    #alarms.save()


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
