# Copyright (c) 2021 - Vlad Mihailescu
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import board
import busio
import digitalio

uart = busio.UART(board.TX, board.RX, baudrate=115200)

# Dict of CLI parameters and corresponding lamp
lamps = {'3': digitalio.DigitalInOut(board.D1),    # UPLINK ACTY
         '2': digitalio.DigitalInOut(board.D8),    # TEMP
         '5': digitalio.DigitalInOut(board.D5),    # NO ATT
         '4': digitalio.DigitalInOut(board.D9),    # GIMBAL LOCK
         '7': digitalio.DigitalInOut(board.D6),    # STBY
         '6': digitalio.DigitalInOut(board.D10),   # PROG
         'B': digitalio.DigitalInOut(board.D7),    # KEY REL
         '8': digitalio.DigitalInOut(board.D11),   # RESTART
         '9': digitalio.DigitalInOut(board.D16),   # OPER ERR
         'A': digitalio.DigitalInOut(board.D12),   # TRACKER
         'D': digitalio.DigitalInOut(board.D17),   # PRIO DSP
         'RED': digitalio.DigitalInOut(board.D13), # On-board LED
         'C': digitalio.DigitalInOut(board.D14),   # ALT
         'F': digitalio.DigitalInOut(board.D18),   # NO DAP
         'E': digitalio.DigitalInOut(board.D15)}   # VEL

for i in lamps:
    lamps[i].direction = digitalio.Direction.OUTPUT

lastLampState = []

while True:
    data_rcvd = uart.read(14)
    if data_rcvd is not None:
        lamps['RED'].value = True # Blink on-board LED during RX
        data = ''.join([chr(i) for i in data_rcvd])
        # Remove unwanted characters from data string
        for ch in ['G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','x','Y','Z','a','b']:
            if ch in data:
                data = data.replace(ch,'')
        data = list(data)

        if data != '':
        # if lamp code was not present in last state, turn it ON
            lastLampsON = []
            for i in range(0, len(data)):
                lastLampsON += data[i]
                if data[i] not in lastLampState:
                    lamps[data[i]].value = True
                # If lamp code present in last state, it's already on so do nothing
                else:
                    pass
            for i in range(0, len(lastLampState)):
                # Turn OFF lamps that were previously ON unless already OFF
                if lastLampState[i] not in data:
                    lamps[lastLampState[i]].value = False
        elif data == '':
            for i in lastLampsON:
                lamps[lastLampsON[i]].value = False
        lastLampState = data
        lamps['RED'].value = False