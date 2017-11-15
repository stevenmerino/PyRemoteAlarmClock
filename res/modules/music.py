import os
import random
import threading
import pygame

class Player(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()
        self.daemon = True
        self.playlist = get_songs()
        pygame.mixer.init()

    def run(self):
        while not self.shutdown_flag.is_set():
            if not pygame.mixer.music.get_busy():
                try:
                    song = self.playlist.pop()
                except IndexError:
                    self.playlist = get_songs()
                else:
                    print("Alarm playing:", os.path.basename(song))
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play(0)
        pygame.mixer.music.stop()
        print("Player Stopped.")

def get_songs():
    songs = list()
    for song in os.listdir(os.path.join(os.path.dirname(os.path.realpath('__file__')), os.path.join("res","music"))):
        if song.endswith(".mp3"):
            songs.append(os.path.join(os.path.dirname(os.path.realpath('__file__')), os.path.join("res","music", song)))
    return random.sample(songs, len(songs))

if __name__ == "__main__":
    pass
    # music = Player()
    # music.start()
    # print("Player Started.")
    # time.sleep(15)
    # music.shutdown_flag.set()
    # while True:
    #     time.sleep(1)
    #     print("endless")


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
