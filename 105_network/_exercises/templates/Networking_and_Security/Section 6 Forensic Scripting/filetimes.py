______ __, d_t_

rootdir _ "/Users/kilroy"
searchdate _ d_t_.da__.today-d_t_.timedelta(days_3)

___ curr, dirs, files __ __.walk(rootdir

    ___ f __ files:
        ___
            pa__ _ "@/@"  (curr, f)
            t _ d_t_.da__.____timestamp(__.pa__.getmtime(pa__))
            __ (t > searchdate
                print("found date @ on file @"  (t,f))
        ______ E.. __ e:
            no_op _ 0