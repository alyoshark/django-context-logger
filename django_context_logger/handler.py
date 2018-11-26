from sys import _getframe

from logging.handlers import RotatingFileHandler


class DjangoContextLogger(RotatingFileHandler):
    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=False, frame_cnt=10, context='request', fields=None):
        super(DjangoContextLogger, self).__init__(filename, mode, maxBytes, backupCount, encoding, delay)
        self.frame_cnt = frame_cnt
        self.context = context
        self.fields = fields

    def prepad_context(self, context):
        # TODO: Nested fields
        return '|'.join('%s:%s' % (f, context.getattr(f)) for f in self.fields)

    def emit(self, record):
        frame = _getframe()
        emit = super(DjangoContextLogger, self).emit(record)
        for i in range(self.frame_cnt):
            if self.context in frame.f_locals:
                ctx = frame.f_locals[self.context]
                emit(self.prepad_context(ctx) + '|' + record)
            frame = frame.f_back
        emit(record)  # Just log as it is