from setuptools import setup
import os
from glob import glob

package_name = 'inorbit_republisher'

setup(
    name=package_name,
    version='0.4.2',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/inorbit_republisher.launch.py']),
        ('share/' + package_name + '/config', ['config/inorbit_republisher.yaml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='InOrbit',
    maintainer_email='support@inorbit.ai',
    description='ROS2 to InOrbit topic republisher',
    license='MIT',
    entry_points={
        'console_scripts': [
            'republisher = inorbit_republisher.republisher:main'
        ],
    },
)