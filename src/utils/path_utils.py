from pathlib import Path
import sys
import os


class PathUtils:
    ROOT = Path(__file__).parent.parent.parent

    CONFIG_FOLDER = ROOT / 'config'
    KMLN_CONFIG_FOLDER = CONFIG_FOLDER / 'kmln'
    LOGS_FOLDER = ROOT / 'logs'

    SRC_FOLDER = ROOT / 'src'
    ASSETS_FOLDER = SRC_FOLDER / 'ui' / 'assets'

    @classmethod
    def resource_path(cls, relative_path: str) -> str:
        if hasattr(sys, '_MEIPASS'):
            base_path = Path(sys._MEIPASS)
        else:
            base_path = cls.ASSETS_FOLDER
        return str(base_path / relative_path)
