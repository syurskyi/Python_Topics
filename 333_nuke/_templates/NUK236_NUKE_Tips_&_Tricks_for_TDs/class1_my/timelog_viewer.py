______ ?
______ os
______ getpass
______ shutil
______ json
______ nukescripts

CURRENT_USER = getpass.getuser()
LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')


class Panel(nukescripts.PythonPanel):
    ___ __init__(self, name):
        super(Panel, self).__init__(name)

        self.setMinimumSize(500,500)

        self.date_combo_box = ?.Enumeration_Knob("date", "Date", [])
        self.delete_push_button = ?.PyScript_Knob("delete", "Delete", "")
        self.log_knob = ?.Multiline_Eval_String_Knob("text","Log","")

        self.addKnob(self.date_combo_box)
        self.addKnob(self.delete_push_button)
        self.addKnob(self.log_knob)

        self.build_date_combo_box()

    ___ delete_log(self):
        message = ?.ask("Are you sure you want to delete this log?")
        __ not message:
            return

        date = self.date_combo_box.value()
        path = "%s/%s/%s" % (LOG_DIR, CURRENT_USER,date)
        shutil.rmtree(path)
        self.log_knob.sV..("")
        self.build_date_combo_box()

    ___ build_date_combo_box(self):
        log_dir = "%s/%s" % (LOG_DIR, CURRENT_USER)
        self.date_combo_box.setValues(os.walk(log_dir).next()[1])

        __ self.date_combo_box.values():
            self.date_combo_box.sV..(self.date_combo_box.values()[0])
            self.build_log_text(self.get_log())

    ___ get_log(self):

        date = self.date_combo_box.value()
        json_path = "%s/%s/%s/log.json" % (LOG_DIR, CURRENT_USER,date)
        log = json.load(open(json_path))
        return log

    ___ build_log_text(self, log):
        txt = ""
        ___ i __ log:
            time = log[i]
            txt += "%s\n%s\n\n" % (i, self.seconds_to_str(time))
        self.log_knob.sV..(txt)

    ___ knobChanged(self, knob):

        __ knob.name() == "date":
            self.build_log_text(self.get_log())

        __ knob.name() == "delete":
            self.delete_log()

    ___ delete_log(self):

        message = ?.ask("Are you sure you want to delete this log?")
        __ not message:
            return

        date = self.date_combo_box.value()
        path = "%s/%s/%s" % (LOG_DIR, CURRENT_USER, date)
        shutil.rmtree(path)
        self.log_knob.sV..("")
        self.build_date_combo_box()

    ___ seconds_to_str(self, sec):

        minutes, seconds = divmod(sec, 60)
        hours, minutes = divmod(minutes, 60)
        return "%02d:%02d" % (hours, minutes)