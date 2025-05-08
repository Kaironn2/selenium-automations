from src.ui.qt_imports import *
from src.ui.components.push_buttons import StartButton
from src.ui.components.line_edit import ModernLineEdit


class InvoicingAssociateView(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.setAlignment(Qt.AlignCenter)
        central_layout.setSpacing(20)
        central_layout.setContentsMargins(32, 32, 32, 32)

        self.input_label = QLabel('Collection Date')
        self.input_label.setStyleSheet('color: #bbb; font-size: 13px; margin-bottom: 0px;')
        central_layout.addWidget(self.input_label, alignment=Qt.AlignCenter)

        self.input = ModernLineEdit('2025/04/21')
        self.input.setFixedWidth(240)
        central_layout.addWidget(self.input, alignment=Qt.AlignCenter)

        central_layout.addSpacing(24)

        self.start_btn = StartButton()
        self.start_btn.setFixedWidth(160)
        central_layout.addWidget(self.start_btn, alignment=Qt.AlignCenter)

        main_layout.addWidget(central_widget, alignment=Qt.AlignCenter)

    def set_input_text(self, text):
        self.input.setText(text)

    def disable_inputs(self):
        self.input.setEnabled(False)
        self.start_btn.setEnabled(False)
