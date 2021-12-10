______ html
______ logging

from PySide2.QtCore ______ QObject, Signal


c_ RichTextHandlerObject(QObject):
    wroteLine = Signal(s..)

    ___ - 
        super().- ()


c_ RichTextHandler(logging.Handler):

    BG_FG_COLORS = {
        logging.DEBUG: (N.., '#999999'),
        logging.INFO: (N.., '#e1e1e1'),
        logging.WARNING: (N.., '#e1e106'),
        logging.ERROR: (N.., '#e10606'),
        logging.CRITICAL: ('#410303', '#ff0000')
    }

    ___ - (self, obj):
        super().- ()
        obj = obj

    ___ emit(self, record):
        rtf_line = format(record)
        obj.wroteLine.emit(rtf_line)

    ___ format(self, record):
        style = _getStyle(record.levelno)
        text = html.escape(logging.Handler.format(self, record))
        prefixLen = l..(text) - l..(record.message)
        __ hasattr(record, 'link'):
            url, start, end = record.link
            start += prefixLen
            end += prefixLen
            text = text[:start] + ('<a href="@">' @ url) + text[start:end] + '</a>' + text[end:]
        r_ '<span style="@">@</span>' @ (style, text.replace(' ', '&nbsp;'))

    ___ _getStyle(self, levelno):
        styles   # list
        bg_color, fg_color = BG_FG_COLORS.get(levelno, (N.., N..))
        __ bg_color:
            styles.a.. ('background-color: @;' @ bg_color)
        styles.a.. ('color: @;' @ (fg_color __ fg_color else BG_FG_COLORS.get(logging.DEBUG)[1]))
        r_ ' '.join(styles)
