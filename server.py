#! /usr/local/bin/python3.6

import res.modules.sockets as sockets
import res.modules.alarms as alarms
import json
import os

if __name__ == "__main__":
    server_socket = sockets.ServerSocket()

    alarms_path = os.path.join(os.path.dirname(os.path.realpath('__file__')), os.path.join("res","alarms", "alarms.json"))

    try:
        alarms_object = alarms.Alarms(alarms_path).load()   # Loads alarm object from file
    except:
        alarms_object = alarms.Alarms(alarms_path)          # If there is no alarm file, create new alarm object.
        print("Created new Alarms object.")
    else:
        print("Alarms object loaded from file.")

    while True:
        alarms.check_alarms(alarms_object)                  # Create threads from alarm object if applicable
        if server_socket.msg is not None:
            try:
                json_alarms = json.loads(server_socket.msg)
            except json.decoder.JSONDecodeError:
                pass
            else:
                print("Client sent JSON.")
                alarms_object.save(json_alarms)     # Save json to file
                alarms_object.load()                # Load newly saved file into alarms_object
                server_socket.msg = None

            if server_socket.msg == "stop":
                alarms.stop_trigger()
                server_socket.msg = None
            elif server_socket.msg == "status":
                print("Client requested status. Feature unfinished.")
                server_socket.msg = None
            elif server_socket.msg == "quit":
                print("Client sent 'quit', server shutting down.")
                break
            elif server_socket.msg == None:
                pass
            else:
                print("Client sent unknown command.")
                server_socket.msg = None

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
