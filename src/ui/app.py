from src.ui.qt_imports import *

from src.ui.views.kmln.invoicing_associate_view import InvoicingAssociateView
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

        self.sidebar = Sidebar(on_selected=self.handle_sidebar_click)
        main_layout.addWidget(self.sidebar)

        self.views = QStackedWidget()
        self.invoicing_view = InvoicingAssociateView()
        self.views.addWidget(self.invoicing_view)

        main_layout.addWidget(self.views)
        self.setCentralWidget(main_widget)

    def handle_sidebar_click(self, key):
        if key == 'invoicing_associate':
            self.views.setCurrentWidget(self.invoicing_view)
