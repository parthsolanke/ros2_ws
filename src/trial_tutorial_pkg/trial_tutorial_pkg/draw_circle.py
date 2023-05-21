#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    
    def __init__(self):
        super.__init__("draw cicle")
        
        # creating and class attribute for command line 
        # the publisher takes 3 args 1st is the msg type
        # 2nd is the topic to publish to 
        # 3rd is the no. of messeges which is ti be sent it acts as a queue buffer to publish msgs to topic
        self.cmd_vel_pub_ = self.create_publisher(Twist , "/turtle1/cmd_vel", 10)
        
        self.get_logger().info("Draw circle node has started")
        
    def send_velocity_info(self):
        
        
        
def main(args=None):
    # initialised Ros2 communications 
    rclpy.init(args=args)
    
    rclpy.shutdown()