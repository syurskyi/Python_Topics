_______ ___

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


___ make_html_links

    ___ line __ ___.stdin:
        
        line = line.s..
        __ line.startswith('http') a.. comma.c.. ',') __ 1:

            href,link_name = line.s..(',')
            href = href.s..
            link_name = link_name.s..


            domain = __.s..(r'https?//(.+?)/').group(1)
            __ domain n.. __ INTERNAL_LINKS:
                add_target = T..
            ____
                add_target = F..


            
            __ n.. add_target:
                link = f'<a href="{href}">{link_name}</a>'
            ____
                link = f'<a href="{href}" target="_blank">{link_name}</a>'

            

            print(line)









        



__ _____ __ _____
    make_html_links()
