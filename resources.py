import os
from pathlib import Path


class DebugFlags:
    PRINT_SUBPROCESSES = False
    VERBOSE_OUTPUT = False

DEBUG_FLAGS = DebugFlags


def _path_to_project_root(project_name):
    path = os.getcwd()
    while not str(path).endswith(project_name):
        path = Path(path).parent

    return path


PATH_ROOT = Path(os.getcwd())
PATH_DATA = PATH_ROOT / 'data'

PATH_CSV_DUMP_FILE = PATH_DATA / 'dump.csv'

USAGE_INFORMATION_REPUBLISH = "[abs/path/to/bagfile] [tf_static topic] [tf topic]"

USAGE_INFORMATION_NORMAL = "[abs/path/to/bagfile]"

USAGE_INFORMATION = "Wrong number of arguments!.\nRun this script either without tf topic info:\n{} or with both tf republish informations supplied.\n{}".format(
    USAGE_INFORMATION_NORMAL, USAGE_INFORMATION_REPUBLISH)


class CmdArgs:

    def __init__(self):
        self.tf_topic = ""
        self.tf_static_topic = ""
        self.file_path = ""
        self.remapping = False
