import logging
from datetime import datetime
from pathlib import Path
from src.utils.path_utils import PathUtils


class LoggingUtils:
    def __init__(self, module_file: str):
        module_name = Path(module_file).stem
        log_dir = PathUtils.LOGS_FOLDER / module_name
        log_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_file = log_dir / f'{timestamp}.log'

        self.logger = logging.getLogger(module_name + '_' + timestamp)
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

    def get_logger(self):
        return self.logger
