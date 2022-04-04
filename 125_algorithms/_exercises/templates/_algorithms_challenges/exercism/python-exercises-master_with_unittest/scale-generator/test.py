_______ unittest

____ scale_generator _______ Scale


c_ ScaleGeneratorTest(unittest.TestCase

    ___ test_naming_scale
        chromatic = Scale('c', 'chromatic')
        e.. = 'C chromatic'
        a.. = chromatic.name
        assertEqual(e.., a..)

    ___ test_chromatic_scale
        chromatic = Scale('C', 'chromatic')
        e.. =  'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#',
                    'B'
        a.. = chromatic.pitches
        assertEqual(e.., a..)

    ___ test_another_chromatic_scale
        chromatic = Scale('F', 'chromatic')
        e.. =  'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb',
                    'E'
        a.. = chromatic.pitches
        assertEqual(e.., a..)

    ___ test_naming_major_scale
        major = Scale('G', 'major', 'MMmMMMm')
        e.. = 'G major'
        a.. = major.name
        assertEqual(e.., a..)

    ___ test_major_scale
        major = Scale('C', 'major', 'MMmMMMm')
        e.. =  'C', 'D', 'E', 'F', 'G', 'A', 'B'
        a.. = major.pitches
        assertEqual(e.., a..)

    ___ test_another_major_scale
        major = Scale('G', 'major', 'MMmMMMm')
        e.. =  'G', 'A', 'B', 'C', 'D', 'E', 'F#'
        a.. = major.pitches
        assertEqual(e.., a..)

    ___ test_minor_scale
        minor = Scale('f#', 'minor', 'MmMMmMM')
        e.. =  'F#', 'G#', 'A', 'B', 'C#', 'D', 'E'
        a.. = minor.pitches
        assertEqual(e.., a..)

    ___ test_another_minor_scale
        minor = Scale('bb', 'minor', 'MmMMmMM')
        e.. =  'Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab'
        a.. = minor.pitches
        assertEqual(e.., a..)

    ___ test_dorian_mode
        dorian = Scale('d', 'dorian', 'MmMMMmM')
        e.. =  'D', 'E', 'F', 'G', 'A', 'B', 'C'
        a.. = dorian.pitches
        assertEqual(e.., a..)

    ___ test_mixolydian_mode
        mixolydian = Scale('Eb', 'mixolydian', 'MMmMMmM')
        e.. =  'Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'Db'
        a.. = mixolydian.pitches
        assertEqual(e.., a..)

    ___ test_lydian_mode
        lydian = Scale('a', 'lydian', 'MMMmMMm')
        e.. =  'A', 'B', 'C#', 'D#', 'E', 'F#', 'G#'
        a.. = lydian.pitches
        assertEqual(e.., a..)

    ___ test_phrygian_mode
        phrygian = Scale('e', 'phrygian', 'mMMMmMM')
        e.. =  'E', 'F', 'G', 'A', 'B', 'C', 'D'
        a.. = phrygian.pitches
        assertEqual(e.., a..)

    ___ test_locrian_mode
        locrian = Scale('g', 'locrian', 'mMMmMMM')
        e.. =  'G', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F'
        a.. = locrian.pitches
        assertEqual(e.., a..)

    ___ test_harmonic_minor
        harmonic_minor = Scale('d', 'harmonic_minor', 'MmMMmAm')
        e.. =  'D', 'E', 'F', 'G', 'A', 'Bb', 'Db'
        a.. = harmonic_minor.pitches
        assertEqual(e.., a..)

    ___ test_octatonic
        octatonic = Scale('C', 'octatonic', 'MmMmMmMm')
        e.. =  'C', 'D', 'D#', 'F', 'F#', 'G#', 'A', 'B'
        a.. = octatonic.pitches
        assertEqual(e.., a..)

    ___ test_hexatonic
        hexatonic = Scale('Db', 'hexatonic', 'MMMMMM')
        e.. =  'Db', 'Eb', 'F', 'G', 'A', 'B'
        a.. = hexatonic.pitches
        assertEqual(e.., a..)

    ___ test_pentatonic
        pentatonic = Scale('A', 'pentatonic', 'MMAMA')
        e.. =  'A', 'B', 'C#', 'E', 'F#'
        a.. = pentatonic.pitches
        assertEqual(e.., a..)

    ___ test_enigmatic
        enigmatic = Scale('G', 'enigmatic', 'mAMMMmm')
        e.. =  'G', 'G#', 'B', 'C#', 'D#', 'F', 'F#'
        a.. = enigmatic.pitches
        assertEqual(e.., a..)

    ___ test_brokeninterval
        w__ assertRaises(V...
            Scale('G', 'enigmatic', 'mAMMMmM')


__ _____ __ _____
    unittest.main()
