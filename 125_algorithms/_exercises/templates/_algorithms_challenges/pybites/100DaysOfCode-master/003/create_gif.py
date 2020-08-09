'''Script to convert multiple images into a gif. Found out about imageio here:
http://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python'''
______ glob
______ sys

______ imageio

DURATION = 1.5
OUT_GIF = 'out.gif'
VALID_EXTENSIONS = ('png', 'jpg')


___ create_gif(filenames, duration=DURATION
    images = []
    ___ filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(OUT_GIF, images, duration=duration)


__ __name__ __ "__main__":

    script = sys.argv.pop(0)
    args = sys.argv

    __ le.(args) __ 0:
        print('Usage: {} <glob pattern or list images>'.format(script))
        sys.exit(1)

    ____ le.(args) __ 1:
        filenames = glob.glob(args[0])

    ____
        filenames = args

    __ not all(f.lower().endswith(VALID_EXTENSIONS) ___ f in filenames
        print('Only png and jpg files allowed')
        sys.exit(1)

    create_gif(filenames)
