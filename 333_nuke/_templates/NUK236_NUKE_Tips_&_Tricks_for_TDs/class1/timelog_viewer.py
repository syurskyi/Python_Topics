______ ?
______ __
______ getpass
______ shutil
______ j___
______ ?

CURRENT_USER = getpass.getuser()
LOG_DIR = "/Users/hugoleveille/Desktop/logs"


c_ Panel(?.PythonPanel):
    ___  - (self, name):
        s_(Panel, self). - (name)

        setMinimumSize(500,500)

        date_combo_box = ?.Enumeration_Knob("date", "Date", [])
        delete_push_button = ?.PyScript_Knob("delete", "Delete", "")
        log_knob = ?.Multiline_Eval_String_Knob("text","Log","")

        addKnob(date_combo_box)
        addKnob(delete_push_button)
        addKnob(log_knob)

        build_date_combo_box()

    ___ delete_log
        m.. = ?.ask("Are you sure you want to delete this log?")
        __ no. m..:
            r_

        date = date_combo_box.v..
        path = "%s/%s/%s" % (LOG_DIR, CURRENT_USER,date)
        shutil.rmtree(path)
        log_knob.sV..("")
        build_date_combo_box()

    ___ build_date_combo_box
        log_dir = "%s/%s" % (LOG_DIR, CURRENT_USER)
        date_combo_box.setValues(__.walk(log_dir).next()[1])

        __ date_combo_box.values():
            date_combo_box.sV..(date_combo_box.values()[0])
            build_log_text(get_log())

    ___ get_log

        date = date_combo_box.v..
        json_path = "%s/%s/%s/log.json" % (LOG_DIR, CURRENT_USER,date)
        log = j___.load(o..(json_path))
        r_ log

    ___ build_log_text(self, log):
        txt = ""
        ___ i __ log:
            ti__ = log[i]
            txt += "%s\n%s\n\n" % (i, seconds_to_str(ti__))
        log_knob.sV..(txt)

    ___ knobChanged(self, knob):

        __ knob.name() __ "date":
            build_log_text(get_log())

        __ knob.name() __ "delete":
            delete_log()

    ___ delete_log

        m.. = ?.ask("Are you sure you want to delete this log?")
        __ no. m..:
            r_

        date = date_combo_box.v..
        path = "%s/%s/%s" % (LOG_DIR, CURRENT_USER, date)
        shutil.rmtree(path)
        log_knob.sV..("")
        build_date_combo_box()

    ___ seconds_to_str(self, sec):

        minutes, seconds = divmod(sec, 60)
        hours, minutes = divmod(minutes, 60)
        r_ "%02d:%02d" % (hours, minutes)