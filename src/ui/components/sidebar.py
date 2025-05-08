from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QFrame, QButtonGroup, QFrame
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

from src.utils.path_utils import PathUtils
from src.ui.helpers.icon_color_converter import IconColorConverter as icc
from src.ui.components.sidebar_button import SidebarButton


class Sidebar(QFrame):
    def __init__(self, on_selected=None, parent=None):
        super().__init__(parent)
        self.setObjectName('Sidebar')
        self.setMinimumWidth(240)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.setStyleSheet("""
            #Sidebar {
                background-color: #22212f;
                border-right: 2px solid red;
            }
        """)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 16, 0, 0)
        self.layout.setSpacing(20)

        title = QLabel("Sidebar Exemplo")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        self.layout.addWidget(title)

        self.layout.addStretch(1)
