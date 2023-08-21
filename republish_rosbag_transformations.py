import csv
import subprocess
import resources
from resources import CmdArgs, DEBUG_FLAGS
from republish_base import TransformationRepublisherBase
from pathlib import Path
from static_broadcaster import StaticBroadcaster
import glob
# Grepros is a cmd line tool. but we still depend on it. therefore we include it here so it is added to the requiremens.txt
import grepros


def _dump_csv_data_from_rosbag(bag_file_path):
    verbose_flag = ""
    if not DEBUG_FLAGS.VERBOSE_OUTPUT:
        verbose_flag = "--no-console-output"
    grepros_cmd = 'grepros {} --filename {} --topic "*/tf_static" --no-filename --write "{}"'.format(verbose_flag,
                                                                                                     bag_file_path,
                                                                                                     str(resources.PATH_CSV_DUMP_FILE))
    subprocess.run(['bash', '-c', grepros_cmd])


class RosBagTransformationRepublisher(TransformationRepublisherBase):

    def __init__(self, cmd_args: CmdArgs):
        super().__init__(cmd_args)

    def start_static_tf_publishers(self, row, group):
        broadcasters = StaticBroadcaster(self.remap)
        broadcasters.metadata.remap_tf_and_tf_static(self.tf_static, self.tf)
        broadcasters.metadata.parent_link = row[group[1]]
        broadcasters.metadata.child_link = row[group[2]]
        broadcasters.translation.set(row[group[3]], row[group[4]], row[group[5]])

        broadcasters.rotation.set_from_quaternion(row[group[6]], row[group[7]], row[group[8]], row[group[9]])
        broadcasters.start()
        return broadcasters.running_subprocess

    def collect_csv_dump(self):

        search_path = str(resources.PATH_DATA) + "/*"
        dump_files = glob.glob(search_path)
        self.dump_path = dump_files[0]

        with open(str(self.dump_path), 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)[3:]

        self.tf_static_groups = {}

        for header in headers:
            header_parts = header.split('.')
            assert (len(header_parts) >= 2)

            group_number = header_parts[1]
            group = self.tf_static_groups.get(group_number, [])
            group.append(header)
            self.tf_static_groups[group_number] = group

    def collect_data(self):
        _dump_csv_data_from_rosbag(self.file_path)
        self.collect_csv_dump()

    def bring_up_publishers(self):

        self.all_subprocesses = []

        with open(str(self.dump_path), 'r') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for row in dict_reader:
                for transform_id in self.tf_static_groups.keys():
                    keys = self.tf_static_groups[transform_id]
                    proc = self.start_static_tf_publishers(row, keys)
                    self.all_subprocesses.append(proc)

        self.wait_for_broadcasters_to_finish()
