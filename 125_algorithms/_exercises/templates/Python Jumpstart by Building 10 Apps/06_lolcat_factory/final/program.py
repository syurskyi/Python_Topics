_______ os
_______ platform
_______ subprocess

_______ cat_service


___ main
    print_header()
    folder  get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)


___ print_header
    print('----------------------------------')
    print('        CAT FACTORY')
    print('----------------------------------')
    print()


___ get_or_create_output_folder
    base_folder  os.path.abspath(os.path.dirname(__file__))
    folder  'cat_pictures'
    full_path  os.path.j..(base_folder, folder)

    __ n.. os.path.exists(full_path) o. n.. os.path.isdir(full_path):
        print('Creating new directory at {}'.f..(full_path))
        os.mkdir(full_path)

    r.. full_path


___ download_cats(folder):
    print('Contacting server to download cats...')
    cat_count  8
    ___ i __ r..(1, cat_count + 1):
        name  'lolcat_{}'.f..(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)

    print("done.")


___ display_cats(folder):
    # open folder
    print('Displaying cats in OS window.')
    __ platform.system() __ 'Darwin':
        subprocess.call(['open', folder])
    ____ platform.system() __ 'Windows':
        subprocess.call(['explorer', folder])
    ____ platform.system() __ 'Linux':
        subprocess.call(['xdg-open', folder])
    ____:
        print("We don't support your os: " + platform.system())


__ _____ __ _____
    main()
