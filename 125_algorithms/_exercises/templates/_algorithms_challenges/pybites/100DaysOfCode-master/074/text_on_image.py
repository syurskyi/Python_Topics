______ os
______ textwrap

from PIL ______ Image, ImageDraw, ImageFont
______ requests

FONT_SIZE = 30
FONT = ImageFont.truetype('opensans.ttf', FONT_SIZE)
TEXT_COLOR = (0, 0, 0, 255)  # black, 100% opacity
OVERLAY_COLOR = (255, 255, 255, 178)  # white, ~70% opacity
TEXT_OFFSET = (20, 20)
TEXT_CHAR_LIMIT = 250
RESIZE_WIDTH = 500
TEXT_WIDTH = 30  # experimental
IN_FILE = 'input.png'
OUT_FILE = 'output.png'


___ download_url(url, in_file=IN_FILE, chunk_size=2000
    print('Downloading {}'.format(url))
    r = requests.get(url, stream=True)
    print('Saving as {}'.format(in_file))

    with open(in_file, 'wb') as fd:
        ___ chunk in r.iter_content(chunk_size
            fd.write(chunk)

    r_ in_file


___ get_input(prompt
    # https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-user
    print(prompt)
    lines = []
    w___ True:
        line = input()
        __ line:
            line = textwrap.fill(line, width=TEXT_WIDTH)
            lines.append(line)
        ____
            break
    r_ '\n\n'.join(lines)


___ _resize(img
    basewidth = RESIZE_WIDTH
    wpercent = basewidth / float(img.size[0])
    hsize = int(float(img.size[1]) * float(wpercent))
    r_ img.resize((basewidth, hsize), Image.ANTIALIAS)


___ create_img_with_text(base_img, input_text, out_file=OUT_FILE
    base = Image.open(base_img).convert('RGBA')
    base = _resize(base)

    txt = Image.new('RGBA', base.size, OVERLAY_COLOR)

    draw_context = ImageDraw.Draw(txt)
    draw_context.text(TEXT_OFFSET, input_text, font=FONT, fill=TEXT_COLOR)

    out = Image.alpha_composite(base, txt)
    out.save(out_file)

    r_ out_file


__ __name__ __ '__main__':
    resource = input('Image file (local or url to download ')

    __ os.path.isfile(resource
        base_img = resource
    ____
        base_img = download_url(resource)

    prompt = 'Text to put on image '
    prompt += '(max {} chars, double enter = end '.format(TEXT_CHAR_LIMIT)
    input_text = get_input(prompt)
    input_text = input_text[:TEXT_CHAR_LIMIT]

    out_file = create_img_with_text(base_img, input_text)

    print('{} created'.format(out_file))
