"""
A viewer for all audio items in the song.
"""
_____ ___
____ PyQt4 _____ ?G.., ?C..
colors _ [?C...Qt.blue,
 ?C...Qt.green,
 ?C...Qt.red,
 ?C...Qt.yellow]

c_ timeline_item(?G...QGraphicsRectItem
    ___  -  , a_length, a_height, a_name, a_track_num, a_y_pos
        ?G...QGraphicsRectItem. -  , 0, 0, a_length, a_height)
        label _ ?G...QGraphicsSimpleTextItem(a_name, parent_self)
        label.setPos(10, 5)
        label.setBrush(?C...Qt.white)
        label.setFlag(?G...QGraphicsItem.ItemIgnoresTransformations)
        setFlag(?G...QGraphicsItem.ItemIsMovable)
        setFlag(?G...QGraphicsItem.ItemSendsGeometryChanges)
        track_num _ a_track_num
        mouse_y_pos _ a_y_pos

    ___ mouseDoubleClickEvent , a_event
        ?G...QGraphicsRectItem.mouseDoubleClickEvent , a_event)
        print "Here's where we'll open the item properties dialog for track " + st.(track_num)

    ___ mousePressEvent , a_event
        ?G...QGraphicsRectItem.mousePressEvent , a_event)
        setGraphicsEffect(?G...QGraphicsOpacityEffect())

    ___ mouseMoveEvent , a_event
        ?G...QGraphicsRectItem.mouseMoveEvent , a_event)
        f_pos _ pos().x()
        __ f_pos < 0:
            f_pos _ 0
        setPos(f_pos, mouse_y_pos)

    ___ mouseReleaseEvent , a_event
        ?G...QGraphicsRectItem.mouseReleaseEvent , a_event)
        setGraphicsEffect(None)
        f_pos_x _ pos().x()
        setPos(f_pos_x, mouse_y_pos)
        print st.(f_pos_x)

c_ timeline(?G...QGraphicsView
    ___  -  , a_item_length _ 4, a_region_length _ 8, a_bpm _ 140.0, a_px_per_region _ 100, total_tracks _ 5, total_regions _ 300
        item_length _ fl..(a_item_length)
        region_length _ fl..(a_region_length)
        ?G...QGraphicsView. - 
        setVerticalScrollBarPolicy(?C...Qt.ScrollBarAlwaysOff)
        setHorizontalScrollBarPolicy(?C...Qt.ScrollBarAlwaysOff)
        scene _ ?G...QGraphicsScene
        scene.setBackgroundBrush(?G...QColor(90, 90, 90))
        setScene(scene)
        audio_items _ []
        track _ 0
        gradient_index _ 0
        set_bpm(a_bpm)
        px_per_region _ a_px_per_region
        total_regions _ total_regions
        viewer_size _ px_per_region * total_regions
        header_height _ 20
        total_tracks _ total_tracks
        item_height _ 65
        padding _ 2
        draw_headers()
        draw_grid()

    ___ set_zoom , a_scale
        """ a_scale == number from 1.0 to 6.0 """
        scale(a_scale, 1.0)

    ___ set_bpm , a_bpm
        bps _ a_bpm / 60.0
        beats_per_region _ item_length * region_length
        regions_per_second _ bps / beats_per_region

    ___ f_seconds_to_regions , a_track_seconds
        """converts seconds to regions"""
        r_ a_track_seconds * regions_per_second

    ___ draw_headers 
        f_header _ ?G...QGraphicsRectItem(0, 0, viewer_size, header_height)
        scene.aI..(f_header)
        ___ i in range(0, total_regions
            f_number _ ?G...QGraphicsSimpleTextItem('%d' % i, f_header)
            f_number.setFlag(?G...QGraphicsItem.ItemIgnoresTransformations)
            f_number.setPos(px_per_region * i, 2)
            f_number.setBrush(?C...Qt.white)

    ___ draw_grid 
        f_pen _ ?G...QPen()
        ___ i in range(1, total_tracks + 1
            f_line _ ?G...QGraphicsLineItem(0, 0, viewer_size, 0)
            f_line.setPos(0, header_height + padding + item_height * i)
            scene.aI..(f_line)

    ___ draw_item_seconds , a_start_region, a_start_bar, a_start_beat, a_seconds, a_name, a_track_num
        f_start _ (a_start_region + (a_start_bar * item_length + a_start_beat) / beats_per_region) * px_per_region
        f_length _ f_seconds_to_regions(a_seconds) * px_per_region
        draw_item(f_start, f_length, a_name, a_track_num)

    ___ draw_item_musical_time , a_start_region, a_start_bar, a_start_beat, a_end_region, a_end_bar, a_end_beat, a_seconds, a_name, a_track_num
        f_start _ (a_start_region + (a_start_bar * item_length + a_start_beat) / beats_per_region) * px_per_region
        f_length _ (a_end_region + (a_end_bar * item_length + a_end_beat) / beats_per_region) * px_per_region - f_start
        f_length_seconds _ f_seconds_to_regions(a_seconds) * px_per_region
        __ f_length_seconds < f_length:
            f_length _ f_length_seconds
        draw_item(f_start, f_length, a_name, a_track_num)

    ___ clear_drawn_items 
        track _ 0
        gradient_index _ 0
        audio_items _ []
        scene.c..
        draw_headers()

    ___ draw_item , a_start, a_length, a_name, a_track_num
        """a_start in seconds, a_length in seconds"""
        f_track_num _ header_height + padding + item_height * track
        f_audio_item _ timeline_item(a_length, item_height, a_name, a_track_num, f_track_num)
        audio_items.ap..(f_audio_item)
        f_audio_item.setPos(a_start, f_track_num)
        f_audio_item.setBrush(colors[gradient_index])
        gradient_index +_ 1
        __ gradient_index >_ le.(colors
            gradient_index _ 0
        scene.aI..(f_audio_item)
        track +_ 1

__ __name__ __ '__main__':
    app _ ?G...?A..
    view _ timeline(total_tracks_5)
    ___ i in range(5
        view.draw_item_musical_time(0, 0, 0, i + 1, 0, 0, 120, 'Item-' + st.(i), i)

    view.set_zoom(2.0)
    view.s..
___.e..(app.e