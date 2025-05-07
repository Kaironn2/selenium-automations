from PySide6.QtCore import Qt
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtGui import QPixmap, QPainter, QColor, QIcon


class IconColorConverter:

    @staticmethod
    def svg_icon_white(svg_path, size=36):
        renderer = QSvgRenderer(svg_path)
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        renderer.render(painter)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), QColor('white'))
        painter.end()
        return QIcon(pixmap)
