from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase

from src.utils.path_utils import PathUtils
from src.ui.app import Window


if __name__ == '__main__':
    app = QApplication([])
    QFontDatabase.addApplicationFont(PathUtils.resource_path('fonts/Inter.ttc'))
    app.setStyleSheet("""
        * {
            font-family: 'Inter';
            font-size: 15px;
        }
        QMainWindow {
            background: #181623;
        }
    """)
    window = Window('SL Automations')
    window.show()
    app.exec()
