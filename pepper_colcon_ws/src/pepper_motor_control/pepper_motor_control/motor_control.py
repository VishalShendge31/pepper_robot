import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty, SetBool

class PepperMotorControl(Node):
    def __init__(self):
        super().__init__('pepper_motor_control')
        
        # Service clients
        self.wakeup_client = self.create_client(Empty, '/naoqi_driver/wakeup')
        self.enable_motor_client = self.create_client(SetBool, '/naoqi_driver/motion/enable')
        
        # Wait for services
        while not self.wakeup_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Wakeup service not available, waiting...')
        while not self.enable_motor_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Motor enable service not available, waiting...')

    def wake_up(self):
        req = Empty.Request()
        future = self.wakeup_client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info('Wakeup successful!')
        else:
            self.get_logger().error('Wakeup failed!')

    def enable_motors(self, enable=True):
        req = SetBool.Request()
        req.data = enable
        future = self.enable_motor_client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info(f'Motors {"enabled" if enable else "disabled"} successfully!')
        else:
            self.get_logger().error('Motor control failed!')

def main(args=None):
    rclpy.init(args=args)
    controller = PepperMotorControl()
    
    try:
        # Wake up Pepper
        controller.wake_up()
        
        # Enable motors
        controller.enable_motors(True)
        
        # Keep node alive for 2 seconds
        start_time = controller.get_clock().now()
        while (controller.get_clock().now() - start_time).nanoseconds < 2e9:
            rclpy.spin_once(controller)
            
    except KeyboardInterrupt:
        pass
    finally:
        controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
