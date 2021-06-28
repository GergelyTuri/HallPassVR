# mouseVR
virtual reality environment for mice

This project aims to support neuroscientist exploring how mice brain cells work when the mice are running in the virtual reality environment. The main part for this project is designing a system which can synchronize the mice movement to the virtual corridor with low latency. The prototype virtual corridor has been done with basic functions. The most recent demo videos can be found here: https://drive.google.com/drive/u/2/folders/1Ucv_41gNv25MAfak_pyqquLuZ15v62hw 

Hardware: 1) Arduino: Tracking and converting mice movement on treadmill to serial data. 
          2) Raspberry Pi 3B: Building and simulating the virtual reality environment. 
          3) TI DLPDLCR2010EVM: Projector.

Software: 1) Python: Used for designing the corridor. The mainly used language for the Project is python. 
          2) Linux: OS for Raspberry Pi.
          3) tkinter: Designing the user interface.


What we have done: We have done building the main part for the system which can simultaneously run and show the virtual reality environment on the computer display 

What we are currently doing: 1) Desginging the User interface through tkinter, providing a more convenient way for user to interact with the system. 
                             2) Intergrity the whole system. Replace the normal display with the TI DLPDLCR2010EVM.
                         
Our future plan: 1) Adding algorithm which can stablize the totally brightness of the whole virtual reality environment. 

Relative Document: 

p13d Library: 
https://pi3d.github.io/html/ReadMe.html


STM32 bootload instruction:
https://circuitdigest.com/microcontroller-projects/programming-stm32f103c8-board-using-usb-port

Relative paper: 
1. https://www.nature.com/articles/d41586-019-00791-w
2. https://www.phenosys.com/products/virtual-reality
3. https://academic.oup.com/cz/article/63/1/109/2962415
4. https://www.raspberrypi.org/forums/viewtopic.php?t=243812#:~:text=The%20Raspberry%20Pi%204%20has,maybe%204K30%20will%20be%20supported
5. https://www.biorxiv.org/content/10.1101/2020.09.13.295469v1?rss=1
6. https://pubmed.ncbi.nlm.nih.gov/32149601/
7. https://www.janelia.org/open-science/large-spherical-treadmill-rodents
8. https://www.ti.com/store/ti/en/p/product/?p=DLPDLCR2010EVM

IMPORTANT: 
How to setup and run the demo: 1) Download and intall the python file dem0_5_10.py under pi3d_demo. Run command: python demo_5_10.py on the terminal under the pi3d_demo 
