# Whale detection on acoustics data-EfficientNet B2
## Data:
30,000 samples of 2-second .aiff sound files with a sample rate of 2kHz

## Idea:
I proceed to convert the audio to mel spectrogram to generate 255x255 .png images, and then I generate Tfrecords. I then feed the Tfrecords to a CNN with Efficientnet B2 as the backbone of the model architecture to classify if there's a whale call present in the images.

## Research objective:
The main objective of this algorithm is to detect North Atlantic right whale calls from audio recordings in order to prevent collisions with shipping traffic.

Detecting whale sounds is important for a few reasons.
* Firstly, it helps researchers to understand more about the behavior and communication of these large marine mammals. Whales produce a variety of vocalizations, including songs, whistles, and clicks, which are used for communication and echolocation. By analyzing these sounds, researchers can gain insight into their behavior, migration patterns, and social structure.
* Secondly, whale sound detection is crucial for conservation efforts. Many species of whales are endangered or threatened due to factors such as hunting, climate change, and pollution. By tracking their vocalizations, researchers can monitor populations and identify areas where conservation efforts are needed.

## Pre-requisites:
* The frequency range of the right whale moans is typically between 100 and 500 Hz, with most of the energy cocentrated around 200 Hz. The moans are usaually produced at a fundamental frequency of around 100 Hz, but contain a series of harmonics and overtones that extend up to 500 Hz.
