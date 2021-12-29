_______ os

base_dir  'images'
png_dir  os.path.join(base_dir, 'images_png')
jpg_dir  os.path.join(base_dir, 'images_jpg')

__ n.. os.path.exists(base_dir):
    os.mkdir(base_dir)

__ n.. os.path.exists(png_dir):
    os.mkdir(png_dir)

__ n.. os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)

___ root, dirs, files __ os.walk(base_dir):
    print(root)