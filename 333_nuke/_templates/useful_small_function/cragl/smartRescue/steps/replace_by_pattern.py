r"""Replace sections in the working file by using regular expression patterns.

This will search the working file for given patterns and will replace it with
the given substitution.

Args:
    replace (list of list): Input that will be replaced to the given output
        in the format:
        [
            [<input search>, <output>],
            [<input search>, <output>],
        ]

Examples:

Standard:
    1) This will change the colorManagement from 'Nuke' to OCIO and the
    'workingSpaceLUT' from 'Cineon' to 'linear':

    colorManagement Nuke -> colorManagement OCIO
    workingSpaceLUT Cineon -> workingSpaceLUT linear

    ---------------------------------------------------------------------------
    2) Replace all sections where finding the word 'robot' followed by any
    number and a dot and a file extension to 'robot.jpg':

    robot\d+\.[a-z]+ -> robot.jpg

    ---------------------------------------------------------------------------

    3) Remove all custom custom knobs that contain the label 'reveal in
    explorer'.

    addUserKnob\s*.*\"reveal in explorer.*" ->

Advanced:
    1) This will change the colorManagement from 'Nuke' to OCIO and the
    'workingSpaceLUT' from 'Cineon' to 'linear':

    {
        "replace": [
            ["colorManagement Nuke": "colorManagement OCIO"],
            ["workingSpaceLUT Cineon": "workingSpaceLUT linear"]
        ]
    }

    ---------------------------------------------------------------------------
    2) Replace all sections where finding the word 'robot' followed by any
    number and a dot and a file extension to 'robot.jpg':

    {
        "replace": [
            ["robot\d+\.[a-z]+", "robot.jpg"]
        ]
    }

    ---------------------------------------------------------------------------

    3) Remove all custom custom knobs that contain the label 'reveal in
    explorer'.

    {
        "replace": [
            ["addUserKnob\s*.*\"reveal in explorer.*", ""]
        ]
    }

"""

# _____ built-in modules
______ re

# _____ local modules
____ smartRescue.base_steps ______ BaseStep


c_ ReplaceByPattern(BaseStep):
    """Replace sections in the working file by searching using patterns."""

    ___ process
        """Process the file removing illegal characters."""
        w__ o..(pa__, "r") __ src:
            content _ src.read()

        ___ rule __ setup["replace"]:
            pattern _ rule[0]
            substitution _ rule[1]

            logger.info("Replace '@' with '@'", pattern, substitution)
            content _ re.sub(pattern, substitution, content)

        w__ o..(pa__, "w") __ dest:
            dest.w..(content)
