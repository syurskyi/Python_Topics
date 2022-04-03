_______ unittest

____ scale_generator _______ Scale


c_ ScaleGeneratorTest(unittest.TestCase

    ___ test_naming_scale
        chromatic = Scale('c', 'chromatic')
        expected = 'C chromatic'
        actual = chromatic.name
        assertEqual(expected, actual)

    ___ test_chromatic_scale
        chromatic = Scale('C', 'chromatic')
        expected =  'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#',
                    'B'
        actual = chromatic.pitches
        assertEqual(expected, actual)

    ___ test_another_chromatic_scale
        chromatic = Scale('F', 'chromatic')
        expected =  'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb',
                    'E'
        actual = chromatic.pitches
        assertEqual(expected, actual)

    ___ test_naming_major_scale
        major = Scale('G', 'major', 'MMmMMMm')
        expected = 'G major'
        actual = major.name
        assertEqual(expected, actual)

    ___ test_major_scale
        major = Scale('C', 'major', 'MMmMMMm')
        expected =  'C', 'D', 'E', 'F', 'G', 'A', 'B'
        actual = major.pitches
        assertEqual(expected, actual)

    ___ test_another_major_scale
        major = Scale('G', 'major', 'MMmMMMm')
        expected =  'G', 'A', 'B', 'C', 'D', 'E', 'F#'
        actual = major.pitches
        assertEqual(expected, actual)

    ___ test_minor_scale
        minor = Scale('f#', 'minor', 'MmMMmMM')
        expected =  'F#', 'G#', 'A', 'B', 'C#', 'D', 'E'
        actual = minor.pitches
        assertEqual(expected, actual)

    ___ test_another_minor_scale
        minor = Scale('bb', 'minor', 'MmMMmMM')
        expected =  'Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab'
        actual = minor.pitches
        assertEqual(expected, actual)

    ___ test_dorian_mode
        dorian = Scale('d', 'dorian', 'MmMMMmM')
        expected =  'D', 'E', 'F', 'G', 'A', 'B', 'C'
        actual = dorian.pitches
        assertEqual(expected, actual)

    ___ test_mixolydian_mode
        mixolydian = Scale('Eb', 'mixolydian', 'MMmMMmM')
        expected =  'Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'Db'
        actual = mixolydian.pitches
        assertEqual(expected, actual)

    ___ test_lydian_mode
        lydian = Scale('a', 'lydian', 'MMMmMMm')
        expected =  'A', 'B', 'C#', 'D#', 'E', 'F#', 'G#'
        actual = lydian.pitches
        assertEqual(expected, actual)

    ___ test_phrygian_mode
        phrygian = Scale('e', 'phrygian', 'mMMMmMM')
        expected =  'E', 'F', 'G', 'A', 'B', 'C', 'D'
        actual = phrygian.pitches
        assertEqual(expected, actual)

    ___ test_locrian_mode
        locrian = Scale('g', 'locrian', 'mMMmMMM')
        expected =  'G', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F'
        actual = locrian.pitches
        assertEqual(expected, actual)

    ___ test_harmonic_minor
        harmonic_minor = Scale('d', 'harmonic_minor', 'MmMMmAm')
        expected =  'D', 'E', 'F', 'G', 'A', 'Bb', 'Db'
        actual = harmonic_minor.pitches
        assertEqual(expected, actual)

    ___ test_octatonic
        octatonic = Scale('C', 'octatonic', 'MmMmMmMm')
        expected =  'C', 'D', 'D#', 'F', 'F#', 'G#', 'A', 'B'
        actual = octatonic.pitches
        assertEqual(expected, actual)

    ___ test_hexatonic
        hexatonic = Scale('Db', 'hexatonic', 'MMMMMM')
        expected =  'Db', 'Eb', 'F', 'G', 'A', 'B'
        actual = hexatonic.pitches
        assertEqual(expected, actual)

    ___ test_pentatonic
        pentatonic = Scale('A', 'pentatonic', 'MMAMA')
        expected =  'A', 'B', 'C#', 'E', 'F#'
        actual = pentatonic.pitches
        assertEqual(expected, actual)

    ___ test_enigmatic
        enigmatic = Scale('G', 'enigmatic', 'mAMMMmm')
        expected =  'G', 'G#', 'B', 'C#', 'D#', 'F', 'F#'
        actual = enigmatic.pitches
        assertEqual(expected, actual)

    ___ test_brokeninterval
        w__ assertRaises(V...
            Scale('G', 'enigmatic', 'mAMMMmM')


__ _____ __ _____
    unittest.main()
