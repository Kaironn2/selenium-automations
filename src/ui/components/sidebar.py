from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QFrame, QButtonGroup
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

from src.utils.path_utils import PathUtils
from src.ui.helpers.icon_color_converter import IconColorConverter as icc
from src.ui.components.sidebar_button import SidebarButton


class Sidebar(QWidget):
    def __init__(self, on_selected, parent=None):
        super().__init__(parent)
        self.setObjectName('Sidebar')
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 16, 0, 0)
        self.layout.setSpacing(20)
        self.buttons = {}
        self.on_selected = on_selected
        self.setAutoFillBackground(True)

        self.setStyleSheet("""
            Sidebar, QWidget#Sidebar {
                background-color: #22212f;
            }
        """)

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)


        # Kmln section
        self._add_section(
            title='Kmln',
            options=[
                ('Invoicing Associate', 'invoicing_associate', PathUtils.resource_path('imgs/circle-dollar-sign.svg')),
            ]
        )
        self._add_separator()

        # Ecs section
        self._add_section(
            title='Ecs',
            options=[
                ('Delivery Launcher', 'delivery_launcher', PathUtils.resource_path('imgs/delivery-truck.svg')),
            ]
        )
        self._add_separator()

        # Mgt section
        self._add_section(
            title='Configs',
            options=[
                ('Settings', 'settings', PathUtils.resource_path('imgs/delivery-truck.svg')),
            ]
        )

        self.layout.addStretch(1)

    def _add_section(self, title, options):
        section_layout = QVBoxLayout()
        section_layout.setSpacing(0)
        title_label = QLabel(title)
        title_label.setStyleSheet('color: white; font-size: 18px; font-weight: bold; margin-bottom: 8px;')
        section_layout.addWidget(title_label, alignment=Qt.AlignLeft)
        for idx, (text, key, icon_path) in enumerate(options):
            self._add_sidebar_button(section_layout, text, key, icon_path)
        self.layout.addLayout(section_layout)

    def _add_sidebar_button(self, layout, text, key, icon_path=None):
        btn = SidebarButton(
            text=text,
            key=key,
            icon_path=icon_path,
            on_click=self.on_selected
        )
        layout.addWidget(btn)
        self.buttons[key] = btn
        self.button_group.addButton(btn)

    def _add_separator(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Plain)
        line.setFixedHeight(1)
        line.setStyleSheet('background: #fff; border: none; margin: 8px 12px;')
        self.layout.addWidget(line)

    def select(self, key):
        for k, btn in self.buttons.items():
            btn.setChecked(k == key)
        if self.on_selected:
            self.on_selected(key)