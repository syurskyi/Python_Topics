____ ____

____ aiofiles


___ read_large_file():
    with open('..\\data\\big_file.txt', 'r') as f:
        return f.read()


_____ ___ async_read_large_file():
    _____ with aiofiles.open('..\\data\\big_file.txt', 'r') as f:
        return _____ f.read()


___ count_words(text):
    return len(text.split(' '))


_____ ___ async_main():
    text = _____ async_read_large_file()
    print(count_words(text))


___ main():
    text = read_large_file()
    print(count_words(text))


__ _______ __ _______
    ____.run(async_main())
    main()
