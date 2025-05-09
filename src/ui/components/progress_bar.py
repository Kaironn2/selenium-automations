from src.ui.qt_imports import *


class HorizontalProgressBar(QWidget):
    def __init__(self, total=100, parent=None):
        super().__init__(parent)
        self.total = total
        self.current = 0

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)

        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(self.total)
        self.progress.setValue(self.current)
        self.progress.setTextVisible(False)
        self.progress.setFixedHeight(22)
        self.progress.setStyleSheet('''
            QProgressBar {
                background: #22223a;
                border-radius: 8px;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #5a43a5, stop:1 #7c5be7);
                border-radius: 8px;
            }
        ''')

        self.counter = QLabel(f'{self.current} / {self.total}')
        self.counter.setStyleSheet('color: #bbb; font-size: 14px; font-weight: bold;')
        self.counter.setFixedWidth(70)
        self.counter.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        layout.addWidget(self.progress, stretch=1)
        layout.addWidget(self.counter)

    def set_value(self, value):
        self.current = value
        self.progress.setValue(value)
        self.counter.setText(f'{self.current} / {self.total}')

    def set_total(self, total):
        self.total = total
        self.progress.setMaximum(total)
        self.counter.setText(f'{self.current} / {self.total}')
