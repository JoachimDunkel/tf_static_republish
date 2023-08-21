import os.path
import sys
from abc import ABC, abstractmethod
from resources import CmdArgs


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
