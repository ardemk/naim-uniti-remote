# Why I did this piece of software ?

Just like Pepitooo (OP) I'm using a Logitech Harmony universal remote to control my home device (TV, Home Cinema, Projector, ...)

The Naim Uniti Atom is integrated in a complex home theater system, and having to stay with the Uniti Remote was not acceptable.

Moreover, as I have to use the Uniti Atom in combination with a receiver, its volume should stay fixed (at 75 in my case) when watching a movie, but low when listening to music with Spotify Connect through the Android app.

Note : AV Fixed Volume was not an option for me, as it sets the Uniti's volume to 100 which introduces too much hiss with my speakers. 75 is a more acceptable level, but it implies that the volume has to be changed manually for each use case. Again, not very convenient!

# How to use the provided code ?

The provided code has to be used in a Home Assistant environment.

Are provided the entries for the configuration.yaml as well as the automation.yaml

These entries have just to be copied into your respective files (do not forget to modify the IP adress of your Uniti device).

# How does it work?

The raspberry will send the commands via HTTP requests to the Naim Uniti device through shell commands (su not needed).
With the provided code, the "on" command to the Uniti is triggered when harmony state goes from "off" to "on", and turned off with the way around.

# Known issues

Pushing an automated custom volume per input breaks the volume management of Spotify Connect through Android (iOS not tested).
Example : let's say that your Uniti is at an initial volume of 50, and that you sent through a HTTP request a volume of 75. On Spotify Connect through Android, the "0" level of the volume bar will be the delta introduced which is in this case +25. 

# On-going work
I've written two python scripts as a workaround to the previous issue :
- One that read the initial volume when the Uniti is turned on and store it in a local txt file before pushing the target volume for the input,
- One that reads the txt file and sets the volume as it was initially and then turns off the Uniti.

Unfortunately, I am still unable to automate their execution through shell commands via automation.yaml (error code 2 in the console).
