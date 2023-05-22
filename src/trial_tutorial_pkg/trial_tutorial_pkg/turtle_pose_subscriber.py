#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):
    
    def __init__(self):
        super().__init__("pose_subscriber")
        
        # attribute of the calss to act as subscriber to node /turtle1/pose
        # the third parameter is the callback to get the msgs from the topic
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
    
    def pose_callback(self, msg: Pose):
        self.get_logger().info("( x: " + str(msg.x) + ", y: " + str(msg.y) + ")")
        
        

def main(args=None):
    rclpy.init(args=args)
    
    node = PoseSubscriberNode()
    rclpy.spin(node)
    
    rclpy.shutdown()