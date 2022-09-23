# HallPassVR
## Head-fixed Mice Virtual Reality System   

We developed an inexpensive, single board computer-based, easy-to-use setup for investigation of mouse spatial learning behavior using a visual virtual reality (VR) environment. This system uses a network of microcontrollers (ESP32) and a Raspberry Pi single-board computer to display a virtual linear track to a headfixed mouse running on a wheel. Along with a custom software package written in Python and C++ to generate parameterized virtual environments, this methodology allows researchers the design of various spatial navigation-based experiments to study neural circuits in the brain underlying spatial behaviors. [Example video here](https://www.youtube.com/watch?v=iCfhJT3dYIo):  

![Mouse on wheel](/media/mouse_on_wheel_small.PNG)]

## Main hardware requriments: 
1. _ESP32 microcontrollers_ to track and convert mouse movement on a treadmill or wheel to serial data and to control other harware elements (lick spout for reward delivery).
2. _Raspberry Pi 4_ for building and simulating the virtual reality environment. 
3. _Projector_ for visualizing the virtual corridor.
4. PCB shields through [OpenMaze](https://claylacefield.wixsite.com/openmazehome/openmaze-shields)

## Software requirements: 
1. The virtual corridor was designed with _Python_. 
2. Native, Linux-based OS for Raspberry Pi.
3. _tkinter_ was used for designing the graphical user interface.
4. _Arduino IDE_ for programing the microcontrollers.
5. _Processing_ for data collection and plotting.
6. The analysis of behavior files currently requires _Matlab_.

### What we have done: 
1. We built the main part of the system which can simultaneously run and show the virtual reality environment on a computer display and a projector.
2. We have built a prototype GUI which can be used to build virtual corridors from virtually any kind of jpeg images.
3. We tested the system with several testbenches.

### Work in progress: 
1. Finalizing the code by adding documentation and examples.
                
### Future plans: 
1. Optimization of the system by e.g., adding an RFID sensor to increase wheel tracking accuracy.
3. Adding other features to the VR software like naturalistic scenes, looming stimulus or cliff-like effects. 
4. Implementing the analysis scripts in Python.
5. Increasing the flexibility of the existing protocols. 
6. Implementing a wireless (e.g., bluetooth) system using this platform.
## Quickstart:
### Initializing VR environment: 

1. Open a terminal window in Raspberry Pi and navigate to the `HallPassVR` folder
 ```bash
cd /home/pi/Documents/HallPassVR
 ```
2. Starting the VR GUI:
```bash
python3 HallPassVR_GUI.py
 ```
3. Setting up the floors and corridors in the GUI
4. Setting up `Processing` sketch to acquire and plot behavior.
5. Preliminary analysis of the acquired data can be done in Matlab with the scripts in `/Analysis code` folder.


#### GUI: 
![GUI](/media/GUI/GUI.jpg)

#### Example virtual corridor: 
![corridor](/media/VR/VR.jpg)

For feature requests, support or questions, please open a ticket on [GitHub](https://github.com/GergelyTuri/mouseVR/issues). 