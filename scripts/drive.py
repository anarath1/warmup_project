#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist, Vector3

class DriveSquare(object):
    def __init__(self):
        # initialize the ROS node
        rospy.init_node('drive_square')
        # setup publisher to the cmd_vel ROS topic
        self.robot_movement_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    def run(self):
        # setup the Twist message we want to send

        #move forward for 5 seconds 
        fwd_twist = Twist(
            linear=Vector3(0.1, 0, 0),
            angular=Vector3(0, 0, 0.25)
        )

#        rospy.sleep(5)

        #turn 

        turn_twist = Twist(
            linear=Vector3(0, 0, 0),
            angular=Vector3(0, 0, 0.2)
        )

 #       rospy.sleep(4)

        for i in range(4):
            fwd_twist()
            rospy.sleep(4)
            turn_twist()
            rospy.sleep(5)



        # publish the message
        self.robot_movement_pub.publish(my_twist)

if __name__ == '__main__':
    # instantiate the ROS node and run it
    node = DriveSquare()
    node.run()
