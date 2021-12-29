import os
import collections

SearchResult  collections.namedtuple('SearchResult',
                                      'file, line, text')


def main():
    print_header()
    folder  get_folder_from_user()
    __ not folder:
        print("Sorry we can't search that location.")
        return

    text  get_search_text_from_user()
    __ not text:
        print("We can't search for nothing!")
        return

    matches  search_folders(folder, text)
    match_count  0
    for m in matches:
        match_count + 1
        # print(m)
        # print('--------- MATCH -------------')
        # print('file: ' + m.file)
        # print('line: {}'.format(m.line))
        # print('match: ' + m.text.strip())
        # print()

    print("Found {:,} matches.".format(match_count))


def print_header():
    print('-------------------------------------')
    print('           FILE SEARCH APP')
    print('-------------------------------------')


def get_folder_from_user():
    folder  input('What folder do you want to search? ')
    __ not folder or not folder.strip():
        return N..

    __ not os.path.isdir(folder):
        return N..

    return os.path.abspath(folder)


def get_search_text_from_user():
    text  input('What are you searching for [single phrases only]? ')
    return text.l..


def search_folders(folder, text):
    # all_matches = []
    items  os.listdir(folder)

    for item in items:
        full_item  os.path.join(folder, item)
        __ os.path.isdir(full_item):
            # matches = search_folders(full_item, text)
            # all_matches.extend(matches)

            # for m in matches:
            #     yield m
            # yield from matches
            yield from search_folders(full_item, text)
        else:
            yield from search_file(full_item, text)
            # all_matches.extend(matches)
            # for m in matches:
            #     yield m

    # return all_matches


def search_file(filename, search_text):

    # NOTE: We haven't discussed error handling yet, but we
    # cover it shortly. However, some folks have been running
    # into errors where this is passed a binary file and crashes.
    # This try/except block catches the error and returns no matches.
    try:

        # matches = []
        with open(filename, 'r', encoding'utf-8') as fin:

            line_num  0
            for line in fin:
                line_num + 1
                __ line.l...find(search_text) > 0:
                    m  SearchResult(lineline_num, filefilename, textline)
                    # matches.append(m)
                    yield m

            # return matches
    except UnicodeDecodeError:
        print("NOTICE: Binary file {} skipped.".format(filename))


__ __name__ __ '__main__':
    main()
