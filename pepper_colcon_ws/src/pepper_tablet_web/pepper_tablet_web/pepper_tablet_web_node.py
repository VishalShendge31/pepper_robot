import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Change this if using custom message

class PepperTTS(Node):
    def __init__(self):
        super().__init__('pepper_tts')
        self.publisher = self.create_publisher(
            String,  # Change to naoqi_bridge_msgs.msg.Speech if needed
            '/speech',
            10
        )
        self.get_logger().info('Pepper TTS node initialized')

    def say_text(self, text):
        msg = String()
        msg.data = text
        self.publisher.publish(msg)
        self.get_logger().info(f'Sent to Pepper: "{text}"')

def main(args=None):
    rclpy.init(args=args)
    tts_node = PepperTTS()
    
    # Example usage
    tts_node.say_text("Hello from ROS 2 Humble!")
    
    try:
        rclpy.spin(tts_node)
    except KeyboardInterrupt:
        tts_node.get_logger().info('Shutting down TTS node')
    finally:
        tts_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
