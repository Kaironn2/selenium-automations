from src.ui.qt_imports import *


class PipelineWorker(QObject):
    finished = Signal()
    error = Signal(Exception)

    def __init__(self, pipeline_class, *args, **kwargs):
        super().__init__()
        self.pipeline_class = pipeline_class
        self.args = args
        self.kwargs = kwargs

    def run(self):
        print('Pipeline started')
        try:
            pipeline = self.pipeline_class(*self.args, **self.kwargs)
            pipeline.run()
            self.finished.emit()
        except Exception as e:
            self.error.emit(e)

def run_pipeline_in_thread(parent, pipeline_class, on_finished, on_error=None, *args, **kwargs):
    print('Running pipeline in thread')
    thread = QThread(parent)
    worker = PipelineWorker(pipeline_class, *args, **kwargs)
    worker.moveToThread(thread)
    thread.started.connect(worker.run)
    worker.finished.connect(thread.quit)
    worker.finished.connect(on_finished)
    if on_error:
        worker.error.connect(on_error)
    thread.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)
    thread.start()
    return thread, worker
