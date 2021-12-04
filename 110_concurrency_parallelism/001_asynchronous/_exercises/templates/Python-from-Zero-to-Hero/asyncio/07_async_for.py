____ ____


_____ ___ fetch_doc(doc):
    _____ ____.s..(1)  # emulating doc downloading
    return doc


_____ ___ get_pages(docs):
    for cur_doc in docs:
        doc = _____ fetch_doc(cur_doc)
        for page in doc:
            _____ ____.s..(1)
            yield page


_____ ___ main():
    _____ for page in get_pages(['doc1', 'doc2']):
        print(f'finally {page}')


__ _______ __ _______
    ____.run(main())
