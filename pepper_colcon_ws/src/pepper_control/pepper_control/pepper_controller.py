#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class PepperController(Node):
    def __init__(self):
        super().__init__('pepper_controller')
        # Publisher on the /cmd_vel topic
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        # Subscriber to get odometry data
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        
        # Timer to publish commands at a fixed rate (e.g., 10 Hz)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Initialize variables
        self.start_position = None
        self.distance_traveled = 0.0
        self.goal_distance = 1.0  # Target distance in meters
        self.get_logger().info("Pepper controller node started.")

    def odom_callback(self, msg):
        """Callback to get current position from odometry."""
        if self.start_position is None:
            self.start_position = msg.pose.pose.position
        else:
            current_position = msg.pose.pose.position
            dx = current_position.x - self.start_position.x
            dy = current_position.y - self.start_position.y
            self.distance_traveled = math.sqrt(dx**2 + dy**2)
            self.get_logger().info(f"Distance traveled: {self.distance_traveled:.2f} meters")

    def timer_callback(self):
        """Control robot to move forward until 1 meter is traveled."""
        msg = Twist()

        # Move forward at 0.2 m/s
        if self.distance_traveled < self.goal_distance:
            msg.linear.x = 0.2
        else:
            msg.linear.x = 0.0  # Stop after 1 meter
            self.get_logger().info("Goal reached. Stopping the robot.")

        msg.angular.z = 0.0  # No rotation
        self.cmd_vel_pub.publish(msg)

        self.get_logger().info(
            f"Published cmd_vel: linear.x = {msg.linear.x:.2f}, angular.z = {msg.angular.z:.2f}"
        )

def main(args=None):
    rclpy.init(args=args)
    node = PepperController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

