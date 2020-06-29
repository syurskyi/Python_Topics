______ os
______ threading
______ getpass
______ datetime
______ json
______ re
______ ?
______ time

CURRENT_USER = getpass.getuser()
LOG_DIR = "/Users/hugoleveille/Desktop/logs"
TIMER = 5
IDLE_TIME = 30


c_ Timelog():

    ___ start_thread(self):

        Timelog.thread = threading.Timer( TIMER, self.write_json)
        Timelog.thread.setDaemon(True)
        Timelog.thread.start()

    ___ get_json(self):
        date = datetime.datetime.today().strftime("%Y-%m-%d")
        json_dir = "%s/%s/%s" % (LOG_DIR, CURRENT_USER, date)
        __ not os.path.exists(json_dir):
            os.makedirs(json_dir)

        self.json_path = "%s/log.json" % json_dir
        __ not os.path.exists(self.json_path):
            data = {}
        ____
            _file = open(self.json_path, "r")
            data = json.load(_file)

        return data

    ___ write_json(self):

        self.script_path = ?.root()['name'].value()

        regex = re.search( r"projects/(\w+)/shots/(\w+)", self.script_path)
        __ regex:
            shot = "%s_%s" % (regex.group(1), regex.group(2))
        ____
            print "Invalid Path"
            self.start_thread()
            return

        __ self.idle_time() > IDLE_TIME:
            print "Script is idle"
            self.start_thread()
            return


        data = self.get_json()

        __ data.has_key(shot):
            data[shot] += TIMER
        ____
            data[shot] = TIMER

        _file = open(self.json_path, "w")
        json.dump(data, _file)
        print data
        self.start_thread()

    ___ idle_time(self):

        now = time.time()
        autosave_path = "%s.autosave" % self.script_path

        #1)  If there is an autosave file, we compare it's last modified time to the local time

        __ os.path.isfile( autosave_path):
            modification_time = int(os.stat( autosave_path).st_mtime)
            _idle_time = now - modification_time

        #2) If nuke is modified and there is no autosave file, it means the user has modified he's script just after
        #saving it. So we consider the script not idle

        elif ?.modified():
            __ not os.path.isfile(autosave_path):
                _idle_time = 0

        #3) If there is no autosave file and nuke is not modified, we compare current time to the modification time of
        # the nuke script

        elif not ?.modified():
            modification_time = int(os.stat( self.script_path).st_mtime)
            _idle_time = now - modification_time

        print _idle_time
        return _idle_time