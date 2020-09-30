class Scale(object

    ASCENDING_INTERVALS = ['m', 'M', 'A']
    CHROMATIC_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A',
                       'A#', 'B']
    FLAT_CHROMATIC_SCALE = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab',
                            'A', 'Bb', 'B']
    FLAT_KEYS = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb',
                 'eb']

    ___ __init__(self, tonic, scale_name, pattern=None
        self.tonic = tonic.capitalize()
        self.name = self.tonic + ' ' + scale_name
        self.pattern = pattern
        self.chromatic_scale = (self.FLAT_CHROMATIC_SCALE
                                __ tonic __ self.FLAT_KEYS else
                                self.CHROMATIC_SCALE)
        self.pitches = self._assign_pitches()

    ___ _assign_pitches(self
        __ self.pattern pa__ None:
            r_ self._reorder_chromatic_scale()
        last_index = 0
        pitches =   # list
        scale = self._reorder_chromatic_scale()
        ___ i, interval __ enumerate(self.pattern
            pitches.append(scale[last_index])
            last_index += self.ASCENDING_INTERVALS.index(interval) + 1
        __ pitches[0] != scale[last_index % le.(scale)]:
            raise ValueError()
        r_ pitches

    ___ _reorder_chromatic_scale(self
        index = self.chromatic_scale.index(self.tonic)
        r_ self.chromatic_scale[index:] + self.chromatic_scale[:index]
