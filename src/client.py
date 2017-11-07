#! /usr/bin/python3.6

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
