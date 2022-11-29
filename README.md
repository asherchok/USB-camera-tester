# USB Camera Tester Script

## About
The goal of this script is to skip the manual process of switching camera with mouse or keyboard on the Windows 10/11 Camera program. This script is designed for performing quality testing for any camera devices. This work combines code from the following 2 sources:
- Code that detects if a USB device is inserted: https://stackoverflow.com/questions/59868022/detecting-usb-device-insertion-on-windows-10-using-python from user @Richard
- Code that activates camera on PC: https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/

## Environment
- Python 3.10.8

## How to use


Install the following libraries on Windows PowerShell terminal:

```sh
pip install wmi
pip install opencv-python
```
Save the python file USB<nolink>-cam-tester.py to your preferred directory from this repository. Read a quick tutorial on how to navigate directory on PowerShell terminal [here](https://www.itprotoday.com/powershell/how-use-powershell-navigate-windows-folder-structure). 
### Activating the script
At the directory that you had saved the USB<nolink>-cam-tester.py script, enter the following onto the terminal:
```sh
python .\USB-cam-tester.py
```
### Instructions
When the script is running, connecting a USB Camera device to PC will open a new window displaying the external camera. There are two ways to close the new window:

- Unplug the USB device.
- Press '/' key.

To stop the script entirely, press CTRL + BREAK (or pause key on laptop keyboards).

##### (optional)
To change the close window key other than the / key, simply edit Line 14 and change / into any other key. One possible example to close the window with c key instead of / would be:
```sh
      if cv2.waitKey(1) & 0xFF == ord('c'):
```
## Limitations
The design of this code is to test one USB camera device one at a time. Current version of this code allows more than one USB camera to be connected to a PC. When this happens, the script will display the first connected USB camera. When the first camera is disconnected, the display window for the second camera will load after a few seconds.

Current version of this code does not allow multiple external USB cameras to display **at the same time**.

## Issues
Issues that were identified by author while in actual deployment at workplace were listed down below.

-Occasionally, new window will not show up on the first insertion and requires replugging to work. This might be a hardware issue and not the script itself.

-New window will not show up consistently if the USB camera device is inserted into a USB extender hub.

Pull requests are welcomed to improve the following project. Future improvement of this project would be converting the python file to an executable file so that users can skip all the steps in **How to use** and **Activating the script**.

## License
MIT

[//]: # (Comments here will not be read by markdown compiler)
