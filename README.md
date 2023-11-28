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
* [Landing Area Part 1](#Landing_Area_Part_1_Functions)
* [Landing Area Part 2](#Landing_area_part_2_plotting)
* [Morse Code Part 1](#Morse_code_part_1_translation)
* [Morse Code Part 2](#Morse_code_part_2_transmission)
* [Beam](#beam)
* [Beam Part 3](#beam_part_3)
* [Beam Iteration](#beam_iterations)
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
We were assigned to make a countdown from 10 in the terminal and when it gets to 1 it prints "Liftoff".

### Evidence 
![ezgif-4-5c041d7028](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/6c06b48a-1de6-400c-8a44-48039b61105d)

### Wiring
No wiring

### Code
[code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Laucnhpad_Part_1)

### Reflection

This assignment was simple and informative for using Pico and the terminal. I learned that to run in Pico you have to click on the code then save (CTR s) and to run you click (CTR d), I was a little confused because I was pressing F5 to run it and it directed me to the circuit python terminal instead of the pico one. 1 piece of code I learned was the range line (for x in range(0,0,0):) I used this line to set the constraints for the countdown (1-10). So for the first blank, you put in the number  you want to start with like 10, for the second blank you want to put in the number 1 less than the one you want it to stop at, so if I wanted to stop it at 1 I would put 0 so it would look like for x in range(10,0,-1):. Finally, for the last one, it is the number from which you want to count up or down so I wanted to count by 1 so I had to put -1 and if you don't put anything in the blank it will count up from 1. Overall this assignment wasn't too difficult and has a good explanation of what the range command did.

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

This assignment was a good next step and reintroduction to LED's for me. One problem I ran into with this assignment was that I had put the "liftoff" after the loop but for the LED to turn on when it printed liftoff, I had to put it in an if statement. The if statement says that "if x <= 1:" if x is less than or equal to 1 then print liftoff and turn on the blue LED. This was also a good recap for the LED code with the line "ledr = digitalio.DigitalInOut(board.GP15)" and "ledr.direction = digitalio.Direction.OUTPUT" connecting the LED to the ground pin and stating the LED as an output. Overall this was a good and simple assignment that helped me better understand Circuit Python.

## Launchpad_Part_3_(button)

### Assignment Description 
For this assignment, we had to make the previous countdown requirements start when we pressed a button.

### Evidence
![Evidence](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/images/ezgif.com-optimize.gif)

### Wiring

![WIN_20230919_13_27_15_Pro](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/f2468d71-3d93-4913-bd7a-1ddc1d924fd9)


### Coding
[code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Launchpad_Part_3)

### Reflection 
This assignment was a good reintroduction to buttons and was relatively easy. A couple of necessary lines for the button include "button = digitalio.DigitalInOut(board.GP17)", "button.value =", and "button.pull = digitalio.Pull.DOWN". For the pull-down it means that if the button is pressed the button value equals True and that you need to connect it to the 3v3 pin, the opposite is true for pull up where when the button is pressed it equals False and you need to be connected to GND. Another thing I learned is that to print a button value or read one you have to use the line button.value which seems obvious but I was just setting button = to something and it wasn't working. Overall, this assignment helped my understanding of buttons.

## Launchpad_Part_4_(Servo)

### Assignment Description
For this assignment, we had to make a servo move 180 degrees after it the terminal prints liftoff to simulate a launch tower disconnecting from a rocket.

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
For this assignment, we had to print out the X, Y, and Z values from where the position of the MPU was. 

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

## Landing_Area_Part_1_(Functions)

### Assignment Description
For this assignment, we had to write code to calculate the area of a triangle given 3 coordinates. We also had to use a function to determine the triangle area and print an error code when letters or improper format are put into the coordinates. 

### Evidence
![ezgif-5-b6aa16a8f6](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/95e079a0-125c-4992-91f4-c59ce1418262)

### Wiring
No Wiring.

### Code
[Code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Landing_Area_Part_1)
*help from [Mason Divers](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Landing_Area_Pt1_Functions.py)*

### Reflection
This assignment was very difficult for me since it incorporated math and code, and I'm ok at math but not so good at code. I had to look at Masons code to fully understand the code (I asked his permission) which helped me a lot to understand some of the code. For example, I learned that "def calculate_triangle_area(x1,y1,x2,y2,x3,y3):" defines the variables used for the calculation of the triangle. Another line is "return abs((.5) * ((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))))" which calculates the area of the triangle with the inputted points using a math equation. The line "x1,y1 = map(float, input("enter the first coordinated (x,y):").split(","))" defines the x1 and y1 as an input for these coordinates and splits them at the comma for the input syntax. Another line " x1,y1, x2,y2, x3,y3 = triangle_area()" identifies the variables as part of the triangle area. Next, "  if (x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))!=0: " checks if the points given make a valid triangle plugging them into the equation. Finally, If it's valid it prints the area and coordinates, and if not it prints an error. 

## Landing_Area_Part_2_(Plotting)

### Assignment Description 

For this assignment, we had to make a triangle print to the OLED screen as well as find the area given 3 points. We also had to print the triangle relative to a base location.

### Evidence

![IMG_20231108_135331](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/e264a20d-ca97-49f3-9eeb-3ce9502f4908)

### Wiring

![IMG_20231017_141925](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/5c508ecd-3be2-48ac-a444-d3e5cd3f63d8)
 
 *Same as Crash Avoidance Part 3 (OLED)*

### Code

[Code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Landing_Area_Part_2) 

*Code from [Mason Divers](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Landing_Area_Pt2_Plotting.py) (same code different commenting)*

### Reflection

This assignment was very challenging for me and I had to use Mason's code (with permission). However, I did try to comprehend the code that I used, for example, the lines "origin_x = 64" and "origin_y = 32" set the coordinate for the origin on the OLED screen because the point 0,0 would be in the top left corner of the OLED and not the middle. Another line of code is "def draw_line(x1, y1, x2, y2, color=0xFFFF00):" this creates a function with the variables x1,y1,x2, and y2 and sets the color of the line. The next line of code in this function is "line = Line(int(x1), int(y1), int(x2), int(y2), color=color)," this defines the line and its integers of x1&2 and y1&2 and also uses the color line to create a white line. For this function its, "def draw_triangle(x1, y1, x2, y2, x3, y3, origin_x, origin_y):" which defines how to draw the triangle including the variables x1&2, y1&2, and the origins. Next, "triangle = Triangle(int(origin_x + x1), int(origin_y - y1)," defines the triangle with how to place the points of input by displacing them with addition, from the origin (there is more with x2&3 and y2&3 but it would take up space). Finally, in the while true the lines, "splash.append(draw_triangle(x1, y1, x2, y2, x3, y3, origin_x, origin_y))" and "splash.append(draw_circle(origin_x, origin_y, 2))" and "splash.append(draw_line(0, 32, 128, 32))" which draws the triangle, circle, and axes using the functions. Overall, this assignment made me more aware of the math that is needed in code and OLED screens.

## Morse_Code_Part_1_(Translation)

### Assignment Description

For this assignment, we had to make a translator to Morse code and make it quit when we put in "-q". We also had to make the spaces between the words a slash. 

### Evidence

![ezgif-4-ba0309d29c](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/c7651c3d-772e-45bc-8b06-3b787cbfd0d1)

### Wiring
*No wiring*

### Code

[Code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Morse_Code_Part_1)

*code from [online](https://codepal.ai/code-generator/query/9UmXp1um/python-translate-text-to-morse-code) (but I wrote half of it) help from [Mason Divers](https://github.com/MasonD552/Engineering_4_Notebook) and [Paul Weder](https://github.com/Pweder69/Engineering_4_Notebook)*

### Reflection

This assignment was difficult for me and took me a long time. At first, I tried to write the code myself but later I looked online for examples of the translator to help me. I landed on a website called codepal which is linked here [codepal](https://codepal.ai/code-generator/query/9UmXp1um/python-translate-text-to-morse-code) which looking back wasn't the best code because it was overcomplicated but helped me to complete the assignment. The next thing I moved onto in the assignment was making the code not print when I entered -q. To do this I made a while True and defined text as "text = input("Enter Morse message:")" which makes text the user input. Then I plugged text into the translator function with "morse_code = translator.translate_to_morse(text)" which translates the input. Now for the -q system, I made the if statement, "if text == "-q":" followed by -q which quits it. Finally, I made the print function for normal printing which is "else: print(f"Morse Code: {morse_code}")" which says that if text doesn't equal q then print the translation. Also, for the translation, a necessary line of code is "text = text.upper()" which makes all input text uppercase so it matches with the all-capital Morse dictionary. Another if statement is "  if text == "":" then " morse_code += "/"" this is the if statement that makes spaces slashes between words by saying that if there is a space print a /.

## Morse_Code_Part_2_(Transmission)

### Assignment Description
For this assignment, we had to make an LED blink to convey a message input by blinking fast for a dot, longer for a dash, and turning off for a space.

### Evidence 
![ezgif-1-ac2fe8e961](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/8270a8d4-9d91-4174-a2bd-f454194b812d)

### Wiring

![268067110-a741c193-4b99-4aba-8f90-9eeb1544838d](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/d71fd61e-d5c2-4b10-9ed2-cd2d4b2d6161)

### Code

[code](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/raspberry-pi/Morse_Code_Part_2)

### Reflection 

This assignment was fun and not so challenging after completing the first one. Some very important lines of code are " modifier = 0.25, dot_time = 1*modifier, dash_time = 3*modifier
between_taps = 1*modifier" etc. These lines set the time necessary for the LED to be on or off for the different variables of the morse code, this is useful because you don't have to come up with the time.sleeps to make the LED blink or stay on for longer. For reading the morse code message you need the line "for character in morse_code:" which is given in the assignment. Next, the line " if character == ".":" is saying if the morse message has a dot in it to blink the led with the lines "ledr.value = True, time.sleep(dot_time), ledr.value = False, time.sleep(between_taps)" the time.sleep(dot_time) uses the variable from before so the led stays on for the right amount of time. You then repeat these lines of code for the "-" and the " " so the led blinks accordingly. Overall, this assignment helped me better understand LEDs and Morse code as well as user input. 


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

## Beam_Iterations 

![part 4 vonmises](https://github.com/Jpark27614/Engineering_4_Notebook/assets/113122312/14de4e65-28d1-414e-98be-78cb9bd7102c)

Our original design needed a lot of work and was complicated to fix but we made it a lot better based on FEA. One problem we noticed with our original design was that it was very frail on the bottom so we added fillets to the base corner to help with strength. Another problem was the bend on the top of the beam so we added support beams going horizontal on the top to reduce stress. Additionally, on the first design, we had a lot of overhang at the top of the Y beam which we were confused by because the angle was 45 but the holes were well over. Finally, the first bracket from the holder had the most stress, to fix this we added more fillets to create strength and get rid of a hard edge. 

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Hyperlink text](http://www.google.com)      

### Test Image
![Volleyball!](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/images/MISC_DETAIL_vs_Tarleton_St_08272021_59912.jpg)  

### Test GIF

![Volleyball](https://github.com/Jpark27614/Engineering_4_Notebook/blob/main/images/200w.gif)  

