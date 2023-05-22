#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# creating a class for the node which will be inherited from the 'Node' in rclpy
class MyNode(Node):
    # isnitializing constructor
    def __init__(self):
        # name of the node which will appear while running this node
        super().__init__("trial_tutorial_talker_node")
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)
        
    def timer_callback(self):
        self.get_logger().info("Hello: " + f"[{str(self.counter_)}]")
        self.counter_ += 1
        
def main(args=None):
    # initialised Ros2 communications 
    rclpy.init(args=args)
    
    # here we will create node
    node = MyNode()
    
    # spin function keeps node running till you kill it
    rclpy.spin(node)
    
    # here it will shutdown the node and comunications
    rclpy.shutdown()

if __name__ == '__main__':
    main()
 