_______ os
_______ r__

r__.seed(30)
images  [f"{s..(i).zfill(3)}_image.{r__.choice(['png', 'jpg'])}" ___ i __ r..(1, 20)]

base_dir  'images'

__ n.. os.path.exists(base_dir):
    os.mkdir(base_dir)

png_dir  os.path.j..(base_dir, 'images_png')
jpg_dir  os.path.j..(base_dir, 'images_jpg')

__ n.. os.path.exists(png_dir):
    os.mkdir(png_dir)

__ n.. os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)

___ image __ images:
    __ image.endswith('.png'):
        open(os.path.j..(png_dir, image), 'w').close()
    ____ image.endswith('.jpg'):
        open(os.path.j..(jpg_dir, image), 'w').close()

___ root, dirs, files __ os.walk(base_dir):
    print(root)
    ___ file __ s..(files):
        print _*\t{file}')