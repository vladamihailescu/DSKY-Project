# DSKY-Project
My open source journey to building a functional, historically-accurate DSKY interface that can be used in simulation. 
 
## v1.0 Hardware (Completed)
 - Raspberry Pi 3B+ running VirtualAGC + driving the display & keyboard
 - Nextion 4.3" LCD HMI (NX4827T043_11) display
 - Alarm Panel PCB designed by Riley Rainey
 - Hand assembled keyboard using Cherry MX blue key switches & Arduino UNO in USB HID mode
 - 3D Printed shell components made from models created/modified by Riley Rainey/Manoel DaSilva from original MIT drawings or myself

## v1.5 Hardware (In Progress)
 - Raspberry Pi 3B+ running VirtualAGC + driving the display & keyboard
 - Nextion 4.3" LCD HMI (NX4827T043_11) display
 - Alarm Panel PCB designed by Riley Rainey
 - Keyboard PCB designed by me with Cherry MX green key switches & LED backlighting
 - 3D Printed shell components made from models created/modified by Riley Rainey/Manoel DaSilva from original MIT drawings or myself

## v2.0 Hardware (Planned)
 - Raspberry Pi 3B+ running VirtualAGC + driving the display & keyboard
 - Custom EL display panel
 - Alarm Panel PCB designed by Riley Rainey
 - Keyboard switches assembled as per original spec using microswitches
 - 3D Printed shell components made from models created/modified by Riley Rainey from original MIT drawings or myself

## Software
 - Drivers for display, alarm panel & keyboard written in Python3
 - VirtualAGC project
 - Project Apollo - NASSP
 
## Setup
Raspberry Pi running VirtualAGC is driving the Nextion HMI, sending lamp instructions to the Alert board and reading keystrokes from Keyboard

## Task List
- 1.0
- [x] Build working GUI for HMI display
- [x] Driver for Nextion HMI display
- [x] Assemble alarm panel PCB
- [x] Driver for alarm panel
- [x] Assemble keyboard
- [x] Driver for keyboard
- [x] Update piDSKY2.py file
- [x] Test with VirtualAGC

- 1.5
- [x] Design & assemble a custom PCB for keyboard
- [ ] Improve code
- [ ] Refine GUI to more closely match original DSKY display
- [ ] Keyboard caps improvements
- [ ] Improve overall DSKY fit & finish & pave way to v2.0

## References
 [VirtualAGC Project](https://www.ibiblio.org/apollo/) - I am so thankful that this exists because it has been my dream to build my own DSKY ever since I first learned of the
 project\
 [Riley Rainey](https://github.com/rrainey) - His amazing work in designing the alert and keyboard PCBs, modeling the DSKY shell and inner components from original drawings gave
 me the opportunity to start this project\
 [Manoel DaSilva](https://github.com/ManoDaSilva) - He created the HMI file which I modified and adapted to my code and the Cherry MX keyswitch stems I used.\
