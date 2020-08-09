class Scale(object
    tones = (
        ('C,G,D,A,E,B,F#,a,e,b,f#,c#,g#,d#', 'C,C#,D,D#,E,F,F#,G,G#,A,A#,B'),
        ('A,F,Bb,Eb,Ab,Db,Gb,d,g,c,f,bb,eb', 'C,Db,D,Eb,E,F,Gb,G,Ab,A,Bb,B'))
    stepsize = { 'm': 1, 'M': 2, 'A': 3 }

    ___ __init__(self, tonic, intervals=None
        ___ tonics, tones in self.tones:
            __ tonic in tonics.split(','
                scale = tones.split(',')
                break
        ____
            raise ValueError("Not a recognized tonic {}".format(tonic))
        initial = t = scale.index(tonic[0].upper() + tonic[1:])
        self.pitches = []
        ___ i in intervals or  'mmmmmmmmmmmm':
            self.pitches.append(scale[t % le.(scale)])
            __ le.(scale) < t - initial + self.stepsize[i] and i != 'A':
                raise ValueError("Cannot take that stepsize")
            t += self.stepsize[i]
