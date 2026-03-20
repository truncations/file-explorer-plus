import os
from win32api import GetMonitorInfo, MonitorFromPoint

height_screen_key = 3

# Stores Keys for readability and Variables here.

# DO NOT CHANGE
_base_directory = os.path.dirname(__file__)[:-len("src")]
_resource_directory = os.path.join(_base_directory, "resource")
ui_src_file_name = "ui_source.ui"

max_log_count = 30

class Directory_Manager:
    default_directory = os.path.abspath(os.sep)
    current_directory = default_directory
    current_directory_path = None

    @staticmethod
    def get_dir_ui_file(ui_file_name):
        return os.path.join(_resource_directory, ui_file_name)

    # MUST INCLUDE FILE EXTENSION.
    @staticmethod
    def get_dir_image_from_icons(image_file_name):
        return os.path.join(_resource_directory, "icons", image_file_name)
    
    # list_obj -> list of str(s)
    @staticmethod
    def split_path_into_list(directory):
        path_list = [path for path in os.path.split(directory)]
        return path_list
    
    # setup definitions for Directory_Manager variables if the methods above are required.
    current_directory_path = split_path_into_list(current_directory)

class Window_Config():

    min_width = 50
    min_height = 200

    # to remove for later
    default_width = 800
    default_height = 500

    @staticmethod
    def get_taskbar_height():
        primary_monitor = MonitorFromPoint((0,0))
        monitor_info = GetMonitorInfo(primary_monitor)
        actual_screen_area = monitor_info.get("Monitor")
        available_screen_area = monitor_info.get("Work")
        return actual_screen_area[height_screen_key]-available_screen_area[height_screen_key]