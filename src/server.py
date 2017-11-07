#! /usr/bin/python3.6

import serverclientsocket as scs
import json
import jsonalarms as ja
import jsonalarmsutils as jau


if __name__ == "__main__":
    s = scs.ServerSocket()

    try:
        a = ja.Alarms("alarms.json").load()
    except:
        a = ja.Alarms("alarms.json")
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
