import resources
import sys
from republish_rosbag_transformations import TransformatRepublisher
import os

resources.DEBUG_FLAGS.PRINT_SUBPROCESSES = False

if __name__ == "__main__":
    
    tf_static_topic = ""
    tf_topic = ""
    bag_file_path = ""
    remapping = False
    
    arguments = sys.argv[1:]
    num_args = len(arguments)
    if num_args < 1 or num_args > 3:
        print(resources.USAGE_INFORMATION)
    
    if num_args == 1:
        "Starting publishers without remapping"
    
    elif len(arguments) == 3:
        tf_static_topic = arguments[1]
        tf_topic = arguments[2]
        "Starting publishers with remapping."
        remapping = True
       
    else:
        print(resources.USAGE_INFORMATION)
        
    bag_file_path = arguments[0]

    publisher = TransformatRepublisher(remapping, tf_static_topic, tf_topic)
    
    publisher.dump_csv_data_from_rosbag(bag_file_path, verbose=False)
    publisher.collect_csv_dump()
    publisher.bringup_publishers()
    
    print("Done")

    
    