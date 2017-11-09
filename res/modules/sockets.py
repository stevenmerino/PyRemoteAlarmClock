#! /usr/local/bin/python3.6

import socket
import threading

class ServerSocket:
    def __init__(self, port = 5001):
        self.s = socket.socket()
        self.host = socket.gethostname()
        self.port = port
        self.msg = None
        self.s.bind(("", self.port)) # Dont specify host when binding on RasPi
        self.s.listen(5)
        self.t = threading.Thread(target = self._listen)
        self.t.start()

    def _listen(self):
        while True:
            self.c, self.addr = self.s.accept()    # Wait for a client to connect
            self.data = self.c.recv(1024) # Recieve data from client
            self.c.send(self.data)  # Echo recieved data back to client
            self.c.close()
            self.msg = self.data.decode()
            #print("Server recieved msg.")
            if(self.msg == 'quit'): break # Temporary - shutdown server with quit msg

class ClientSocket:
    def __init__(self, server_address = socket.gethostname(), server_port = 5001):
        self.host = server_address
        self.port = server_port

    def send(self, msg):
        self.s = socket.socket()
        self.s.connect((self.host, self.port))
        self.msg = msg.encode()   # Convert message to bytes
        self.s.send(self.msg)
        while True:
            self.data = self.s.recv(1024)    # Recieve data
            if not self.data: break     # If data is empty break
            if(self.msg == self.data):  # Compare sent msg with recieved message
                print("Client sent msg successfully.")
            else:
                print("Error in transmission")
        self.s.close()  # Close socket when recieve loop breaks

if __name__ == '__main__':
    s = ServerSocket()
    c = ClientSocket()
    c.send('quit')

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
