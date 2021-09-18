"""The Head-Fixed Mice Virtual Reality System

This Python script shows a virtual environment using a Tk interface. It aims to manage an infinity corridor which can
be controlled by mouse movements or an additional electronic component via serial communication.
"""
from argparse import ArgumentParser, SUPPRESS

import glob
import pi3d
import re
import serial
import time


def build_argparser() -> ArgumentParser():
    """Argument builder for construction via terminal.

        Returns:
            ArgumentParser: It represents the information needed to parse a single argument from one or more strings
            from the command line.
    """
    parser = ArgumentParser(add_help=False)
    arg_group = parser.add_argument_group("Options")
    arg_group.add_argument(
        "-h", "--help",
        action="help",
        default=SUPPRESS,
        help="Show this help message and exit.")

    # Serial arguments.
    arg_group.add_argument(
        "-p", "--port",
        default=r"/dev/ttyS0",
        help="Port is a device name: depending on operating system. e.g. /dev/ttyUSB0 on GNU/Linux or COM3 on Windows.",
        type=str)
    arg_group.add_argument(
        "-b", "--baudrate",
        help="The parameter baudrate can be one of the standard values: 50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200. These are well supported on all platforms.",
        default=115200,
        type=int
    )

    # Virtual environmental arguments.
    arg_group.add_argument(
        "-w", "--wall",
        help="A boolean value to add a wall in the middle of corridor.",
        default=False,
        type=bool
    )
    arg_group.add_argument(
        "-e", "--elevation",
        help="The user's point of view in the enviroment.",
        default=20,
        type=int
    )

    return parser


class VirtualEnvironment:
    """
    """

    @property
    def width(self):
        return self._width


    @width.setter
    def width(self, w):
        if (w < 1):
            raise ValueError("[Class Setter] Sorry the width is below eligibility criteria")
        self._width = w


    @property
    def height(self):
        return self._height


    @height.setter
    def height(self, h):
        if (h < 1):
            raise ValueError("[Class Setter] Sorry the height is below eligibility criteria")
        self._height = h


    @property
    def border(self):
        return self._border


    @border.setter
    def border(self, b):
        self._border = b


    @property
    def default_length(self):
        return self._default_length


    @default_length.setter
    def default_length(self, dl):
        if (dl < 1):
            raise ValueError("[Class Setter] Sorry the default length is below eligibility criteria")
        self._default_length = dl


    def __init__(self, port: str = "/dev/ttyS0", baudrate: int = 115200,
                 elevation: int = 20, has_wall: bool = False):

        # User's point of view in the enviroment.
        self.__elevation = elevation

        # Draw a wall in the corridor.
        self.__has_wall = has_wall
        
        # Virtual reality environment's resolution.
        self._width  = 1280
        self._height = 720
        self._border = 65

        # The default corridor length.
        self._default_length = 192

        # Setup the primary control device (i.e., Arduino or Mouse).
        self.__setup_device(port, baudrate)

        # Read the path file with the patterns IDs.
        self.__read_path_file()

        # Create a list with all  available pattern files.
        self.__create_pattern_list()


    def __setup_device(self, port: str, baudrate: int):
        # Try to connect to an Arduino via serial port. In case the device is not available,
        # the user will control the virtual environment via mouse movements.
        try:
            self.__serial_connection = serial.Serial(
                port=port,
                baudrate=baudrate,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )

        # In case of exception, defines the control variable as `None`.
        except OSError as err:
            print("[Connection Error] " + str(err))
            self.__serial_connection = None

        # This file saves the serial data into a text file.
        finally:
            self.__serial_output = open(r"data/serial_output.txt", "w")


    def __read_path_file(self):
        # Read the path file data.
        path_file = open(r"tmp/path.txt", "r")
        display_array = path_file.readline()
        display_length = path_file.readline()
        path_file.close()

        # Define a list with all patterns IDs.
        self.__display_list = [int(x) for x in display_array.split()]

        # Define the corridor measurements.
        self.__corridor_length  = self._default_length * int(display_length)
        self.__corridor_average = self.__corridor_length / len(self.__display_list)
        self.__corridor_start   = self.__corridor_average / 2


    def __create_pattern_list(self):

        string_pattern = r"images/patterns/**/*.jpg"
        self.__pattern_list = glob.glob(string_pattern, recursive=True)
        self.__pattern_list.sort()


    def __create_corridor(self):
        
        # The shader used to render the Shape Buffers using their draw() methods.
        shader = pi3d.Shader("uv_flat")

        # Create a list with all texture patterns.
        patterns = []
        for _ in range(5):
            for display in self.__display_list:
                patterns.append(pi3d.Texture(self.__pattern_list[display]))

        # Virtual environmental textures.
        ceil_tex = [pi3d.Texture(r"images/textures/crop.jpg")]
        floor_tex = pi3d.Texture(r"images/textures/grey.jpg")
        wall_tex = pi3d.Texture(r"images/textures/hornbeam2.png")

        # Create the elevation map.
        map_width = 10000.0
        map_depth = 10000.0
        map_height = 0.0

        elevation_map = pi3d.ElevationMap(
            mapfile="images/textures/white.png",
            width=map_width, depth=map_depth, height=map_height,
            divx=64, divy=64
        )
        elevation_map.set_draw_details(shader, [floor_tex], 0, 0.0)

        # Create an infinity corridor.
        for i, pattern in enumerate(patterns):
            pi3d.corridor(
                self.__corridor_start + self.__corridor_average * i,
                10, elevation_map, 50, self.__corridor_average, 30,
                details=[shader, [pattern], 1.0, 0.0, 1.0, 1.0], walls="nso"
            )

        # Draw a wall.
        if self.__has_wall:
            pi3d.corridor(
                self.__corridor_length + 1, 10, elevation_map, 50, 1, 30,
                details=[shader, [wall_tex], 1.0, 0.0, 1.0, 1.0], walls="w")  

        # Create the enviroment cube.
        enviroment_cube = pi3d.EnvironmentCube(
            size=20000.0, maptype="HALFCROSS"
        )
        enviroment_cube.set_draw_details(shader, ceil_tex)

        return elevation_map, enviroment_cube


    def __read_serial_data(self):
        position = 0

        # Waiting data from the connected Arduino.
        while self.__serial_connection.in_waiting:
            
            # Read the serial data.
            serial_str = self.__serial_connection.readline().decode("utf-8")
            try:
                if serial_str.find(",") != -1:
                    dy_str = serial_str[0:serial_str.find(",")]
                    dy_list = [int(d) for d in re.findall(r"-?\d+", dy_str)]
                    dy = dy_list[0]
                    position = int(dy)
                else:
                    position = 0

            # Fail reading serial data.
            except OSError as err:
                print("[Reading Error] " + str(err))
                self.__serial_connection.flush()
                position = 0

        return position


    def __save_serial_data(self, round_count: int, position: int):
        # Get the current timestamp, i.e., the number of seconds from 01/01/1970 to now.
        timestamp = time.time()

        # Write the current data into a text file.
        self.__serial_output.write(
            str(timestamp).strip() + "," +
            str(round_count).strip() + "," +
            str(position).strip()
        )
        self.__serial_output.write("\n")


    def run(self):

        # Setup display and initialise pi3d.
        DISPLAY = pi3d.Display.create(
            w=self._width,
            h=self._height - self._border,
            far=4000.0,
            background=(0, 0, 0, 0),
            frames_per_second=120
        )

        # Create the virtual corridor.
        elevation_map, enviroment_cube = self.__create_corridor()

        # The mouse and keyboard managers.
        mouse = pi3d.Mouse(restrict=False)
        mouse.start()
        keyboard = pi3d.Keyboard()

        # Setup the virtual camera.
        CAMERA = pi3d.Camera.instance()

        # A solid object is one that the avatar can not walk through.
        man = pi3d.SolidObject(
            "man", pi3d.Size(0.5, self.__elevation, 0.5),
            pi3d.Position(
                0, (elevation_map.calcHeight(5, 5) + self.__elevation / 2), 0
            ), 1
        )

        # Set the initial object position.
        initial_xm = -30
        initial_ym = self.__elevation / 2
        initial_zm = 9
        initial_position = pi3d.Position(initial_xm, initial_ym, initial_zm)

        man.move(initial_position)

        # Mouse controlling.
        previous_ym = 0

        # Round controller.
        round_count = 0

        # Draws all the models that comprise the building.
        pi3d.SolidObject.drawall()

        # The main event loop for the Display.
        while DISPLAY.loop_running():
            
            # Define the camera position.
            CAMERA.reset()
            CAMERA.rotate(-90, 0, 0)
            CAMERA.rotate(0, -90, 0)
            CAMERA.position((man.x(), man.y() + 3, man.z()))

            # Draws all the models that comprise the building.
            enviroment_cube.draw()
            elevation_map.draw()
            pi3d.SolidObject.drawall()

            # Read the current mouse position.
            _, my = mouse.position()

            # Read the current man position.
            if self.__serial_connection is not None:
                man_pos = self.__read_serial_data()
            else:
                man_pos = my - previous_ym

            xm = man.x() + man_pos

            # Update the previous mouse position.
            previous_ym = my

            # When it is needed, rotates the infinity virtual corridor.
            if xm < initial_xm:
                round_count -= 1
                xm = self.__corridor_length + initial_xm
                self.__save_serial_data(round_count, xm)

            elif xm > self.__corridor_length - 20:
                round_count += 1
                xm = initial_xm
                self.__save_serial_data(round_count, xm)

            # Set the new man position.
            zm = man.z()
            ym = elevation_map.calcHeight(xm, zm) + self.__elevation / 2
            new_position = pi3d.Position(xm, ym, zm)

            # Count for colissions.
            collisions = man.CollisionList(new_position)
            if not collisions:
                man.move(new_position)

            # Waits for a user input to quit the application.
            key = keyboard.read()
            if key == 27:
                keyboard.close()
                mouse.stop()
                DISPLAY.stop()
                if self.__serial_connection is not None:
                    self.__serial_connection.close()
                break

        # When everything done, release the allocated resources.
        self.__serial_output.close()
        DISPLAY.destroy()


if __name__ == "__main__":
    args = build_argparser().parse_args()
    vr = VirtualEnvironment(
        port=args.port, baudrate=args.baudrate,
        elevation=args.elevation, has_wall=args.wall
    )
    vr.run()
