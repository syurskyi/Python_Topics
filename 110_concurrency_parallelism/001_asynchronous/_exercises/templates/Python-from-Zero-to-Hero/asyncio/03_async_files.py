____ ____

____ aiofiles


___ read_large_file():
    w___ open('..\\data\\big_file.txt', 'r') __ f:
        r_ f.read()


_____ ___ async_read_large_file():
    _____ w___ aiofiles.open('..\\data\\big_file.txt', 'r') __ f:
        r_ _____ f.read()


___ count_words(text):
    r_ len(text.split(' '))


_____ ___ async_main():
    text = _____ async_read_large_file()
    print(count_words(text))


___ main():
    text = read_large_file()
    print(count_words(text))


__ _______ __ _______
    ____.run(async_main())
    main()
