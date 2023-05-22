#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

# this code contains a closed loop architecture of subcriber and publisher 

class TurtlesimControllerNode(Node):
    
    def __init__(self):
        super().__init__("Turtlesim_controller")
        self.get_logger().info("Turtlesim controller has started. ")
        
        # creating a publisher to the topic "/turtle1/cmd_vel" to publish comands to that topic
        self.cmd_vel_pub_ = self.create_publisher(Twist , "/turtle1/cmd_vel", 10)
        
        # creating a subscriber to the "/turtle1/pose" topic to get positional data from that topic
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
    
    def pose_callback(self, pose: Pose):
        cmd = Twist()
        
        # creating an if condition to check if th eturtle is closer to the boundries
        # if the turtle is cvloser to th eboundries then turning by updating the z angular velocity
        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 2.0
            cmd.angular.z = 0.5
        # or else going straight    
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        
        # now publishing the msg to the topic "/turtle/cmd_vel" via node cmd_vel_pub_
        self.cmd_vel_pub_.publish(cmd)  
            
        

def main(args=None):
    rclpy.init(args=args)
    
    node = TurtlesimControllerNode()
    rclpy.spin(node)
    
    rclpy.shutdown