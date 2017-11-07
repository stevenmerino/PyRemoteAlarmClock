# RemoteAlarmClock

Alarm clock application that is controlled from a separate device. The idea being that you need get out of bed, go all the way to a different room to turn off your morning alarm. Further increasing the chances that you will stay awake when your alarm goes off. No snoozing allowed!

It should be mentioned that I'm a noob programmer. This program uses raw sockets to transfer JSON across the network and potentially has security risks.

**USE AT YOUR OWN RISK**

## Getting Started

The way I'm implementing this into my routine is by having a wireless Raspberry Pi with speakers in my room, running the RemoteAlarmClock server. The RemoteAlarmClock client is used from my main computer in another room. In the future I would like to set up a battery powered Raspberry Pi Zero W as the client and be able to place it anywhere I choose say the kitchen next to the coffee pot for instance.

If you are going to use the server on a Raspberry Pi currently you will need to build python 3.6.0 yourself. [These](https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f) instructions worked for me.

See Prerequisites for additional requirements.

### Prerequisites

[Python 3.6.0](https://www.python.org/downloads/release/python-360/)
```
When using earlier versions: "AttributeError: 'TypeField' object has no attribute 'name'"
```

[pygame](https://www.pygame.org/wiki/GettingStarted)
```
sudo pip3.6 install pygame
```

### Installing

Place music files in "src/res/music"
You will need to edit the "src/jsonalarmsutils.py" trigger function to point to the correct path of your songs.
It is pretty embarrassing how this works, but it will be changed in the next feature upgrade to detect mp3 in the directory automatically and not use weird while loops to detect the end of the song.

```
def trigger(alarm):
    print("Alarm Triggered", alarm.name, alarm.msg)
    pygame.mixer.music.load(os.path.join('res', 'music', 'song1.mp3'))
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.load(os.path.join('res', 'music', 'song2.mp3'))
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pass
```


## Running the tests

TODO: Explain how to run the automated tests for this system

### Break down into end to end tests

TODO: Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

TODO: Add additional notes about how to deploy this on a live system

## Built With

* [Python](https://www.python.org/downloads/release/python-360/) - Version 3.6.0

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

Version 1.0.1 - [Changelog](CHANGES.md)

## Authors

* **Steven Merino**, 2017, [stevenmerino](https://github.com/stevenmerino)

See also the list of [contributors](AUTHORS.md) who participated in this project.

## License

See the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* [Randy Daw-Ran Liou](https://medium.com/@dawran6/writing-descriptors-in-python-3-6-b26affd15a0a) - Python descriptors article.
