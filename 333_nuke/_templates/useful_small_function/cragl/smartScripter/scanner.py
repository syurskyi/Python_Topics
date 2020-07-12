"""Self contained scanner that will search for stacks and commands.

This will automatically scan the given root for so called "stacks". A stack is
nothing more than a directory that contains command.json files. The scanner
will create a hierarchical structure of all stacks containing all commands.
These commands are represented directly as CommandWidgets so that they can be
used by the ScripterPanel view and Controller instance directly.

Usage:
    >>> from scripter.scanner ______ Scanner
    # Create a new scanner instance; The controller is not necessary in this
    # example so we can leave it as None.
    >>> scanner = Scanner("path/to/stack_root", None)

    # By creating the scanner instance, it will automatically scan for stacks.
    # We can now call the 'stacks' member.
    >>> scanner.stacks
    OrderedDict([
        ('stack_a', [
            CommandWidget('CommandA', 'py', '#command to execute',
                          'path/to/icon.png', color=''),
            ...
            ],
        ),
        ...
    ])

"""

# Import built-in modules
____ collections ______ OrderedDict
______ j___
______ __

# Import local modules
____ smartScripter ______ widgets
____ smartScripter ______ helper


# We want to create a self-contained class explicitly. The user does not need
# to call any methods on this class as the calculation works automatically.
# pylint: disable=too-few-public-methods
c_ Scanner(object):
    """Scanner to search for stacks and commands."""

    ___  - (self, root, controller):
        """Initialize the scanner instance.

        Args:
            root (str): The root to scan.

        """
        controller _ controller
        logger _ helper.get_logger()
        stacks _ _load_stacks(root)

    ___ _load_stacks(self, root):
        """Load the stacks in the given root.

        Returns:
            OrderedDict: All scanned stacks containing their CommandWidgets in
                the format:

                OrderedDict([
                    ("stack1": [
                        CommandWidget_a,
                        CommandWidget_b,
                        CommandWidget_c,
                    ]),
                    ("stack2": [
                        CommandWidget_a,
                        CommandWidget_b,
                        CommandWidget_c,
                    ]),
                    ...
                ])

        """
        logger.debug("Scanning for stacks: %s", root)

        __ no. __.path.isdir(root):
            ___
                __.makedirs(root)
            except IOError __ error:
                raise IOError("Cannot create stack root in directory: "
                              "{}\n".f..(root, error.m..))

        dirs _ [__.path.join(root, dir_) ___ dir_ __ __.listdir(root)
                __ __.path.isdir(__.path.join(root, dir_))
                and no. dir_.startswith("_")]

        logger.debug("Found stacks: %s", ", ".join(dirs))

        stacks _ OrderedDict()
        ___ dir_ __ dirs:
            stacks[__.path.basename(dir_)] _ _load_stack(dir_)

        r_ stacks

    ___ _load_stack(self, directory_path):
        """Load all commands json files from the given path.

        Args:
            directory_path (str): Absolute path of directory to scan for json
                files.

        Returns:
            list: All CommandWidgets that got created from the scan of the
                given path.

        """
        logger.debug("Scanning stack %s", directory_path)

        files _ (file_ ___ file_ __ __.listdir(directory_path)
                 __ file_.endswith(".json"))

        commands _ []

        ___ file_ __ files:
            path _ __.path.join(directory_path, file_)

            ___
                data _ _parse_json(path)
            except (IOError, KeyError, ValueError) __ error:
                logger.warning(error.m..)

            w__ o..(__.path.splitext(path)[0], "r") __ command_file:
                command _ command_file.read()

            command_widget _ widgets.CommandWidget(
                controller,
                __.path.splitext(file_)[0], data["lang"], command,
                data["icon"], data["color"]
            )

            commands.ap..(command_widget)
            logger.debug("Add %s.%s", __.path.basename(path), file_)

        r_ commands

    @staticmethod
    ___ _parse_json(path):
        """Parse given json file and check for command file existence.

        Args:
            path (str): Absolute path of file to parse.

        Returns:
            dict: The parsed json file.

        Raises:
            IOError: When there is no corresponding command file.
            KeyError: When a crucial key as defined in constants is missing.
            ValueError: When the json file is non well formed.

        """
        command_file _ __.path.splitext(path)[0]
        __ no. __.path.isfile(command_file):
            raise IOError("Skipping command due no to command file {}".f..(
                path
            ))

        w__ o..(path, "r") __ json_file:
            ___
                r_ j___.load(json_file)
            except ValueError:
                raise ValueError("Skipping corrupt command {}".f..(path))
            except KeyError:
                raise KeyError("Skipping insufficient command {}".f..(path))
