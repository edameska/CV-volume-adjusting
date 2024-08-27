# Hand Gesture Volume Control

This project uses computer vision and hand tracking to control the volume of your audio output on a Linux or Windows system using hand gestures.

## Overview

The script captures video from your webcam, detects your hand, and uses the distance between your thumb and index finger to adjust the system volume. It uses the `OpenCV` library for video capture and hand tracking, `numpy` for mathematical operations, and `pulsectl` for controlling the system audio.

## Requirements

- Linux or Windows Subsystem for Linux (WSL)
- Windows 
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- PulseAudio (`pulsectl` Python library) or Python Core Audio Windows Library (`pycaw` Python library)

## Installation

1. **Install Python dependencies**:

   ```bash
   pip install opencv-python numpy pulsectl
   ```
   or

     ```bash
   pip install opencv-python numpy pycaw
   ```
3. **Ensure your webcam is connected and functioning properly**

## Usage
1.**Run the script using python**
   - for Linux
   ```bash
   python volumeControlLinux.py
```
  - for Windows
 ```bash
   python volumeControlWindows.py
```

2. **Adjust volume by moving your thumb and index finger** :
    -Closer together: decreases volume.
    -Farther apart: increases volume.


## Customization
* **Change Sink Device**: Modify the sink variable in the set_volume function to control a different audio device. The default is set to headphones (pulse.sink_list()[3]), but you can change this index to match your desired output device.
* **Change Camera**:  Modify the vap variable to control a different camera device. The default is set to primary camera (cap = cv2.VideoCapture(0)), but you can change the index to match your preferred device.
* **Adjust Detection Confidence**: You can change the detectionCon parameter in HTM.handDetector to adjust the hand detection confidence threshold.
