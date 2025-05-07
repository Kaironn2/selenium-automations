from pathlib import Path
import sys
import os


class PathUtils:
    ROOT = Path(__file__).parent.parent.parent
    SRC_FOLDER = ROOT / 'src'

    DATA_FOLDER = SRC_FOLDER / 'data'
    KMLN_DATA_FOLDER = DATA_FOLDER / 'kmln'
    LOGS_FOLDER = DATA_FOLDER / 'logs'

    ASSETS_FOLDER = SRC_FOLDER / 'ui' / 'assets'

    @classmethod
    def resource_path(cls, relative_path: str) -> str:
        if hasattr(sys, '_MEIPASS'):
            base_path = Path(sys._MEIPASS)
        else:
            base_path = cls.ASSETS_FOLDER
        return str(base_path / relative_path)
