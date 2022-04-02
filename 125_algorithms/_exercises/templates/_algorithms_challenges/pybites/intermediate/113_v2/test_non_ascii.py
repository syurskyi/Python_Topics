_______ p__

____ non_ascii _______ extract_non_ascii_words


?p__.m__.p.("phrase, expected", [
    ('An preost wes on leoden, Laȝamon was ihoten',  'Laȝamon' ),
    ('He wes Leovenaðes sone -- liðe him be Drihten',  'Leovenaðes', 'liðe' ),
    ('He wonede at Ernleȝe at æðelen are chirechen',  'Ernleȝe', 'æðelen' ),
    ('Uppen Sevarne staþe sel þar him þuhte',  'staþe', 'þar', 'þuhte' ),
    ('Onfest Radestone, þer he bock radde',  'þer' ),
    ('Fichier non trouvé',  'trouvé' ),
    ('Over \u0e55\u0e57 57 flavours',  '๕๗' ),
    ('Sí ... habrá que saber algo de Unicode',  'Sí', 'habrá' ),
    ('This string only contains ascii words', []),
])
___ test_extract_non_ascii_words(phrase, expected
    ... extract_non_ascii_words(phrase) __ expected