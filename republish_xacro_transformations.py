from republish_base import TransformationRepublisherBase
from resources import CmdArgs


def collect_transformations_from_xacro(xacro_file_path):
    print("Collecting transformations from: {}".format(xacro_file_path))

#TODO is this easily possible?
class XacroTransformationRepublisher(TransformationRepublisherBase):

    def __init__(self, cmd_args: CmdArgs):
        super().__init__(cmd_args)

    def collect_data(self):
        collect_transformations_from_xacro(self.file_path)

    def bring_up_publishers(self):
        print("Bringing up publishers")
