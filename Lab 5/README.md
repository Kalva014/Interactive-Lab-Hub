# Observant Systems

**NAMES OF COLLABORATORS HERE**


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

## Prep

1. Spend about 10 Minutes doing the Listening exercise as described in [ListeningExercise.md](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%205/ListeningExercise.md)
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:
1. Pull the new Github Repo.(Please wait until thursday morning. There are still some incompatabilities to make the assignment work.)
1. Raspberry Pi
1. Webcam 

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show the filledout answers for the Contextual Interaction Design Tool.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

The following command is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***
# Object Detection
<img width="922" alt="Screen Shot 2022-10-23 at 5 09 45 PM" src="https://user-images.githubusercontent.com/46539140/197419512-8e274a4f-f4b1-4fd8-b058-64aceb015a6c.png">
* Potential Design: Food Classification System
Classify what type of category the food is a part of. Examples include being a vegetable or meat.

# Optical Flow Detection
<img width="915" alt="Screen Shot 2022-10-23 at 5 08 12 PM" src="https://user-images.githubusercontent.com/46539140/197419517-55512b90-2c3f-4567-84b7-f92943ec75ef.png">
* Potential Design: Sports movement system.
By using the optical flow algorithm, we can detect patterns in an athlete's movement which can help for coaching younger players users how to do a specific technique.

# Face Detection
<img width="925" alt="Screen Shot 2022-10-23 at 5 00 12 PM" src="https://user-images.githubusercontent.com/46539140/197419520-2daa2beb-c10d-4607-8acd-7fcafeb4e842.png">
* Potential Design: Skin Care system.
By scanning a user's face, the face detection can help diagnose what skin type they have to help with acne or blackheads. 

# Contours Detection
<img width="911" alt="Screen Shot 2022-10-23 at 4 58 06 PM" src="https://user-images.githubusercontent.com/46539140/197419527-8fe758bb-c2f9-4b51-a9a8-ec51c5106260.png">
* Potential Design: Lost object tracking system.
By being able to classify and detect the contours of specific objects, this algorithm can be applied to situations where someone could feed images to the algorithm of an object they lost in their room which can help them find it through the detection algorithm.


#### Filtering, FFTs, and Time Series data. 
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU or Microphone data stream could create a simple activity classifier between walking, running, and standing.

To get the microphone working we need to install two libraries. `PyAudio` to get the data from the microphone, `sciPy` to make data analysis easy, and the `numpy-ringbuffer` to keep track of the last ~1 second of audio. 
Pyaudio needs to be installed with the following comand:
``sudo apt install python3-pyaudio``
SciPy is installed with 
``sudo apt install python3-scipy`` 

Lastly we need numpy-ringbuffer, to make continues data anlysis easier.
``pip install numpy-ringbuffer``

Now try the audio processing example:
* Find what ID the micrpohone has with `python ListAvalibleAudioDevices.py`
    Look for a device name that includes `USB` in the name.
* Adjust the variable `DEVICE_INDEX` in the `ExampleAudioFFT.py` file.
    See if you are getting results printed out from the microphone. Try to understand how the code works.
    Then run the file by typing `python ExampleAudioFFT.py`



Using the microphone, try one of the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up a running averaging** Can you set up a running average over one of the variables that are being calculated.[moving average](https://en.wikipedia.org/wiki/Moving_average)

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

For technical references:

* Volume Calculation with [RootMeanSqare](https://en.wikipedia.org/wiki/Root_mean_square)
* [RingBuffer](https://en.wikipedia.org/wiki/Circular_buffer)
* [Frequency Analysis](https://en.wikipedia.org/wiki/Fast_Fourier_transform)


**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***
1. For the rms volume the minimum was 80 and the maximum was 400.<img width="218" alt="Screen Shot 2022-10-24 at 11 47 34 AM" src="https://user-images.githubusercontent.com/46539140/197569204-b0df3999-35d7-4009-b93c-e5c9af499d0e.png"><img width="226" alt="Screen Shot 2022-10-24 at 11 48 12 AM" src="https://user-images.githubusercontent.com/46539140/197569323-0cb8ceae-b432-4c4b-9144-6d76d86935a9.png"><img width="303" alt="Screen Shot 2022-10-24 at 11 56 08 AM" src="https://user-images.githubusercontent.com/46539140/197571079-a6bb3c15-669f-449a-8f70-48c6baa9e063.png">
2. Here is the code for the running average of the volume: <img width="384" alt="Screen Shot 2022-10-24 at 11 57 40 AM" src="https://user-images.githubusercontent.com/46539140/197571333-ac58ceb0-d7e9-4f48-a2e3-ebed38765264.png">

3. Max peak and min peak volume: <img width="312" alt="Screen Shot 2022-10-24 at 11 59 41 AM" src="https://user-images.githubusercontent.com/46539140/197571736-b0670838-0190-49e4-b132-a5827c84c40a.png">


### (Optional Reading) Introducing Additional Concepts
The following sections ([MediaPipe](#mediapipe) and [Teachable Machines](#teachable-machines)) are included for your own optional learning. **The associated scripts will not work on Fall 2022's Pi Image, so you can move onto part B.** However, you are welcome to try it on your personal computer. If this functionality is desirable for your lab or final project, we can help you get a different image running the last OS and version of python to make the following code work.

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr25
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi3 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

~~\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\*~~

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

~~**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***~~


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


### Part B
### Construct a simple interaction.

* Pick one of the models you have tried, and experiment with prototyping an interaction.
* This can be as simple as the boat detector showen in a previous lecture from Nikolas Matelaro.
* Try out different interaction outputs and inputs.
* Fill out the ``Contextual Interaction Design Tool`` sheet.[Found here.](ThinkingThroughContextandInteraction.png)
![IMG_0243](https://user-images.githubusercontent.com/46539140/198294777-1713947c-7e47-4300-9f7c-1c2cbde2b8a8.jpg)

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***
I tried the pose detection model using the Google's teachable machines. I specifically built upon my idea of a sports movement detection interaction that tracks and classifies the user's movements depending on the sport. I built the teachable machines model to recognize two types of important movements in basketball. The movements include shooting a basketball and directing other players to move by pointing.  The user can move themselves in front of the camera and if the model recoginzes the specific pose based off the sample images it took, it will classify whether the user shooting or directing on the screen.

Here is a video demonstrating the trained model on teachable machines:
https://drive.google.com/file/d/1nhWQ5PHDr9TikG0c43KqKXLiOrN_8c49/view?usp=sharing

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do? The sports movement detection model detects specific movements with no other objects in the background. The reason for no other objects in the background is to limit noise when classifying movemenets.
3. When does it fail? The object fails when trying to follow multiple movements as it has a hard time of detecting whose movements to track. 
4. When it fails, why does it fail? Additionally when the model fails it also fails due to not having a stationary class(when the user isn't doing anything). This causes the model to use one of the other classifications which is wrong.
5. Based on the behavior you have seen, what other scenarios could cause problems? Other scenarios that could cause problems would be dependent on the lighting and how fast the user is moving such that the camera does not have time to classify the movement since the movement is usually fast paced.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system? The users will be aware of the uncertainties if they see incorrect classification in the initial use. The users would have to test the same movement several times in order to get the correct angles and poses for the model to behave properly.
1. How bad would they be impacted by a miss classification? A misclassification could be bad if the model was being used for a sports competition that judges based off the types of movements being done(e.g. skateboarding competitions which scores based off what tricks the skateboarder does).
1. How could change your interactive system to address this? To change the interactive system would be to add more movement classes for the model to capture better analysis of the athletes.
1. Are there optimizations you can try to do on your sense-making algorithm. Additionally an optimization would be to show the accuracy of the movement and adding a larger dataset of labeled images.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

The sports movement detection model can be used for spectators, athletes, or coaches when watching sports. I noticed that a good environment is one that is well lit with not too many objects lying around in the background. The goal is to reduce as much background noise for classification. A bad environment is one in which the lighting is bad/dark and there are a lot of movement from other objects in the background. The model breaks when the athlete is not moving or if the athlete is moving too fast. By breaking it means that the classification is completely incorrect. Additionally since there aren't enough images fed into the model, the classification only works when the user is using a specific arm. The other behavior is that the model displays the accuracy it believes in classifying the movement. The athletes are quite skeptical with how accurate their movements are when seeing the model interpret their movement. However the movement classification works most of the time.

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***
https://drive.google.com/file/d/1r44J_Exx04vpWW-gbbnCURVcHC_TOJV0/view?usp=sharing

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
![IMG_0244](https://user-images.githubusercontent.com/46539140/198296735-4d457df4-d47f-4265-b9e4-bb1b45a8e9af.jpg)
https://drive.google.com/drive/folders/1LcT_aN3xQFyVG9DCTJoZntbBK8aKcSLR?usp=sharing
