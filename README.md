# warmup_proje

Drive in a square:
A high-level description (a few sentences): Describe the problem and your approach at a high-level. Include any relevant diagrams or pictures that help to explain your approach.
The problem was to make the robot drive in a square. My approach was the time approach where I made the robot drive straight for a couple seconds, then turn 90 degrees and repeat this 4 times to drive in a square. I tweaked the amount of time I let the robot sleep for (to let it drive straight) based on visualization. I also tweaked the amount to turn it by based on visualization. 

Code explanation (a couple of sentences per function): Describe the structure of your code. For the functions you wrote, describe what each of them does.

The forward twist function makes the robot move forward. 
Then it sleeps for 4 seconds. 
The turn twist function makes the robot move 90 derees. 
Then it sleeps for 5 seconds. 
This is in a loop to complete the square. 

Challenges: An evident challenge for me was figuring out gazebo since I was doing everything in simulation. I think also just understanding the different ros functions and how to use ros was a big challenge. 

Future work: I would complete the other behaviors if I have more time, but I think completing the drive in a square and submitting it makes the most sense for me right now, because the more time I spend on this, the more behind I will get in the particle filter project.

Takeaways: Working in simulation is very different from working on the physical turtlebot and while some things may work in simulation the same won’t work on the physical bot (as expected). So to work in simulation keeping in mind if everything works in gazebo it doesn’t mean everything will actually work on the bot. 
Knowing what you want the robot to do wasn’t the hard part, but rather going through the ros commands and doing them in the correct order, and doing the object-oriented part of the programming was the hard part. 





