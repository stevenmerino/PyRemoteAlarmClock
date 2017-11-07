#! /usr/bin/python3

import serverclientsocket as scs
import jsonalarms as ja
import sys

c = scs.ClientSocket()
alarms = ja.Alarms("alarms.json").load()

if sys.argv[-1] == "send":
    c.send(alarms.to_json())
else:
    c.send(sys.argv[-1])
