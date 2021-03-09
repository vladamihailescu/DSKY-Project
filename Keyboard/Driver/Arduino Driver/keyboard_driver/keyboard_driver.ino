/* Copyright (c) 2021 - Vlad Mihailescu
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
*/

#include <Keypad.h>

const byte ROWS = 3; 
const byte COLS = 7; 

uint8_t buf[8] = {0};

char hexaKeys[ROWS][COLS] = {
  {87, 87, 36, 37, 38, 6, 8},
  {25, 86, 33, 34, 35, 19, 21},
  {17, 39, 30, 31, 32, 14}
};

byte rowPins[ROWS] = {2, 3, 4}; 
byte colPins[COLS] = {5, 6, 7, 8, 9, 10, 11}; 

Keypad dsKb = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

void setup(){
  Serial.begin(9600);
}
  
void loop(){
  char dsKey = dsKb.getKey();
  
  if (dsKey){
    buf[2] = dsKey;
    Serial.write(buf, 8);
    releaseKey();
  }
}

void releaseKey()
{
  buf[0] = 0;
  buf[2] = 0;
  Serial.write(buf, 8);  // Release key  
}
