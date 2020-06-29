import nuke
import os
import getpass
import shutil
import json
import nukescripts

CURRENT_USER = getpass.getuser()
LOG_DIR = "/Users/hugoleveille/Desktop/logs"


class Panel(nukescripts.PythonPanel):
    def __init__(self, name):
        super(Panel, self).__init__(name)

        self.setMinimumSize(500,500)

        self.date_combo_box = nuke.Enumeration_Knob("date", "Date", [])
        self.delete_push_button = nuke.PyScript_Knob("delete", "Delete", "")
        self.log_knob = nuke.Multiline_Eval_String_Knob("text","Log","")

        self.addKnob(self.date_combo_box)
        self.addKnob(self.delete_push_button)
        self.addKnob(self.log_knob)

        self.build_date_combo_box()

    def delete_log(self):
        message = nuke.ask("Are you sure you want to delete this log?")
        if not message:
            return

        date = self.date_combo_box.value()
        path = "%s/%s/%s" % (LOG_DIR, CURRENT_USER,date)
        shutil.rmtree(path)
        self.log_knob.setValue("")
        self.build_date_combo_box()

    def build_date_combo_box(self):
        log_dir = "%s/%s" % (LOG_DIR, CURRENT_USER)
        self.date_combo_box.setValues(os.walk(log_dir).next()[1])

        if self.date_combo_box.values():
            self.date_combo_box.setValue(self.date_combo_box.values()[0])
            self.build_log_text(self.get_log())

    def get_log(self):

        date = self.date_combo_box.value()
        json_path = "%s/%s/%s/log.json" % (LOG_DIR, CURRENT_USER,date)
        log = json.load(open(json_path))
        return log

    def build_log_text(self, log):
        txt = ""
        for i in log:
            time = log[i]
            txt += "%s\n%s\n\n" % (i, self.seconds_to_str(time))
        self.log_knob.setValue(txt)

    def knobChanged(self, knob):

        if knob.name() == "date":
            self.build_log_text(self.get_log())

        if knob.name() == "delete":
            self.delete_log()

    def delete_log(self):

        message = nuke.ask("Are you sure you want to delete this log?")
        if not message:
            return

        date = self.date_combo_box.value()
        path = "%s/%s/%s" % (LOG_DIR, CURRENT_USER, date)
        shutil.rmtree(path)
        self.log_knob.setValue("")
        self.build_date_combo_box()

    def seconds_to_str(self, sec):

        minutes, seconds = divmod(sec, 60)
        hours, minutes = divmod(minutes, 60)
        return "%02d:%02d" % (hours, minutes)