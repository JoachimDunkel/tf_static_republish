import os.path
import sys
from abc import ABC, abstractmethod
from resources import CmdArgs
from republish_rosbag_transformations import RosBagTransformationRepublisher
from republish_xacro_transformations import XacroTransformationRepublisher


class TransformationRepublisherBase(ABC):

    # TODO use cmd_args directly.
    def __init__(self, cmd_args: CmdArgs):
        self.remap = cmd_args.remapping
        self.tf_static = cmd_args.tf_static_topic
        self.tf = cmd_args.tf_topic
        self.file_path = cmd_args.file_path

    @abstractmethod
    def collect_data(self):
        pass

    @abstractmethod
    def bring_up_publishers(self):
        pass


def _get_file_ending(file_path):
    _, ext = os.path.splitext(file_path)
    return ext


def _is_ros2_bag(file_path):
    ext = _get_file_ending(file_path)
    return ext == '.db3'


def _is_xacro_file(file_path):
    ext = _get_file_ending(file_path)
    return ext == '.xacro'


def create_publisher(cmd_args: CmdArgs) -> TransformationRepublisherBase:

    if _is_ros2_bag(cmd_args.file_path):
        print("Starting ros-bag republishing.")
        return RosBagTransformationRepublisher(cmd_args)
    elif _is_xacro_file(cmd_args.file_path):
        print("Starting xacro-file republishing.")
        return XacroTransformationRepublisher(cmd_args)
    else:
        print("An unsupported file was provided: {} \n Shutting down.".format(cmd_args.file_path))
        sys.exit(-1)
