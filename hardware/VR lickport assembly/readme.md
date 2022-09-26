# Instructions for assembling the lickport

We developed a capacitive touch sensor lick port which is highly sensitive and easy to implement. A metal water spout is connected to ESP32 board which detects lick touch events and delivers liquid rewards via a solenoid valve actuated by an H-bridge circuit on the OpenMaze OMesp32 PCB. The sensitivity of the port can be tuned. Note: this type of lick sensor can introduce a significant amount of electric noise when the mouse licks the spout which could be disadvantageous for electrophysiological recordings. Please contact the authors for alternative solutions using IR beam break lick detection. 

| material | description | source |
| -------- | ----------- | ------ | 
|ESP32 | microcontroller | e.g., [Amazon.com](https://www.amazon.com/s?k=ESP32&crid=ZCZ3J597DJO9&sprefix=esp32%2Caps%2C94&ref=nb_sb_noss_1)|
|ESP32 shield| custom design | see files: ????? |
|Capacitive Touch Breakout|AT42QT1010|Sparkfun|
| lick spout | 20068-638 | [VWR](https://us.vwr.com/store/) |
|adjustable arm| for holding the lick spout | [Amazon](https://www.amazon.com/Magnetic-Adjustable-Indicator-Holder-Digital/dp/B00L5T2ZA8) |
|arm holder| 3D printed| attach file @claylacefield|
|spout holder| 3D printed | [water spout holder](water%20spout%20holder%20for%2016%20needle.stl) |
|solenoid valve |003-0137-900 | [Parker]([003-0137-900](https://ph.parker.com/us/12051/en/series-3-miniature-inert-liquid-valve/003-0137-900))|
|tubing | for delivering water| e.g., [this](https://www.fishersci.com/shop/products/exel-international-iv-administration-set-2/p-2624960)|

### Final assembly

![Lickport](../media/wheel_lickport_assembly.png)