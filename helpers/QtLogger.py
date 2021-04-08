import logging

from PyQt5 import QtWidgets, QtCore


class QTextEditLogger(logging.Handler):
    """
    Связывает QTextEdit и logging. Выделяет разные уровни сообщений цветом.
    """
    def __init__(self, a_text_edit: QtWidgets.QTextEdit):
        super().__init__()
        self.text_edit = a_text_edit

    def emit(self, record):
        msg = self.format(record)

        if record.levelno == logging.CRITICAL:
            color = QtCore.Qt.darkRed
        elif record.levelno == logging.ERROR:
            color = QtCore.Qt.red
        elif record.levelno == logging.WARNING:
            color = QtCore.Qt.darkYellow
        elif record.levelno == logging.INFO:
            color = QtCore.Qt.blue
        else:  # DEBUG or NOTSET
            color = QtCore.Qt.black

        self.text_edit.setTextColor(color)
        self.text_edit.insertPlainText(msg + '\n')
        self.text_edit.ensureCursorVisible()
