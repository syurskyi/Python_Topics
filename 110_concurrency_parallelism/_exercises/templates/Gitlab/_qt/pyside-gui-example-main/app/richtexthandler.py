______ html
______ logging

from PySide2.QtCore ______ QObject, Signal


class RichTextHandlerObject(QObject):
    wroteLine = Signal(s..)

    ___ __init__(self):
        super().__init__()


class RichTextHandler(logging.Handler):

    BG_FG_COLORS = {
        logging.DEBUG: (N.., '#999999'),
        logging.INFO: (N.., '#e1e1e1'),
        logging.WARNING: (N.., '#e1e106'),
        logging.ERROR: (N.., '#e10606'),
        logging.CRITICAL: ('#410303', '#ff0000')
    }

    ___ __init__(self, obj):
        super().__init__()
        self.obj = obj

    ___ emit(self, record):
        rtf_line = self.format(record)
        self.obj.wroteLine.emit(rtf_line)

    ___ format(self, record):
        style = self._getStyle(record.levelno)
        text = html.escape(logging.Handler.format(self, record))
        prefixLen = len(text) - len(record.message)
        if hasattr(record, 'link'):
            url, start, end = record.link
            start += prefixLen
            end += prefixLen
            text = text[:start] + ('<a href="%s">' % url) + text[start:end] + '</a>' + text[end:]
        return '<span style="%s">%s</span>' % (style, text.replace(' ', '&nbsp;'))

    ___ _getStyle(self, levelno):
        styles = []
        bg_color, fg_color = self.BG_FG_COLORS.get(levelno, (N.., N..))
        if bg_color:
            styles.append('background-color: %s;' % bg_color)
        styles.append('color: %s;' % (fg_color if fg_color else self.BG_FG_COLORS.get(logging.DEBUG)[1]))
        return ' '.join(styles)
