from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QApplication, QStackedWidget
)
from PySide6.QtGui import QIcon

from src.ui.views.invoicing_associate_view import InvoicingAssociateView
from src.ui.components.sidebar import Sidebar


class Window(QMainWindow):
    def __init__(self, title: str):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(1000, 700)

        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.sidebar = Sidebar()
        main_layout.addWidget(self.sidebar)

        self.views = QStackedWidget()
        main_layout.addWidget(self.views)

        self.setCentralWidget(main_widget)
