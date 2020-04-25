____ winappdbg ______ *

w__ Debug ( bKillOnExit _ T.. ) __ dbg:
    dbg.execl("calc.exe")

    w__ dbg:
        ___
            dbg.wait(1000)
        ______ E.. __ e:
            print(e)

        ___
            dbg.dispatch
        f..
            dbg.cont

cmdDbg _ Debug
cmdDbg.system.scan_processes
    # let's look for cmd.exe processes
___ ( proc, name ) __ cmdDbg.system.find_processes_by_filename( 'cmd.exe'
    # print out the process ID and the name of the process
    print proc.get_pid, name
