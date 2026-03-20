from win32api import GetMonitorInfo, MonitorFromPoint

height_screen_key = 3

# list_obj -> list of str(s)
def convert_list_to_str_directory(list_obj):
    s = list_obj[0] + ":/"
    return s+"/".join(list_obj[1:])+"/"

def get_taskbar_height():
    primary_monitor = MonitorFromPoint((0,0))
    monitor_info = GetMonitorInfo(primary_monitor)
    actual_screen_area = monitor_info.get("Monitor")
    available_screen_area = monitor_info.get("Work")
    return actual_screen_area[height_screen_key]-available_screen_area[height_screen_key]