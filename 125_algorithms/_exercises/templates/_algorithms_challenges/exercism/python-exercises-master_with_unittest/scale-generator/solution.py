c_ Scale(o..

    ASCENDING_INTERVALS =  'm', 'M', 'A'
    CHROMATIC_SCALE =  'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A',
                       'A#', 'B'
    FLAT_CHROMATIC_SCALE =  'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab',
                            'A', 'Bb', 'B'
    FLAT_KEYS =  'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb',
                 'eb'

    ___ - , tonic, scale_name, pattern_ N..
        tonic tonic.capitalize()
        name tonic + ' ' + scale_name
        pattern pattern
        chromatic_scale (FLAT_CHROMATIC_SCALE
                                __ tonic __ FLAT_KEYS ____
                                CHROMATIC_SCALE)
        pitches _assign_pitches()

    ___ _assign_pitches
        __ pattern __ N..
            r.. _reorder_chromatic_scale()
        last_index 0
        pitches    # list
        scale _reorder_chromatic_scale()
        ___ i, interval __ e..(pattern
            pitches.a..(scale[last_index])
            last_index += ASCENDING_INTERVALS.i.. interval) + 1
        __ pitches[0] !_ scale[last_index % l..(scale)]:
            r.. V...()
        r.. pitches

    ___ _reorder_chromatic_scale
        index chromatic_scale.i.. tonic)
        r.. chromatic_scale[index:] + chromatic_scale[:index]
