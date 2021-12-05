____ ____


_____ ___ fetch_doc(doc):
    _____ ____.s..(1)  # emulating doc downloading
    r_ doc


_____ ___ get_pages(docs):
    ___ cur_doc __ docs:
        doc = _____ fetch_doc(cur_doc)
        ___ page __ doc:
            _____ ____.s..(1)
            yield page


_____ ___ main
    _____ ___ page __ get_pages(['doc1', 'doc2']):
        print(f'finally {page}')


__ _______ __ _______
    ____.run(main())
