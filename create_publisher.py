import os
import sys
from resources import CmdArgs
from republish_rosbag_transformations import RosBagTransformationRepublisher
from republish_xacro_transformations import XacroTransformationRepublisher
from republish_from_yaml import YamlTransformationRepublisher
from republish_base import TransformationRepublisherBase


def _get_file_ending(file_path):
    _, ext = os.path.splitext(file_path)
    return ext


def _is_ros2_bag(file_path):
    ext = _get_file_ending(file_path)
    return ext == '.db3'


def _is_xacro_file(file_path):
    ext = _get_file_ending(file_path)
    return ext == '.xacro'


def _is_yaml_file(file_path):
    ext = _get_file_ending(file_path)
    return ext == '.yaml'


def create_publisher(cmd_args: CmdArgs) -> TransformationRepublisherBase:
    if _is_ros2_bag(cmd_args.file_path):
        print("Starting ros-bag republishing.")
        return RosBagTransformationRepublisher(cmd_args)
    elif _is_xacro_file(cmd_args.file_path):
        print("Starting xacro-file republishing.")
        return XacroTransformationRepublisher(cmd_args)
    elif _is_yaml_file(cmd_args.file_path):
        print("Starting yaml-file republishing.")
        return YamlTransformationRepublisher(cmd_args)
    else:
        print("An unsupported file was provided: {} \n Shutting down.".format(cmd_args.file_path))
        sys.exit(-1)
