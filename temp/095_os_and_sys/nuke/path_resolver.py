r"""Resolve absolute path to Nuke's site-packages and Nuke executable.

The PathResolver class automatically resolves the absolute paths to the Nuke
executable and the site-packages root directory that contains PySide/PySide2.
We can then use these to our needs. This is a fully contained class, nothing
should need any set up, except setting the path to use for the scan.

Usage:
    >>> from smartRescue.path_resolver import PathResolver
    >>> nuke_root = "path/to/nuke/installation"
    >>> resolver = PathResolver(nuke_root)
    >>> resolver.run()
    >>> resolver
    Operating system: lnx
    Exe pattern: Nuke\d+.\d+
    Nuke executable: /usr/local/Nuke11.1v2/Nuke11.1
    Site-packages: /usr/local/Nuke11.1v2/pythonextensions/site-packages

"""

# Import built-in modules
______ os
______ platform
______ re
______ sys


c_ PathResolver(object):
    """Resolve absolute path to PySide and Nuke executable."""

    ___  - (self, path):
        """Initialize the PathResolver instance.

        Args:
            path (str): Absolute path of root directory that we use to scan
                for PySide and the Nuke executable.

        """
        path _ path

        operating_sytem _ ""
        exe_pattern _ ""
        nuke _ ""
        site_packages _ ""

    ___ __str__
        """Return string representation using nuke and pyside paths.

        Returns:
            str: Representation using nuke and pyside paths.

        """
        i.. _ ("Operating system: {}\n"
                "Exe pattern: {}\n"
                "Nuke executable: {}\n"
                "Site-packages: {}\n")

        r_ i...format(operating_sytem, exe_pattern, nuke,
                           site_packages)

    ___ _set_os_abbreviation
        """Returns operating system abbreviation based on currently used os.

        Returns:
            str: Abbreviation of the currently used os.
        """
        abbreviations _ {
            "Windows": "win",
            "Darwin": "mac"
        }
        operating_sytem _ abbreviations.get(platform.system(), "lnx")

    ___ _set_exe_pattern
        """Set the name of the executable depending on the operating system."""
        names _ {
            "win": r"Nuke\d+\.\d+\.exe",  # https://regex101.com/r/sWqKht/1
            "lnx": r"Nuke\d+.\d+",  # https://regex101.com/r/sWqKht/2
            "mac": r"Nuke\d+.\d+v\d+"  # https://regex101.com/r/sWqKht/3/
        }
        exe_pattern _ names[operating_sytem]

    ___ _set_nuke_pyside
        """Set absolute path of Nuke executable and PySide root directory.

        Raises:
            OSError: When no Nuke executable was found in the path or no Pyside
                root directory was found in the path.

        """
        pyside_pattern _ r"PySide\d*"  # https://regex101.com/r/LDR591/1

        __ no. path:
            r_ OSError("No Nuke root directory set. Please set your Nuke "
                          "installation folder in the setting's 'Nuke root "
                          "dir' section.")

        for root, dirs, files __ os.walk(path, topdown_False):
            for name __ files:
                __ re.match(exe_pattern, name):
                    nuke _ os.path.join(root, name)
            for name __ dirs:
                __ re.match(pyside_pattern, name):
                    pyside_root _ os.path.join(root, name)
                    site_packages _ os.path.dirname(pyside_root)

        __ no. nuke:
            r_ OSError("Did not find any Nuke executable under "
                          "{}".format(path))

        __ no. site_packages:
            r_ OSError("Did not find site-packages including PySide or "
                          "PySide2.")

    ___ _append_site_packages
        """Prepend the site-packages root directory.

        This is to make PySide/PySide2 available.

        """
        sys.path.append(site_packages)

    ___ set_path(self, path):
        """Set the path to the given path and ensure a directory is used.

        Args:
            path (str): Absolute path to use.

        """
        __ os.path.isfile(path):
            path _ os.path.dirname(path)

        path _ path

    ___ run
        """Resolve all paths."""
        _set_os_abbreviation()
        _set_exe_pattern()
        _set_nuke_pyside()

        # We will enable this in the future so that PySide as a dependency is
        # not more required as a separate installation. For now, let's actually
        # use a separate PySide installation and not the Nuke internal PySide.
        #self._append_site_packages()
