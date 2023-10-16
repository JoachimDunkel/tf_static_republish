# tf_static_republish

## Overview

Easily republish tf_static transformations from an existing ros2 - bag file

Additionally it is possible  to define topic remappings.

## Setup

Put the project wherever you want.
If you want to use it from everywhere it should probably be in /usr/bin?

`pip install -r requirements.txt`

## Example usages

There are two options:

### Republish static_tf from a ros2 bag (.db3 file)

```bash
python3 <abs_path>/tf_static_republish/main.py 
<abs_path>/rosbag2_example.db3 
```

### Republish static_tf from a .yaml file

`data/trans_example_data.yaml` provides an example how static transformations can be created manually and used for republishing static transformations.

```bash
python3 <abs_path>/tf_static_republish/main.py 
<abs_path>/data/example_trans.yaml 
```

### Republishing tf-topics

All commands (above) expect either only 1 argument ( a file ), or 3 arguments
( a file ) and both tf-republishing topics. So they can be called either with:


`file_path`

or

`file_path` `<tf_static_republish_topic>` `<tf_republish_topic>`

If tf-republishing topics are specified the internal started static_tf_republisher will be called with following flags:

--ros-args --remap tf:=<tf_static_republish_topic> --remap tf_static:=<tf_republish_topic>


## Future features?

Parsing transformations directly from a `.xacro` could be usefull but was not implemented yet, because that would require extensive file parsing and generalizing it is not straight forward, feel free to contribute.
