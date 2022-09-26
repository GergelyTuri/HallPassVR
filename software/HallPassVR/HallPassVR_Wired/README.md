# HallPassVR
## Virtual reality system for head-fixed mouse experiments. 

Main python files:
1. GUI_INTERFACE.py: main GUI script (can rename without consequence)
2. NUKE.py: deletes history or something like that?
3. VR_CORRIDOR_BUILD_WIRED.py: main VR run script
4. VR_OPEN.py: creates VR on second screen with TK (this is run by HallPassVR_GUI.py, and in turn runs HallPassVR_wired.py)

/HallPassVR_wired/image folder contains image files for use with VR
1. ELEMENTS: image options for hall panels (so if you want a new panel pattern, insert into this folder before running “python3 GUI_INTERFACE.py”)
2. HIST_PATH: jpegs of previous entire paths, with datetime they’re run (and name from GUI)
3. HIST_PATTERN: jpegs of constituent patterns (4-element combinations, which are read into GUI to use later)
4. SOURCE/DEFAULT: default jpegs (e.g. chess_pattern_5x5.jpg)
