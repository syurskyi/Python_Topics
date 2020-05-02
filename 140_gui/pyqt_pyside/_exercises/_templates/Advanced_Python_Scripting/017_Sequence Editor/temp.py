"""
A viewer for all audio items in the song.
"""
_____ ___
____ PyQt4 _____ QtGui, ?C..
colors = [?C...Qt.blue,
 ?C...Qt.green,
 ?C...Qt.red,
 ?C...Qt.yellow]

c_ timeline_item(QtGui.QGraphicsRectItem
    ___  -  , a_length, a_height, a_name, a_track_num, a_y_pos
        QtGui.QGraphicsRectItem. -  , 0, 0, a_length, a_height)
        label = QtGui.QGraphicsSimpleTextItem(a_name, parent=self)
        label.setPos(10, 5)
        label.setBrush(?C...Qt.white)
        label.setFlag(QtGui.QGraphicsItem.ItemIgnoresTransformations)
        setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        setFlag(QtGui.QGraphicsItem.ItemSendsGeometryChanges)
        track_num = a_track_num
        mouse_y_pos = a_y_pos

    ___ mouseDoubleClickEvent , a_event
        QtGui.QGraphicsRectItem.mouseDoubleClickEvent , a_event)
        print "Here's where we'll open the item properties dialog for track " + st.(track_num)

    ___ mousePressEvent , a_event
        QtGui.QGraphicsRectItem.mousePressEvent , a_event)
        setGraphicsEffect(QtGui.QGraphicsOpacityEffect())

    ___ mouseMoveEvent , a_event
        QtGui.QGraphicsRectItem.mouseMoveEvent , a_event)
        f_pos = pos().x()
        __ f_pos < 0:
            f_pos = 0
        setPos(f_pos, mouse_y_pos)

    ___ mouseReleaseEvent , a_event
        QtGui.QGraphicsRectItem.mouseReleaseEvent , a_event)
        setGraphicsEffect(None)
        f_pos_x = pos().x()
        setPos(f_pos_x, mouse_y_pos)
        print st.(f_pos_x)

c_ timeline(QtGui.QGraphicsView
    ___  -  , a_item_length = 4, a_region_length = 8, a_bpm = 140.0, a_px_per_region = 100, total_tracks = 5, total_regions = 300
        item_length = float(a_item_length)
        region_length = float(a_region_length)
        QtGui.QGraphicsView. - 
        setVerticalScrollBarPolicy(?C...Qt.ScrollBarAlwaysOff)
        setHorizontalScrollBarPolicy(?C...Qt.ScrollBarAlwaysOff)
        scene = QtGui.QGraphicsScene
        scene.setBackgroundBrush(QtGui.QColor(90, 90, 90))
        setScene(scene)
        audio_items = []
        track = 0
        gradient_index = 0
        set_bpm(a_bpm)
        px_per_region = a_px_per_region
        total_regions = total_regions
        viewer_size = px_per_region * total_regions
        header_height = 20
        total_tracks = total_tracks
        item_height = 65
        padding = 2
        draw_headers()
        draw_grid()

    ___ set_zoom , a_scale
        """ a_scale == number from 1.0 to 6.0 """
        scale(a_scale, 1.0)

    ___ set_bpm , a_bpm
        bps = a_bpm / 60.0
        beats_per_region = item_length * region_length
        regions_per_second = bps / beats_per_region

    ___ f_seconds_to_regions , a_track_seconds
        """converts seconds to regions"""
        return a_track_seconds * regions_per_second

    ___ draw_headers 
        f_header = QtGui.QGraphicsRectItem(0, 0, viewer_size, header_height)
        scene.addItem(f_header)
        for i in range(0, total_regions
            f_number = QtGui.QGraphicsSimpleTextItem('%d' % i, f_header)
            f_number.setFlag(QtGui.QGraphicsItem.ItemIgnoresTransformations)
            f_number.setPos(px_per_region * i, 2)
            f_number.setBrush(?C...Qt.white)

    ___ draw_grid 
        f_pen = QtGui.QPen()
        for i in range(1, total_tracks + 1
            f_line = QtGui.QGraphicsLineItem(0, 0, viewer_size, 0)
            f_line.setPos(0, header_height + padding + item_height * i)
            scene.addItem(f_line)

    ___ draw_item_seconds , a_start_region, a_start_bar, a_start_beat, a_seconds, a_name, a_track_num
        f_start = (a_start_region + (a_start_bar * item_length + a_start_beat) / beats_per_region) * px_per_region
        f_length = f_seconds_to_regions(a_seconds) * px_per_region
        draw_item(f_start, f_length, a_name, a_track_num)

    ___ draw_item_musical_time , a_start_region, a_start_bar, a_start_beat, a_end_region, a_end_bar, a_end_beat, a_seconds, a_name, a_track_num
        f_start = (a_start_region + (a_start_bar * item_length + a_start_beat) / beats_per_region) * px_per_region
        f_length = (a_end_region + (a_end_bar * item_length + a_end_beat) / beats_per_region) * px_per_region - f_start
        f_length_seconds = f_seconds_to_regions(a_seconds) * px_per_region
        __ f_length_seconds < f_length:
            f_length = f_length_seconds
        draw_item(f_start, f_length, a_name, a_track_num)

    ___ clear_drawn_items 
        track = 0
        gradient_index = 0
        audio_items = []
        scene.clear()
        draw_headers()

    ___ draw_item , a_start, a_length, a_name, a_track_num
        """a_start in seconds, a_length in seconds"""
        f_track_num = header_height + padding + item_height * track
        f_audio_item = timeline_item(a_length, item_height, a_name, a_track_num, f_track_num)
        audio_items.append(f_audio_item)
        f_audio_item.setPos(a_start, f_track_num)
        f_audio_item.setBrush(colors[gradient_index])
        gradient_index += 1
        __ gradient_index >= len(colors
            gradient_index = 0
        scene.addItem(f_audio_item)
        track += 1

__ __name__ __ '__main__':
    app = QtGui.?A..(___.argv)
    view = timeline(total_tracks=5)
    for i in range(5
        view.draw_item_musical_time(0, 0, 0, i + 1, 0, 0, 120, 'Item-' + st.(i), i)

    view.set_zoom(2.0)
    view.s..
___.e..(app.exec_())