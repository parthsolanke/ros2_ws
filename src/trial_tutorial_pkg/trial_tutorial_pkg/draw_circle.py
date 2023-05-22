#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    
    def __init__(self):
        super().__init__("trial_tutorial_draw_cicle_node")
        
        # creating and class attribute for command line 
        # the publisher takes 3 args 1st is the msg type
        # 2nd is the topic to publish to 
        # 3rd is the no. of messeges which is ti be sent it acts as a queue buffer to publish msgs to topic
        self.cmd_vel_pub_ = self.create_publisher(Twist , "/turtle1/cmd_vel", 10)
        
        # now here we get the timer to call teh send_velocity_info function and to specify the time interval
        self.timer_ = self.create_timer(0.5, self.send_velocity_info) 
        
        self.get_logger().info("Draw circle node has started\n")
        
    def send_velocity_info(self):
        # specifying the msg type 
        msg = Twist()
        
        # specifying the msg data
        msg.linear.x = 2.0
        msg.angular.z  = 1.0
        
        # now publishing the messege 
        self.cmd_vel_pub_.publish(msg)
        
        # printing the msg
        self.get_logger().info("msg: (linearX = " + f"{msg.linear.x})\n")
        self.get_logger().info("msg: (angularZ = " + f"{msg.linear.z})\n")
        
        
        
def main(args=None):
    # initialised Ros2 communications 
    rclpy.init(args=args)
    
    # initializing node
    node = DrawCircleNode()
    
    # calling the spin function to spin the node 
    rclpy.spin(node)
    
    rclpy.shutdown()