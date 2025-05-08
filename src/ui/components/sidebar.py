from src.ui.qt_imports import *

from src.utils.path_utils import PathUtils
from src.ui.helpers.icon_color_converter import IconColorConverter as icc
from src.ui.components.push_buttons import SidebarButton


class Sidebar(QFrame):
    def __init__(self, on_selected=None, parent=None):
        super().__init__(parent)
        self.on_selected = on_selected
        self.setObjectName('Sidebar')
        self.setFixedWidth(240)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.setStyleSheet('''
            #Sidebar {
                background-color: #22212f;
                border-top-right-radius: 16px;
                border-bottom-right-radius: 16px;
            }
        ''')

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 16, 0, 0)
        self.layout.setSpacing(20)

        title = QLabel('SL Automations')
        title.setStyleSheet('color: white; font-size: 18px; font-weight: bold;')
        self.layout.addWidget(title, alignment=Qt.AlignHCenter)

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)

        self.ecs_section()
        self.kml_section()

        self.layout.addStretch(1)
        self.box_shadow()

    def box_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(16)
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setOffset(6, 0)
        self.setGraphicsEffect(shadow)

    def create_button(self, text, key, icon_path=None, icon_size=24):
        button = SidebarButton(
            text=text,
            key=key,
            icon_path=icon_path,
            icon_size=icon_size,
        )
        self.layout.addWidget(button)
        self.button_group.addButton(button)

    def create_section(self, title, buttons):
        section_title = QLabel(title)
        section_title.setStyleSheet('color: white; font-size: 16px; margin-left: 12px;')
        self.layout.addWidget(section_title, alignment=Qt.AlignLeft)

        for button in buttons:
            self.layout.addWidget(button)
            self.button_group.addButton(button)

    def ecs_section(self):
        btn1 = SidebarButton(
            text='Delivery Launcher',
            key='delivery_launcher',
            icon_path=PathUtils.resource_path('icons/package-check.svg'),
            on_click=self.on_selected,
        )
        self.create_section('Ecs', [btn1])

    def kml_section(self):
        btn1 = SidebarButton(
            text='Invoicing Associate',
            key='invoicing_associate',
            icon_path=PathUtils.resource_path('icons/circle-dollar-sign.svg'),
            on_click=self.on_selected,
        )
        self.create_section('Kmln', [btn1])
