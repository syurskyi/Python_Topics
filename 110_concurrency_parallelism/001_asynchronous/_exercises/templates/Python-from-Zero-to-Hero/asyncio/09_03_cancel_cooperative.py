____ ____
____ threading


_____ ___ fetch_doc(doc):
    _____ ____.s..(3)  # emulating doc downloading
    print(f'{doc=}')
    r_ doc


_____ ___ get_docs(docs, token):
    pages = []
    ___ cur_doc __ docs:
        __ token.is_set():
            break
        doc = _____ fetch_doc(cur_doc)
        ___ page __ doc:
            pages.append(page)
    r_ pages


___ get_response(token):
    reply = input('Want to cancel or no? [y/n]')
    __ reply == 'y':
        token.set()


_____ ___ main():
    token = threading.Event()
    task = ____.create_task(get_docs(['doc1', 'doc2', 'doc3'], token))

    t = threading.Thread(target=get_response, args=(token,))
    t.start()

    result = _____ task
    ___ doc __ result:
        print(f'{doc}', e.._'')


__ _______ __ _______
    ____.run(main())
