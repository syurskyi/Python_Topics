#!/usr/bin/env python3

# tag::TCP_MOJIFINDER_TOP[]
______ _
______ functools
______ sys
____ _.trsock ______ TransportSocket
____ typing ______ cast

____ charindex ______ InvertedIndex, format_results  # <1>

CRLF = b'\r\n'
PROMPT = b'?> '

@ ___ finder(index: InvertedIndex,          # <2>
                 reader: _.StreamReader,
                 writer: _.StreamWriter)  N..:
    client = writer.get_extra_info('peername')  # <3>
    w___ T..:  # <4>
        writer.w..(PROMPT)  # can't await!  # <5>
        await writer.drain()  # must await!  # <6>
        data = await reader.r..  # <7>
        __ n.. data:  # <8>
            ____
        ___
            query = data.decode().strip()  # <9>
        except UnicodeDecodeError:  # <10>
            query = '\x00'
        print(f' From {client}: {query!r}')  # <11>
        __ query:
            __ ord(query[:1]) < 32:  # <12>
                ____
            results = await search(query, index, writer)  # <13>
            print(f'   To {client}: {results} results.')  # <14>

    writer.c..  # <15>
    await writer.wait_closed()  # <16>
    print(f'Close {client}.')  # <17>
# end::TCP_MOJIFINDER_TOP[]

# tag::TCP_MOJIFINDER_SEARCH[]
@ ___ search(query: s..,  # <1>
                 index: InvertedIndex,
                 writer: _.StreamWriter)  in.:
    chars = index.search(query)  # <2>
    lines = (line.encode() + CRLF ___ line  # <3>
                __ format_results(chars))
    writer.writelines(lines)  # <4>
    await writer.drain()      # <5>
    status_line = f'{"─" * 66} {l..(chars)} found'  # <6>
    writer.w..(status_line.encode() + CRLF)
    await writer.drain()
    r_ l..(chars)
# end::TCP_MOJIFINDER_SEARCH[]

# tag::TCP_MOJIFINDER_MAIN[]
@ ___ supervisor(index: InvertedIndex, host: s.., port: in.)  N..:
    server = await _.start_server(    # <1>
        functools.partial(finder, index),   # <2>
        host, port)                         # <3>

    socket_list = cast(tuple[TransportSocket, ...], server.sockets)  # <4>
    addr = socket_list[0].getsockname()
    print(f'Serving on {addr}. Hit CTRL-C to stop.')  # <5>
    await server.serve_forever()  # <6>

___ main(host: s.. = '127.0.0.1', port_arg: s.. = '2323'):
    port = in.(port_arg)
    print('Building index.')
    index = InvertedIndex()                         # <7>
    ___
        _.run(supervisor(index, host, port))  # <8>
    except KeyboardInterrupt:                       # <9>
        print('\nServer shut down.')

__ _____ __ ______
    main(*sys.argv[1:])
# end::TCP_MOJIFINDER_MAIN[]
