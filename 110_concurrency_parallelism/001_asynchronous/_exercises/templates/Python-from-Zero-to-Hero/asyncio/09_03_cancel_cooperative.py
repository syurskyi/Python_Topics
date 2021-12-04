____ ____
____ threading


_____ ___ fetch_doc(doc):
    _____ ____.s..(3)  # emulating doc downloading
    print(f'{doc=}')
    return doc


_____ ___ get_docs(docs, token):
    pages = []
    for cur_doc in docs:
        if token.is_set():
            break
        doc = _____ fetch_doc(cur_doc)
        for page in doc:
            pages.append(page)
    return pages


___ get_response(token):
    reply = input('Want to cancel or no? [y/n]')
    if reply == 'y':
        token.set()


_____ ___ main():
    token = threading.Event()
    task = ____.create_task(get_docs(['doc1', 'doc2', 'doc3'], token))

    t = threading.Thread(target=get_response, args=(token,))
    t.start()

    result = _____ task
    for doc in result:
        print(f'{doc}', end='')


__ _______ __ _______
    ____.run(main())
