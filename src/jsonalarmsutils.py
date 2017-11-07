#! /usr/bin/python3.6

import threading
import datetime
import jsonalarms as ja
import pygame
import os

pygame.mixer.init()

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

def stop_trigger():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        print("Alarm Stopped.")
    else:
        print("Trigger is not running.")

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

# Checks each Alarm in the list of Alarms if 1. today is in the Alarm's list of weekdays 2. the alarm is in the future and 3. if a thread for the alarm has already been created.
# If an alarm is today, in the future, and has no thread, one is created.
def check_alarms(alarms):
    for alarm in alarms.alarms['Alarms']:
        if check_alarm_weekday(alarm):
            if check_alarm_time(alarm):
                if alarm.thread == None:
                    create_thread(alarm)


if __name__ == "__main__":
    # a = ja.Alarms("alarms.json").load()
    # check_alarms(a)
    # print(a.alarms['Alarms'][0].thread)
    #create_thread(a.alarms['Alarms'][0])
    #check_alarm_time(a.alarms['Alarms'][0])
    #alarm_thread(a.alarms['Alarms'][0])
    #print(f(a.alarms['Alarms']))
