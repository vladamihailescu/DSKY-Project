# DSKY-Project
 My open source journey to building a functional DSKY that can be used in simulator. 
 
 Hardware
 Raspberry Pi 3+
 Nextion 4.3" LCD HMI (NX4827T043_11) display
 Alarm Panel & Keyboard PCBs designed by Riley Rainey
 3D Printed shell components made from models created by Riley Rainey from original MIT drawings
 
 Software
 HMI file for the DSKY display layout
 Modified piDSKY2.py file of the VirtualAGC project
 Arduino sketches for reading keystrokes and alert lamp statuses
 
 Setup
 Raspberry Pi running VirtualAGC is driving the Nextion HMI, sending lamp instructions to the Alert board and reading keystrokes from Keyboard
 
 References
 VirtualAGC Project - I am so thankful that this exists because it has been my dream to build my own DSKY ever since I first learned of the project
 Riley Rainey - His amazing work in designing the alert and keyboard PCBs, modeling the DSKY shell and inner components from original drawings gave me the opportunity to start
                this project
 Manoel DaSilva - He created the HMI file which I modified and adapted to my code
