# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [LED Blink](#led_blink)
* [Launchpad Part 1](#launchpad_part_1_countdown)
* [Launchpad Part 2](#launchpad_part_2_led)
* [Launchpad Part 3](#launchpad_part_3_button)
* [Launchpad Part 4](#launchpad_part_4_servo)
* [Crash Avoidance Part 1](#crash_avoidance_part_1_acceleration)
* [Crash Avoidance Part 2](#crash_avoidance_part_2_light_and_power)
* [Crash Avoidance Part 3](#crash_avoidance_part_3_oled_screen)
* [Beam](beam)
* [Beam Part 3](beam_part_3)
* [Beam Iteration](Beam_Iterations)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## LED_Blink

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

## Launchpad_Part_1_(countdown)

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

## Launchpad_Part_2_(LED)

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

## Launchpad_Part_3_(button)

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

## Launchpad_Part_4_(Servo)

### Assignment Description
For this assignment, we had to make a servo move 180 degrees after it prints liftoff to simulate a launch tower disconnecting

### Evidence 

![Evidence](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/images/ezgif.com-video-to-gif%20(3).gif) 

### Wiring 
![0](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/14deccb5-e756-4d19-aebe-16a47aac0807)

### coding
[code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Launchpad_Part_4)

### Reflection

This assignment was a good intro to motors and libraries. In this assignment, I learned how to import libraries to circuit python, first, you have to download the library bundle and unzip the file (Extract all). Next, you find the library you want, in this case, "adafruit_motor". You then have to import it into the circuit python file in the library folder. I also learned the servo commands you need for circuit python which are pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle =2** 15, frequency = 50), servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500), and servo1.angle = x. The PWMio allows you to control pins with pulse width modulation in this case GP0 and setting the frequency to 50. servo.Servo sets the maximum and minimum pulse of the servo so it does not go further than a certain point. Finally, servo1.angle sets the angle of the servo so if I set x to 180 it would go from whatever angle it's at and go to 180.

## Crash_Avoidance_Part_1_(Acceleration)

### Assignment Description
For this assignment, we had to print out the X, Y, and Z values from where the position the MPU was. 

### Evidence 
![ezgif com-video-to-gif (4)](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/932d6412-8a23-4459-9d42-9078a91d5c87)

### Wiring 

![IMG_20230922_135553](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/abf397f0-9e8f-4d42-b0b9-5c17f5c508b2)

### Coding
[code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_Part_1)

Got help from [Mason Divers](https://github.com/masond552/Engineering_4_Notebook) but he didn't write the code he just helped me write mine

### Reflection 

This assignment was relatively difficult but a good introduction to the MPU. You have to use i2c = busio.I2C(scl_pin, sda_pin) to link the code to the MPU and to assign the SCL and SDA pin you have to use SCL/SDA = board.x. The next line of code is acceleration = mpu.acceleration this just gives a simpler name to the MPU acceleration. The most complicated line of code for this assignment was print(f"acceleration m/s^2- X:{round(acceleration[0],3)} Y:{round(acceleration[1],3)} Z:{round(acceleration[2]),3}" ) this command uses a tuple with the [0],[1],[2] to separate them. The round and ,3 rounds the number to the thousands place so the terminal is more organized. Overall, this assignment was very challenging for me because code is not my strong suit and I did need assistance from Mason.

## Crash_Avoidance_Part_2_(light_and_power)

### Assignment Description
For this assignment, we had to make an LED turn on whenever the MPU was at a 90-degree angle.

### Evidence
![ezgif-1-49c31ba919](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/76985ac5-f7c9-4c36-8c59-14c1c2bf6e75)

### Wiring
![0](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/02bf826b-e833-4a58-a40c-bdbc2d092d77)

### Code
[code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_Part_2)

### Reflection

This assignment was very informative about batteries and not too difficult to work with the LED. For the code, I added onto the previous assignment and all I changed was adding the LED values and a new if and elif statement. For the if statement I used the line if z_acceleration < 0: this states that if the z_acceleration from this line of code, x_acceleration, y_acceleration, z_acceleration = acceleration (defining them to the MPU acceleration) is less than 0 then turn the LED on. This works because when the value is negative the MPU is turned 90 degrees or more and only not when it's facing upright. The elif statement (elif z_acceleration > 0:) says that when the value of z is positive or level then turn the LED off or else the LED will stay on forever. For the battery, no code is needed and we were given how to wire it to GND and the VSYS pin. Overall, this assignment was fairly simple but was a good introduction to the battery and helped me to understand tuples better. 

## Crash_Avoidance_Part_3_(OLED_Screen)

### Assignment Description
For this assignment, we had to print the X, Y, and Z angular velocities to an OLED screen and round to the 3rd decimal point. It also had to be powered by a battery and have an LED that turns on at 90 degrees.

### Evidence
![ezgif-1-88ec2a6e88](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/9b8b4aa4-f677-4c16-b8c0-17847d3cdbd6)

### Wiring 
![IMG_20231017_141925](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/5c508ecd-3be2-48ac-a444-d3e5cd3f63d8)

### Code
[Code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_Part_3)
*From [Mason Divers](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_OLED.py)*

### Reflection
This assignment was challenging for me and I didn't have time to finish the code so I used Masons. I do understand some lines of code, however, like text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5) which assigns the position, font, and color of the text on the OLED. These 2 lines of code, angular_velocity = mpu.gyro and x_angular_velocity, y_angular_velocity, z_angular_velocity = angular_velocity makes it read the angular velocity and assign the angular velocity and the x, y, and z values. Finally, angular_velocity_text = f"X: {x_angular_velocity:.3f},\n Y: {y_angular_velocity:.3f},\n Z: {z_angular_velocity:.3f}", led_status = "LED Status: ON" if led.value else "LED Status: OFF", and text_area.text = angular_velocity_text + "\n" + led_status are commands to print the angular velocity and LED status onto the OLED. Also to avoid OLED flickering you have to use a time.sleep(0.1). Overall, it is too bad I couldn't get to finish this assignment but it was a good lesson on time management especially since I'm not the best at code but I still learned a little bit from the assignment. 


&nbsp;

## Onshape_Assignment_Template

## Beam 

### Assignment Description
This assignment explores engineering tradeoffs by designing a 3D-printed beam to maximize load-bearing capacity while adhering to specific constraints. The goal is to create a beam that avoids breaking or excessive bending(beyond 35mm) and satisfies the following requirements:


* Ensure full engagement with the holder. 
* Follow the example eye bolt mounting geometry. 
* Place the eyebolt hole's center 180 mm from the attachment block's front face. 
* Prevent any part of the beam from extending below the attachment block. 
* Maintain vertical angles >= 45 degrees relative to the horizontal plane. 
* Use PLA material. 
* Keep the entire beam, including the attachment block, under 13 grams in weight.

### Part Link 
[Onshape](https://cvilleschools.onshape.com/documents/dd59f389e3f75e6c83491e1b/w/01511871c7c3bde9b77a0bbb/e/06a6eb71a015865d3f97e651)

### Part Image

![Beam Starter + Holder Copy 1 (1)](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/766cf5b4-94f9-42e1-afa2-e64d0952e2ba)
![Beam Starter + Holder Copy 1](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/f180a9b1-f98f-467f-bd19-60019194ef5e)


### Reflection

This assignment was very fun and challenging for us. We took inspiration on this design from the I beam which is the strongest beam so we wanted to incorporate it into our design. The problem with the I beam was that it had too much of an overhang so we redesigned it as a Y beam for support. Another issue we ran into was having too much weight, in the beginning the beam was very solid but it had way too much weight. For the cut down we had to add several circles and rectangular holes which affected the stability of the beam. My advice is for next time to create a little simpler design to avoid all the holes that we had to put, although I think our Y beam design was sturdy.

## Beam_Part_3 
![Assembly 1 (2)](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/52434908-00ab-4d5e-bc0c-1c5b10ab8dfd)

![Assembly 1](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/b75d61dd-dec5-4f03-b979-d2e7e029005f)
*Deformation scale = 1*

Our beam did well against the FEA but there is definitely room for improvement. In the base of our beam the bottom as well as the top are under pressure and it would snap there. The problem is the sharp corners and lack of materials, we are going to fix it by adding fillets and slimming it down to bulk up certain parts. Another problem we faced was the stress of the line of circles because they are too close together. 

# Beam_Iterations 

![part 4 vonmises](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/14de4e65-28d1-414e-98be-78cb9bd7102c)

Our original design needed a lot of work and was complicated to fix but we made it a lot better based on FEA. One problem we noticed with our original design was that it was very frail on the bottom so we added fillets to the base corner to help with strength. Another problem was the bend on the top of the beam so we added support beams going horizontal on the top to reduce stress. Finally, the first bracket from the holder had the most stress, to fix this we added more fillets to create strength and get rid of a hard edge. 

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Hyperlink text](http://www.google.com)      

### Test Image
![Volleyball!](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/images/MISC_DETAIL_vs_Tarleton_St_08272021_59912.jpg)  

### Test GIF

![Volleyball](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/images/200w.gif)  

