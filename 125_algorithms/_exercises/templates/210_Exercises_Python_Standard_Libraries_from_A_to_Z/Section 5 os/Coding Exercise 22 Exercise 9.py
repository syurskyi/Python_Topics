_______ os
_______ random

random.seed(30)
images  [f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}" ___ i __ r..(1, 20)]

base_dir  'images'
png_dir  os.path.join(base_dir, 'images_png')
jpg_dir  os.path.join(base_dir, 'images_jpg')

__ n.. os.path.exists(base_dir):
    os.mkdir(base_dir)

__ n.. os.path.exists(png_dir):
    os.mkdir(png_dir)

__ n.. os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)

___ image __ images:
    __ image.endswith('.png'):
        open(os.path.join(png_dir, image), 'w').close()
    ____ image.endswith('.jpg'):
        open(os.path.join(jpg_dir, image), 'w').close()

___ root, dirs, files __ os.walk(base_dir):
    ___ file __ s..(files):
        print(file)