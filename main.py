import resources
from resources import CmdArgs
import sys
from create_publisher import create_publisher
import os

resources.DEBUG_FLAGS.PRINT_SUBPROCESSES = False
resources.DEBUG_FLAGS.VERBOSE_OUTPUT = False

if __name__ == "__main__":

    args = CmdArgs()

    arguments = sys.argv[1:]
    num_args = len(arguments)
    if num_args < 1 or num_args > 3:
        print(resources.USAGE_INFORMATION)
        sys.exit(-1)

    if num_args == 1:
        "Starting publishers without remapping"

    elif len(arguments) == 3:
        args.tf_static_topic = arguments[1]
        args.tf_topic = arguments[2]
        "Starting publishers with remapping."
        args.remapping = True

    else:
        print(resources.USAGE_INFORMATION)

    args.file_path = arguments[0]

    publisher = create_publisher(args)
    publisher.collect_data()
    publisher.bring_up_publishers()

    print("Done")
