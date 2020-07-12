______ ?
______ __
______ getpass
______ shutil
______ j___
______ ?

CURRENT_USER _ getpass.getuser()
LOG_DIR _ "/Users/hugoleveille/Desktop/logs"


c_ Panel(?.PythonPanel):
    ___  - (self, name):
        s_(Panel, self). - (name)

        setMinimumSize(500,500)

        date_combo_box _ ?.E_K..("date", "Date", [])
        delete_push_button _ ?.PS_K..("delete", "Delete", "")
        log_knob _ ?.Multiline_Eval_String_Knob("text","Log","")

        aK..(date_combo_box)
        aK..(delete_push_button)
        aK..(log_knob)

        build_date_combo_box()

    ___ delete_log
        m.. _ ?.ask("Are you sure you want to delete this log?")
        __ no. m..:
            r_

        date _ date_combo_box.v..
        path _ "@/@/@" % (LOG_DIR, CURRENT_USER,date)
        shutil.rmtree(path)
        log_knob.sV..("")
        build_date_combo_box()

    ___ build_date_combo_box
        log_dir _ "@/@" % (LOG_DIR, CURRENT_USER)
        date_combo_box.setValues(__.walk(log_dir).next()[1])

        __ date_combo_box.values():
            date_combo_box.sV..(date_combo_box.values()[0])
            build_log_text(get_log())

    ___ get_log

        date _ date_combo_box.v..
        json_path _ "@/@/@/log.json" % (LOG_DIR, CURRENT_USER,date)
        log _ j___.load(o..(json_path))
        r_ log

    ___ build_log_text(self, log):
        txt _ ""
        ___ i __ log:
            ti__ _ log[i]
            txt +_ "@\n@\n\n" % (i, seconds_to_str(ti__))
        log_knob.sV..(txt)

    ___ knobChanged(self, knob):

        __ knob.name() __ "date":
            build_log_text(get_log())

        __ knob.name() __ "delete":
            delete_log()

    ___ delete_log

        m.. _ ?.ask("Are you sure you want to delete this log?")
        __ no. m..:
            r_

        date _ date_combo_box.v..
        path _ "@/@/@" % (LOG_DIR, CURRENT_USER, date)
        shutil.rmtree(path)
        log_knob.sV..("")
        build_date_combo_box()

    ___ seconds_to_str(self, sec):

        minutes, seconds _ divmod(sec, 60)
        hours, minutes _ divmod(minutes, 60)
        r_ "%02d:%02d" % (hours, minutes)