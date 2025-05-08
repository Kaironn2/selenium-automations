from PySide6.QtWidgets import QPushButton, QSizePolicy
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from src.ui.helpers.icon_color_converter import IconColorConverter as icc


class SidebarButton(QPushButton):
    def __init__(self, text: str, key: str, icon_path: str = None, icon_size: int = 24, on_click=None, parent=None):
        super().__init__(text, parent)
        self.setFlat(True)
        self.setCursor(Qt.PointingHandCursor)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet('''
            QPushButton {
                background: transparent;
                color: #eee;
                font-size: 15px;
                padding: 10px 0 10px 12px;
                margin: 0px;
                text-align: left;
                border: none;
            }
            QPushButton:checked {
                background: #181623;
                border-left: 4px solid #5a43a5;
            }
            QPushButton:hover {
                background: #333;
            }
        ''')
        self.setCheckable(True)
        self.key = key

        if icon_path:
            if str(icon_path).endswith('.svg'):
                self.setIcon(icc.svg_icon_white(icon_path))
            else:
                self.setIcon(QIcon(icon_path))
            self.setIconSize(QSize(icon_size, icon_size))

        if on_click:
            self.clicked.connect(lambda _: on_click(self.key))
