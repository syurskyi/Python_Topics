import sys

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():

    for line in sys.stdin:
        
        line = line.strip()
        if line.startswith('http') and comma.count(',') == 1:

            href,link_name = line.split(',')
            href = href.strip()
            link_name = link_name.strip()


            domain = re.search(r'https?//(.+?)/').group(1)
            if domain not in INTERNAL_LINKS:
                add_target = True
            else:
                add_target = False


            
            if not add_target:
                link = f'<a href="{href}">{link_name}</a>'
            else:
                link = f'<a href="{href}" target="_blank">{link_name}</a>'

            

            print(line)









        



if __name__ == '__main__':
    make_html_links()
