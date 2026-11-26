import rclpy
from rclpy.node import Node
from std_msgs.msg import Person

rclpy.init()
node = Node("listener")

def cb(msg):
    node.get_logger().info("Listen: %s" % msg)

def main():
    sub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)
