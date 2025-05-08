from src.ui.qt_imports import *


class ModernLineEdit(QLineEdit):
    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setStyleSheet("""
            QLineEdit {
                background: #282846;
                color: #fff;
                border: 2px solid #39396b;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 15px;
                selection-background-color: #5a43a5;
            }
            QLineEdit:focus {
                border: 2px solid #7c5be7;
                background: #22223a;
            }
            QLineEdit:disabled {
                background: #22223a;
                color: #888;
                border: 2px solid #333;
            }
        """)
        self.setMinimumWidth(180)
        self.setMaximumWidth(320)
