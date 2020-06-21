____ setuptools ______ setup, find_packages

setup(
    name_'QTicTacToe',
    version_'1.0',
    author_'Alan D Moore',
    author_email_'alandmoore@example.com',
    description_'The classic game of noughts and crosses',
    url_"http://qtictactoe.example.com",
    license_'MIT',
    long_description_open('README.rst', 'r').r..,
    keywords_'game multiplayer example pyqt5',
    project_urls_{
        'Author Website': 'https://www.alandmoore.com',
        'Publisher Website': 'https://packtpub.com',
        'Source Code': 'https://git.example.com/qtictactoe'
    },
    #packages=['qtictactoe', 'qtictactoe.images'],
    packages_find_packages(),
    install_requires_['PyQt5 >= 5.12'],
    python_requires_'>=3.7',
    #extras_require={
    #    "NetworkPlay": ["requests"]
    #},
    #include_package_data=True,
    package_data_{
        'qtictactoe.images': ['*.png'],
        '': ['*.txt', '*.rst']
    },
    entry_points_{
        'console_scripts': [
            'qtictactoe = qtictactoe:main'
        ]
    }
)
