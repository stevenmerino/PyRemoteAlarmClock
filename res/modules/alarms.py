#! /usr/local/bin/python3.6

import res.modules.typefield as typefield    # Needs Python 3.6 to work.
import pygame
import json
import threading
import datetime
import os

pygame.mixer.init()

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

    def save(self, json_alarms):
        alarms_object = {}
        alarms_object['Alarms'] = []
        for alarm in json_alarms['Alarms']:
            alarms_object['Alarms'].append(alarm)
        try:
            with open(self.filepath, 'w') as outfile:
                json.dump(alarms_object, outfile, indent = 5)
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
        else:
            print("Saved:", alarms_object)

    def load(self):
        try:
            with open(self.filepath) as infile:         # TODO: If no file exists, create one
                self.alarms = {}
                self.alarms['Alarms'] = []
                for alarm in json.load(infile)['Alarms']:
                    self.create(alarm[1]['name'], alarm[1]['msg'], alarm[1]['time'], alarm[1]['repeat'])
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
        else:
            print("Loaded:", self.to_json())
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

# Checks each Alarm in the list of Alarms if 1. today is in the Alarm's list of weekdays 2. the alarm is in the future and 3. if a thread for the alarm has already been created.
# If an alarm is today, in the future, and has no thread, one is created.
def check_alarms(alarms_object):
    for alarm in alarms_object.alarms['Alarms']:
        if check_alarm_weekday(alarm):
            if check_alarm_time(alarm):
                if alarm.thread == None:
                    create_thread(alarm)

# Checks a single Alarm to see if today's weekday is in the list of weekdays (Alarm.repeat)
def check_alarm_weekday(alarm):
    for weekday in alarm.repeat:
        if weekday is datetime.datetime.now().weekday():
            return True
    return False

# Check if an Alarm's time is before the current time. return true if Alarm's time is in the future otherwise false
def check_alarm_time(alarm):
    current_time = datetime.datetime.now().time().replace(second = 0, microsecond = 0)
    alarm_time = datetime.time(hour = alarm.time[0], minute = alarm.time[1])
    if alarm_time > current_time:
        return True
    else:
        return False

# Creates a thread that runs alarm_thread func for the given Alarm and stores that thread in the Alarm
def create_thread(alarm):
    t = threading.Thread(target = alarm_thread, args = (alarm,))
    t.daemon = True
    t.start()
    alarm.thread = t

# Checks an Alarm's time against the current time and calls trigger function if they are equal then stops
# TODO: slow down thread to reduce cpu usage?
def alarm_thread(alarm):
    alarm_time = datetime.time(hour = alarm.time[0], minute = alarm.time[1])
    run = True
    while run:
        current_time = datetime.datetime.now().time().replace(microsecond = 0)
        if current_time == alarm_time:
            trigger(alarm)
            run = False

# The trigger that is run when an alarm equals the current time
# This is a gnarly nightmarish way to do a playlist TODO: revise music player add random song selection
def trigger(alarm):
    print("Alarm Triggered", alarm.name, alarm.msg)
    pygame.mixer.music.load(os.path.join('res', 'music', 'hobbits.mp3'))
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.load(os.path.join('res', 'music', 'sherlock.mp3'))
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.load(os.path.join('res', 'music', 'skyrim.mp3'))
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.load(os.path.join('res', 'music', 'zelda.mp3'))
    pygame.mixer.music.play(0)
    #TODO: remove the self.thread value of the running alarm

def stop_trigger():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        print("Alarm Stopped.")
    else:
        print("Trigger is not running.")
    #TODO: remove the self.thread value of the running alarm

if __name__ == "__main__":
    alarms_path = os.path.join(os.path.dirname(os.path.realpath('__file__')), os.path.join("res","alarms", "alarms.json"))
    alarms_object = Alarms(alarms_path).load()
    print(alarms_object)

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
