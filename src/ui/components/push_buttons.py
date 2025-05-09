from src.ui.qt_imports import *
from src.ui.helpers.icon_color_converter import IconColorConverter as icc
from src.utils.path_utils import PathUtils


class BaseButton(QPushButton):
    def __init__(self, text: str, icon_path: str = None, icon_size: int = 24, on_click=None, parent=None):
        super().__init__(text, parent)
        self.setFlat(True)
        self.setCursor(Qt.PointingHandCursor)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setCheckable(True)

        if icon_path:
            if str(icon_path).endswith('.svg'):
                self.setIcon(icc.svg_icon_white(icon_path))
            else:
                self.setIcon(QIcon(icon_path))
            self.setIconSize(QSize(icon_size, icon_size))


class SidebarButton(BaseButton):
    def __init__(self, text: str, key: str, icon_path: str = None, icon_size: int = 24, on_click=None, parent=None):
        super().__init__(text, icon_path, icon_size, on_click, parent)
        self.setStyleSheet('''
            QPushButton {
                background: transparent;
                color: #eee;
                font-size: 15px;
                padding: 10px 0 10px 36px;
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
        self.key = key

        if on_click:
            self.clicked.connect(lambda: on_click(key))


class StartButton(BaseButton):
    def __init__(self, text='Start', icon_path=PathUtils.resource_path('icons/circle-play.svg'), icon_size=20, on_click=None, parent=None):
        super().__init__(text, icon_path, icon_size, on_click, parent)
        self.setStyleSheet('''
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #5a43a5, stop:1 #7c5be7);
                color: #fff;
                font-size: 16px;
                font-weight: bold;
                padding: 10px 32px;
                border-radius: 8px;
                border: none;
                letter-spacing: 1px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7c5be7, stop:1 #5a43a5);
                color: #fff;
            }
            QPushButton:pressed {
                background: #3c2f67;
            }
            QPushButton:disabled {
                background: #888;
                color: #ccc;
            }
        ''')
        self.setFixedSize(140, 40)

        if on_click:
            self.clicked.connect(on_click)
