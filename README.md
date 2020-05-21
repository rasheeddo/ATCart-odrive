# ATCart-odrive

please make sure your MOAB's IP is correct according to `atdrive-moab` [firmware](https://github.com/rasheeddo/atdrive-moab/tree/odrive).


`testSendUDP.py` is a test script to send command packet to MOAB+ODRIVE. You can choose `sendRPMOdrivePacket(rpmR,rpmL)` or `sendDEGOdrivePacket(degR,degL)` depends on each mode you want to control.

`testRecvUDP.py` is a test script to listen odrive feedback variable. The data you will get are
[int mode, float rightWheel_rpm, float leftWheel_rpm, float rightWheel_degree, float leftWheel_degree, float rightWheel_initial_degree, float leftWheel_initial_degree].

