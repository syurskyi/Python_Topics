____ pathlib _______ PosixPath
_______ difflib
_______ os


___ get_matching_files(directory: PosixPath, filter_str: str) -> l..:
    """Get all file names in "directory" and (case insensitive) match the ones
       that exactly match "filter_str"

       In case there is no exact match, return closely matching files.
       If there are no closely matching files either, return an empty list.
       (Return file names, not full paths).

       For example:

       d = Path('.')
       files in dir: bite1 test output

       get_matching_files(d, 'bite1') => ['bite1']
       get_matching_files(d, 'Bite') => ['bite1']
       get_matching_files(d, 'pybites') => ['bite1']
       get_matching_files(d, 'test') => ['test']
       get_matching_files(d, 'test2') => ['test']
       get_matching_files(d, 'output') => ['output']
       get_matching_files(d, 'o$tput') => ['output']
       get_matching_files(d, 'nonsense') => []
    """


    
    exact_matches    # list
    close_matches    # list
    
    files = os.listdir(directory)
    ___ file __ files:

        __ file.lower() __ filter_str:
            exact_matches.a..(file)
    
        
    __ exact_matches:
        r.. exact_matches


    close_matches = difflib.get_close_matches(filter_str,(file.lower() ___ file __ files))
    r.. close_matches






