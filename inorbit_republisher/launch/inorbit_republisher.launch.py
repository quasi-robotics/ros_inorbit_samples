# Copyright (C) 2026 Quasi, Inc. All Rights Reserved.

import os

import launch
import lifecycle_msgs.msg
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, RegisterEventHandler, EmitEvent
from launch.event_handlers import OnShutdown
from launch.events import matches_action
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.event_handlers import OnStateTransition
from launch_ros.actions import Node, LifecycleNode
from launch_ros.events.lifecycle import matches_node_name, ChangeState

def generate_launch_description():

    return LaunchDescription([

        Node(
            name='inorbit_republisher',
            package='inorbit_republisher',
            executable='republisher',
            output='screen',
            arguments=['--ros-args', '--disable-rosout-logs', '--disable-external-lib-logs'],
            parameters=[{'config': launch.substitutions.PathJoinSubstitution([get_package_share_directory('inorbit_republisher'), 'config', 'inorbit_republisher.yaml'])}],
        ),

    ])
