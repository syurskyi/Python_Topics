______ html
______ l__

____ PySide2.QtCore ______ QObject, Signal


c_ RichTextHandlerObject(QObject):
    wroteLine = Signal(s..)

    ___ - 
        s__().- ()


c_ RichTextHandler(l__.Handler):

    BG_FG_COLORS = {
        l__.DEBUG: (N.., '#999999'),
        l__.INFO: (N.., '#e1e1e1'),
        l__.WARNING: (N.., '#e1e106'),
        l__.ERROR: (N.., '#e10606'),
        l__.CRITICAL: ('#410303', '#ff0000')
    }

    ___ -  obj):
        s__().- ()
        obj = obj

    ___ emit record):
        rtf_line = f..(record)
        obj.wroteLine.emit(rtf_line)

    ___ f.. record):
        style = _getStyle(record.levelno)
        text = html.escape(l__.Handler.f.. record))
        prefixLen = l..(text) - l..(record.message)
        __ hasattr(record, 'link'):
            url, start, end = record.link
            start += prefixLen
            end += prefixLen
            text = text[:start] + ('<a href="@">' @ url) + text[start:end] + '</a>' + text[end:]
        r_ '<span style="@">@</span>' @ (style, text.replace(' ', '&nbsp;'))

    ___ _getStyle levelno):
        styles   # list
        bg_color, fg_color = BG_FG_COLORS.get(levelno, (N.., N..))
        __ bg_color:
            styles.a.. ('background-color: @;' @ bg_color)
        styles.a.. ('color: @;' @ (fg_color __ fg_color else BG_FG_COLORS.get(l__.DEBUG)[1]))
        r_ ' '.join(styles)
