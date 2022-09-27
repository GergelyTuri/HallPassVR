# Instructions for the electronic components

Files in the `ESP32 files` directory should be uploaded to the ESP32 boards connected to the lickport and rotary encoder. 

Files in `/PCBs` can get manufatured with companies specialized to PCB production. Typically we use [OSH Park](https://oshpark.com/) if we don't want to modify the design. More info on how to order and assemble these shields can be found on [OpenMaze](http://www.openmaze.org/).

| material | description | source |
| -------- | ----------- | ------ |
| Raspberry Pi 4 model B | single-board computer | e.g., raspberrypi.com, adafruit.com |
| rotary encoder | ENS1J-B28-L00256L | digikey.com[^1] |
|ESP32 devKitC v4 | microcontroller (x2)| e.g., [Amazon.com](https://www.amazon.com/s?k=ESP32&crid=ZCZ3J597DJO9&sprefix=esp32%2Caps%2C94&ref=nb_sb_noss_1)|
|OpenMaze OMwESP32 shield| custom design | see: `/PCBs` folder |

[^1]: Alternative sources: amazon.com, mouser.com, DigiPart, etc.

## Installation instructions for Raspberry Pi:
### Configure RaspberryPi 4 model B 
This single-board computer has an onboard GPU to facilitate VR environment rendering, as well as two HDMI ports for experiment control/monitoring and VR projection.
1. Download Raspberry Pi Imager app and install OS (currently RaspberryPi OS r.2021-05-07) on microSD card (8GB+), insert and boot Raspberry Pi.
2. Configure Raspberry Pi: (menu bar) 
- `Preferences>Raspberry Pi Configuration>`
  - `Display>Screen Blanking>Disable`
  - `Interfaces>Serial Port>Enable` 
  - `Performance>GPU Memory>256`
3. In the terminal: 
``` bash
sudo nano /boot/config.txt
``` 
then uncomment `config_hdmi_boost=4`. Save, reboot the Raspberry Pi.

4. Download and install Arduino IDE from arduino.cc/en/software (e.g. arduino-1.8.19-linuxarm.tar.gz)
5. Download and install Processing IDE from github.com/processing/processing4/releases (e.g. processing-4.0.1-linux-arm32.tgz)
6. In the terminal
```bash
sudo pip3 install pillow –-upgrade
```
7. Then, 
```bash
sudo pip3 install pi3d
```
8. Install ESP32 support on Arduino IDE.

## Set up rotary encoder-ESP32 connections
1. Connect wires between rotary encoder and ESP32.
2. Connect serial RX/TX wires between ESP32 Serial2 (pins 16,17) and behavior ESP32.
3. Connect serial RX/TX wires between ESP32 Serial0 (RX/TX) and Raspberry Pi GPIO (or direct USB connection).
4. Set up behavior ESP32 connections with behavioral hardware (via OMwESP32small PCB).
5. Connect 12V liquid solenoid valve to ULN2803 IC output (e.g. pin#32).
6. Connect lick port to ESP32 touch inputs (e.g. T2, GPIO15).
7. Connect serial RX/TX wires between behav ESP32 Serial2 (pins 16,17) and rotary encoder ESP32 (see above #1.b.).
8. Plug USB into Raspberry Pi USB port (or other PC running Processing to capture behavior data).
9. Plug Raspberry Pi HDMI #2 output into projector HDMI port.

## Set up software (rotary encoder ESP32 and behavior ESP32 w. OM PCB)
1. Plug rotary encoder ESP32 into Raspberry Pi USB port first- it will be automatically be named `/dev/ttyUSB0`
2. Load rotary encoder arduino code by first selecting the ESP32 under `Arduino IDE>Tools>Boards>ESP32 Dev Module`, then `Tools>Port`>`/dev/ttyUSB0`, then click `Upload`: `RotaryEncoder_Esp32_VR.ino`
3. Plug behavior ESP32 into Raspberry Pi USB port next- it will be named `/dev/ttyUSB1`
4. Load behavior sequence arduino code (ESP32 Dev Module already selected), then `Tools>Port>` `/dev/ttyUSB1`, then click `Upload`: `wheel_VR_behavior.ino`
5. You can test serial connections by selecting the Port in the Arduino IDE, then clicking on `Tools>Serial Monitor` (baud rate:115200), to observe serial output from the rotary board (USB0) or the behavior board (USB1).
6. Download HallPassVR python code from this GitHub repo (`/software/HallPassVR`) to `/home/pi/Documents`.
