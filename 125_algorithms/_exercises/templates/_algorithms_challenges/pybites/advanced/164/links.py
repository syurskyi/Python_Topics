_______ sys

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


___ make_html_links():

    ___ line __ sys.stdin:
        
        line = line.s..
        __ line.startswith('http') a.. comma.c.. ',') __ 1:

            href,link_name = line.s..(',')
            href = href.s..
            link_name = link_name.s..


            domain = re.search(r'https?//(.+?)/').group(1)
            __ domain n.. __ INTERNAL_LINKS:
                add_target = True
            ____:
                add_target = False


            
            __ n.. add_target:
                link = f'<a href="{href}">{link_name}</a>'
            ____:
                link = f'<a href="{href}" target="_blank">{link_name}</a>'

            

            print(line)









        



__ __name__ __ '__main__':
    make_html_links()
