# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [LED Blink](#LED_Blink)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## LED Blink

### Assignment Description

For this assignment, we had to make the LED on the Pico blink. 

### Evidence 

![ezgif-3-c815a12281](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/65563a97-4842-4247-88bb-90def2fd031b)

### Wiring

No wiring

### Code

[Code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/LED_blink.py) 

### Reflection

This assignment was a good reintroduction to circuit python for me. It reminded me of the basic lines of code like time.sleep() and the different variables to import like board. It was also a great tutorial to pushing to github which last year I didn't fully know how to do. The tutorial explains that you have to save the code with CTR S then in Explorer click the plus and finally use the drop down next to commit and press "commit and push". Overall I really enjoyed this assignment because it was fairly simple but informative after a summer of not coding.

## Launchpad Part 1 (countdown)

### Assignment Description
We were assigned to make a countdown from 10 in the terminal and when it gets to 1 it says "Liftoff"

### Evidence 
![ezgif-4-5c041d7028](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/6c06b48a-1de6-400c-8a44-48039b61105d)

### Wiring
No wiring

### Code
[code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Laucnhpad_Part_1)

### Reflection

This assignment was simple and informative for using Pico and the terminal. I learned that to run in Pico you have to click on the code then save (CTR s) and to run you click (CTR d), I was a little confused because I was pressing F5 to run it and it directed my to the circuit python terminal instead of the pico one. 1 piece of code I learned was the range line (for x in range(0,0,0):) I used this line to set the constraints for the countdown (1-10). So for the first blank, you put in the number  you want to start with like 10, for the second blank you want to put in the number 1 less than the one you want it to stop at, so if I wanted to stop it at 1 I would put 0. Finally, for the last one, it is the number from which you want to count up or down so I wanted to count by 1 so I had to put -1 and if you don't put anything in the blank it will count up from 1. Overall this assignment wasn't too difficult and has a good explanation of what the range command did.

## Launchpad Part 2 (LED)

### Assignment Description
For this assignment, we had to add on to the previous countdown but make a red LED blink when it counted down and a blue light blink when it said "Liftoff".

### Evidence
![ezgif-3-79db49eaea](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/f1670d59-62e1-4002-94ee-dddbf565b040)

### wiring 
![launchpad led wiring](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/a741c193-4b99-4aba-8f90-9eeb1544838d)

### Code
[code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Launchpad_Part_2)

### Reflection

This assignment was a good next step and reintroduction to LED's. One problem I ran into with this assignment was that I had put the "liftoff" after the loop but for the LED to turn on when it printed liftoff, I had to put it in a if statement. The if statement says that "if x <= 1:" if x is less than 1 then print liftoff and turn on the blue LED. This was also a good recap for the LED code with the line "ledr = digitalio.DigitalInOut(board.GP15)" and "ledr.direction = digitalio.Direction.OUTPUT" connecting the LED to the ground pin and stating the LED as an output. Overall this was a good and simple assignment that helped me better understand Circuit Python.

## Launchpad Part 3 (button)

### Assignment Description 
For this assignment, we had to make the countdown start when we pressed a button.

### Evidence
![Evidence](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/images/ezgif.com-optimize.gif)

### Wiring

![WIN_20230919_13_27_15_Pro](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/f2468d71-3d93-4913-bd7a-1ddc1d924fd9)


### Coding
[code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Launchpad_Part_3)

### Reflection 
This assignment was a good introduction to buttons and was relatively easy. A couple of necessary lines for the button include "button = digitalio.DigitalInOut(board.GP17)", "button.value =", and "button.pull = digitalio.Pull.DOWN". For the pull-down it means that if the button is pressed the button value equals True and that you need to connect it to the 3v3 pin, the opposite is true for pull up where when the button is pressed it equals false and you need to be connected to GND. Another thing I learned is that to print a button value or read one you have to use the line button.value which seems obvious but I was just setting button = to something and it wasn't working. Overall, this assignment was a good introduction back to buttons.

## Launchpad Part 4 (Servo)

### Assignment Description
For this assignment, we had to make a servo move 180 degrees after it prints liftoff to simulate a launch tower disconnecting

### Evidence 

![Evidence](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/images/ezgif.com-video-to-gif%20(3).gif) 

### Wiring 
![0](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/14deccb5-e756-4d19-aebe-16a47aac0807)

### coding
[code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Launchpad_Part_4)

### Reflection

This assignment was a good intro to motors and libraries. In this assignment, I learned how to import libraries to circuit python, first, you have to download the library bundle and unzip the file (Extract all). Next, you find the library you want, in this case, "adafruit_motor". You then have to import it into the circuit python file in the library folder. I also learn the servo commands you need for circuit python which are pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle =2** 15, frequency = 50), servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500), and servo1.angle = x. The PWMio allows you to control pins with pulse width modulation in this case GP0 and setting the frequency to 50. servo.Servo sets the maximum and minimum pulse of the servo so it does no go further than a certain point. Finally, servo1.angle sets the angle of the servo so if I set x to 180 it would go from whatever angle it's at and go to 180.

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Hyperlink text](http://www.google.com)      

### Test Image
![Volleyball!](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/images/MISC_DETAIL_vs_Tarleton_St_08272021_59912.jpg)  

### Test GIF

![Volleyball](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/images/200w.gif)  

