import subprocess
from util import *
import resources


class Translation:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def set(self, x: str, y: str, z: str):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def to_string(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)


class Rotation:
    def __init__(self):
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0

    def set(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set_from_quaternion(self, x: str, y: str, z: str, w: str):
        self.roll, self.pitch, self.yaw = euler_from_quaternion(float(x), float(y), float(z), float(w))

    def to_string(self):
        return str(self.roll) + " " + str(self.pitch) + " " + str(self.yaw)


class MetaData:
    def __init__(self, remap=False):
        self.parent_link = ""
        self.child_link = ""

        self.remap = remap
        self.cmd_args = "--ros-args --remap tf:={} --remap tf_static:={}"

    def remap_tf_and_tf_static(self, tf_static="tf_static", tf="tf"):
        self.remap = True
        self.remap_tf = tf
        self.remap_tf_static = tf_static

    def to_string(self):
        msg = self.parent_link + " " + self.child_link + " "
        if self.remap:
            msg += self.cmd_args.format(self.remap_tf, self.remap_tf_static)
        return msg


class StaticBroadcaster:

    def __init__(self, remap=False):
        self.translation = Translation()
        self.rotation = Rotation()
        self.metadata = MetaData(remap)

        self.running_subprocess = None

        self.cmd_format = "ros2 run tf2_ros static_transform_publisher {} {} {}"

    def start(self):
        cmd = self.cmd_format.format(self.translation.to_string(), self.rotation.to_string(), self.metadata.to_string())

        if resources.DEBUG_FLAGS.PRINT_SUBPROCESSES:
            print("Running process:\n{}".format(cmd))
            return

        self.running_subprocess = subprocess.Popen(['/bin/sh', '-c', cmd])

    @classmethod
    def from_dict(cls, data):
        obj = cls()

        obj.metadata.parent_link = data['parent']
        obj.metadata.child_link = data['child']

        trans_data = data['translation']
        obj.translation.set(trans_data['x'], trans_data['y'], trans_data['z'])

        rot_data = data['rotation']
        obj.rotation.set(rot_data['roll'], rot_data['pitch'], rot_data['yaw'])

        return obj
