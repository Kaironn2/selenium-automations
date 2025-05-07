from pathlib import Path


class PathUtils:
    ROOT = Path(__file__).parent.parent.parent
    DATA_FOLDER = ROOT / 'src' / 'data'
    KMLN_DATA_FOLDER = DATA_FOLDER / 'kmln'
    LOGS_FOLDER = DATA_FOLDER / 'logs'
