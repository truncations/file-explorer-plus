from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QWidget, 
    QLabel, 
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout,
    QLineEdit,
    QStackedWidget,
    QToolBar,
    QSizePolicy,
)
from PyQt6.QtGui import QAction, QIcon
#import src.keys_vars when main runner
import keys_vars as keys_vars

class Menu_Button(QAction):
    def __init__(self, text, ref, icon : QIcon = None, tip="", is_toggleable=False):
        super().__init__(text, ref)
        self.setStatusTip(tip)
        self.setCheckable(is_toggleable)

        if icon is not None:
            self.setIcon(icon)

class Main_Application(QMainWindow):
    def __init__(self):
        super().__init__()

        self.customize_window()
        self.create_widgets()
        self.design_widgets()
        self.design_layouts()
        self.connect_events()

    def customize_window(self):
        self.setWindowTitle("File Explorer+")
        #self.setWindowIcon()
        self.setMinimumSize(keys_vars.Window_Config.min_width, keys_vars.Window_Config.min_height)
        self.resize(keys_vars.Window_Config.default_width, keys_vars.Window_Config.default_height)

    # only create widgets that will be present always throughout the application.
    def create_widgets(self):
        self.main_widget = QWidget()
        self.menu_buttons_row = QToolBar("Menu Buttons")

        # menu buttons
        self.tab_buttons = {
            "explorer": Menu_Button("Explorer",self,None,"View Explorer Tab.",True),
            "media": Menu_Button("Media",self,None,"View Media Tab.",True),
            "settings": Menu_Button("Settings",self,None,"View Settings Tab.",True),
        }

        self.extra_buttons = {
            "open_with_file_explorer": Menu_Button("BACKWARDS COMPATIBILITY",self),
            "list_view": Menu_Button("LIST VIEW",self),
            "icons_view": Menu_Button("ICONS VIEW",self),
        }

        # navigation stuff
        self.navigation_buttons = {
            "backwards": QPushButton("B"),
            "forwards": QPushButton("F"),
            "back_directory": QPushButton("U"),
            "refresh":  QPushButton("R"),
        }
        self.directory_bar = QLabel("Directory Bar")
        self.search_bar = QLineEdit()
        self.search_button = QPushButton("S")

        # main content
        self.navigation_section = QWidget()
        self.pages = QStackedWidget()

        # extra info
        self.storage_bar = QWidget()
        self.extra_info = QLabel("EXTRA INFO")
        

    def design_widgets(self):
        # prevent the toolbar, menu_buttons_row from being movable and hidden.
        self.menu_buttons_row.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.menu_buttons_row.setMovable(False)

        for button in self.navigation_buttons.values():
            button.setMaximumWidth(25)
        self.search_button.setMaximumWidth(25)

        self.search_bar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.directory_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def design_layouts(self):
        """
        create layouts
        """
        self.main_layout = QVBoxLayout()

        self.navigation_section_layout = QVBoxLayout()
        self.navigation_section_layout.setContentsMargins(5,5,5,5)
        self.navigation_section_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        # TEST
        self.navigation_section_layout.addWidget(QLabel("TEST"))
        self.navigation_section_layout.addWidget(QLabel("QUICK ACCESS"))
        self.navigation_section_layout.addWidget(QLabel("MY HEAD"))

        # directroy bar, search bar, and navigation buttons
        self.main_navigation_row = QHBoxLayout()    
        self.navigation_buttons_row = QHBoxLayout()
        self.directory_bar_row = QHBoxLayout()
        self.search_row = QHBoxLayout()

        # navigation section (on the left) and the main window itself
        self.main_content_row = QHBoxLayout()
        self.navigation_section.setLayout(self.navigation_section_layout)

        # extra info like storage for disk and number of items in directory.
        self.extra_info_row = QHBoxLayout()

        """
        push widgets into layouts
        """
        for button in self.tab_buttons.values():
            self.menu_buttons_row.addAction(button)
        for button in self.extra_buttons.values():
            self.menu_buttons_row.addAction(button)

        for button in self.navigation_buttons.values():
            self.navigation_buttons_row.addWidget(button)  
        self.directory_bar_row.addWidget(self.directory_bar)
        self.search_row.addWidget(self.search_bar, 3)
        self.search_row.addWidget(self.search_button)
        self.main_navigation_row.addLayout(self.navigation_buttons_row, 1)
        self.main_navigation_row.addLayout(self.directory_bar_row, 5)
        self.main_navigation_row.addLayout(self.search_row, 1)

        self.main_content_row.addWidget(self.navigation_section)
        self.main_content_row.addWidget(self.pages)

        self.extra_info_row.addWidget(self.storage_bar, 4)
        self.extra_info_row.addWidget(self.extra_info, 1)

        """
        finalize
        """ 
        self.main_layout.addLayout(self.main_navigation_row)
        self.main_layout.addLayout(self.main_content_row)
        self.main_layout.addLayout(self.extra_info_row)

        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        self.addToolBar(self.menu_buttons_row)

    def connect_events(self):
        pass

def start_application():
    application = QApplication([])

    # load any QT-required variables if necessary

    main_window = Main_Application()
    main_window.show()

    application.exec()

start_application()