import os
import src.utility_functions as util_functions

# Stores Keys for readability and Variables here.

base_directory = os.path.dirname(__file__)[:-len("src")]
resource_directory = base_directory + "resource/"
ui_src_file_name = "ui_source.ui"

current_directory_path = ["A", "docs", "LibreOffice", "Writer Docs"]
current_directory = util_functions.convert_list_to_str_directory(current_directory_path)
max_log_count = 30

class Window_Config():
    min_width = 50
    min_height = 200

    # to remove for later
    default_width = 800
    default_height = 500