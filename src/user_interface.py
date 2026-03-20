from PyQt6 import uic # allows to load ui
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout
)
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QIcon
import sys
import src.vars_util as vars_util

class Special_Bounds_Keys:
    TOP_OF_SCREEN = 1
    BOTTOM_OF_SCREEN = -1
    NO_SPECIALS = 0

class Main_Application(QMainWindow):
    app_ref = None
    window_at_top = False

    def __init__(self, app_reference):
        super().__init__()

        Main_Application.app_ref = app_reference
        self.load_ui()
        
        self.setup_main_window_functions()

        self.title_row.mouseMoveEvent = self.move_window_event

    def setup_main_window_functions(self):
        # minimize, fullscreen, quit, move window.
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.button_close_window.clicked.connect(self.close_window)
        self.button_minimize_window.clicked.connect(self.minimize_window)
        self.button_fullscreen_window.clicked.connect(self.fullscreen_button_clicked)

    def load_ui(self):
        uic.load_ui.loadUi(vars_util.Directory_Manager.get_dir_ui_file(vars_util.ui_src_file_name), self)

    # events
    def close_window(self):
        Main_Application.app_ref.exit()

    def minimize_window(self):
        self.setWindowState(Qt.WindowState.WindowMinimized)

    def fullscreen_button_clicked(self):
        if self.isMaximized():
            self.display_fullscreen_unenabled()
        else:
            self.display_fullscreen_enabled()

    # helpers for fullscreening
    def display_fullscreen_enabled(self):
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.button_fullscreen_window.setIcon(QIcon(vars_util.Directory_Manager.get_dir_image_from_icons("fullscreen_2.png")))

    def display_fullscreen_unenabled(self):
        self.setWindowState(Qt.WindowState.WindowActive)
        self.button_fullscreen_window.setIcon(QIcon(vars_util.Directory_Manager.get_dir_image_from_icons("fullscreen.png")))

    def move_window_event(self, event):
        if self.isMaximized():
            self.display_fullscreen_unenabled()

        if event.buttons() == Qt.MouseButton.LeftButton:
            new_position : QPoint = self.pos() + event.globalPosition().toPoint() - self.click_position
            # ensure that the window is always apparent, even when near the taskbar, as well as if the window hits the top, it will auto fullscreen.
            special_bounds_key = self.check_for_special_bounds(new_position)
            Main_Application.window_at_top = False

            if special_bounds_key == Special_Bounds_Keys.TOP_OF_SCREEN:
                Main_Application.window_at_top = True
                self.move(new_position)
            elif special_bounds_key == Special_Bounds_Keys.NO_SPECIALS:
                self.move(new_position)
            
            self.click_position = event.globalPosition().toPoint()
            event.accept()

    # MUST TAKE IN QPOINT
    def check_for_special_bounds(self, pos : QPoint):
        screen_area_geometry = QApplication.primaryScreen().geometry()
        screen_area_geometry = (screen_area_geometry.width(), screen_area_geometry.height())

        taskbar_height = vars_util.Window_Config.get_taskbar_height()
        # is window at top of screen?
        if pos.y() <= 0:
            return Special_Bounds_Keys.TOP_OF_SCREEN
        # else is window near the taskbar?
        elif pos.y() > screen_area_geometry[1] - taskbar_height - 5:
            return Special_Bounds_Keys.BOTTOM_OF_SCREEN
        # otherwise we're fine..
        else:
            return Special_Bounds_Keys.NO_SPECIALS

    def mousePressEvent(self, event):
        self.click_position = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        if Main_Application.window_at_top:
            self.display_fullscreen_enabled()

def start_application():
    app = QApplication([])

    # define all QT variables here

    window = Main_Application(app)
    window.show()

    sys.exit(app.exec())
