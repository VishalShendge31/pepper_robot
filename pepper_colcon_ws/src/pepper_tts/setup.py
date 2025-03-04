from setuptools import find_packages, setup

package_name = 'pepper_tts'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pepper',
    maintainer_email='shendge.vishal.vilas@gmail.com',
    description='Pepper Text-to-Speech ROS2 Package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'tts_node = pepper_tts.tts_node:main',
        ],
    },
)
