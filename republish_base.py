import os.path
import sys
from abc import ABC, abstractmethod
from resources import CmdArgs


class TransformationRepublisherBase(ABC):

    def __init__(self, cmd_args: CmdArgs):
        self.remap = cmd_args.remapping
        self.tf_static = cmd_args.tf_static_topic
        self.tf = cmd_args.tf_topic
        self.file_path = cmd_args.file_path

        self.all_subprocesses = []

    @abstractmethod
    def collect_data(self):
        pass

    @abstractmethod
    def bring_up_publishers(self):
        pass

    def wait_for_broadcasters_to_finish(self):
        for process in self.all_subprocesses:
            if process is None:
                continue

            process.wait()
