from resources import CmdArgs, DEBUG_FLAGS
from republish_base import TransformationRepublisherBase
from static_broadcaster import *
import yaml


class YamlTransformationRepublisher(TransformationRepublisherBase):

    def __init__(self, cmd_args: CmdArgs):
        super().__init__(cmd_args)

    def bring_up_publishers(self):
        for broadcaster in self.broadcasters:
            broadcaster.start()
            self.all_subprocesses.append(broadcaster.running_subprocess)

        self.wait_for_broadcasters_to_finish()

    def collect_data(self):
        with open(self.file_path, 'r') as file:
            data = yaml.safe_load(file)

        self.broadcasters = [StaticBroadcaster.from_dict(trans_data) for trans_data in data['transformations']]
        for broadcaster in self.broadcasters:
            broadcaster.metadata.remap_tf_and_tf_static(self.tf, self.tf_static)

