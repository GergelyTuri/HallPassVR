# mouseVR
## Head-fixed Mice Virtual Reality System   
@GergelyTuri adding deployment/update time

This project aims to support naturalistic research about how mice cranial nerves respoonse when running under visual stimuli (espeically gratings or dot stimuli). Implementing VR environment can create a more realistic environment for experiment. The overall system will be used as a part for further research with several behavirol boxes. The main parts for this project are: 1) designing a VR environment which can synchronize the mice movement to the virtual corridor with low latency. 2) Create GUI to adjust, generate and store information for corridor. The prototype virtual corridor has been done with basic functions. The most recent demo videos can be found [here]():  

## HARDWARE: 
1. Arduino Nano: Tracking and converting mice movement on treadmill to serial data. 
2. Raspberry Pi 4: Building and simulating the virtual reality environment. 
3. TI DLPDLCR2010EVM: Projector.
4. ESP32: Run as the rotary encoder and bluetooth/WiFi for further development.



## SOFTWARE: 
1. Python: Used for designing the corridor. The mainly used language fr the Project is python. 
2. Linux: OS for Raspberry Pi.
3. tkinter: Designing the user interface.


### WHAT WE HAVE DONE: 
1. We have done building the main part for the system which can simultaneously run and show the virtual reality environment on the computer display.
2. Finish the prototype GUI.
3. Test the whole system with several testbenches.



### WHAT WE CURRENTLY WORKING ON: 
1. Replace Arduino with ESP32 for further development.
2. Try communicating Android Studio App with gyroscape data captured with VR environment, mimicking rotating movement of mice head.
                
                
### FUTURE PLANS: 
1. Optimize durability and accuracy of the system.
2. Adding RFID sensor increasing accuracy of synchronization.
3. Implement algorithm which can stablize the totally brightness of the whole virtual reality environment, either OpenCV or FPGA.




## Initializing VR environment (demo): 

1. Download, unzip the python file demo_7_2.zip file under MouseVR/demo_complete to pi3d/pi3d_demo. 
2. To open GUI and run the VR.
 ```bash
python3 GUI_Interface_demo_7_2.py
 ```
To cleaning all history, pattern combinations, file paths and other data.

```bash
python3 nuke.py
 ```
Corridor_demo_7_2.py: Individual VR corridor.
 ```bash
python Corridor_demo_7_2.py
 ```

GUI: 
![GUI](/media/GUI/GUI.jpg)

Virtual corridor: 
![corridor](/media/VR/VR.jpg)



------------------------------------------------------------------Relative Document---------------------------------------------------------------- 

p13d Library: 
https://pi3d.github.io/html/ReadMe.html

ESP Arduino IDE board Manager set up:
https://github.com/espressif/arduino-esp32

Hardware setup:
https://github.com/HarveyLab/mouseVR

Relative paper: 
1. https://www.nature.com/articles/d41586-019-00791-w
2. https://www.phenosys.com/products/virtual-reality
3. https://academic.oup.com/cz/article/63/1/109/2962415
4. https://www.raspberrypi.org/forums/viewtopic.php?t=243812#:~:text=The%20Raspberry%20Pi%204%20has,maybe%204K30%20will%20be%20supported
5. https://www.biorxiv.org/content/10.1101/2020.09.13.295469v1?rss=1
6. https://pubmed.ncbi.nlm.nih.gov/32149601/
7. https://www.janelia.org/open-science/large-spherical-treadmill-rodents
8. https://www.ti.com/store/ti/en/p/product/?p=DLPDLCR2010EVM

