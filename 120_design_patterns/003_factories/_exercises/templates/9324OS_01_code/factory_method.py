# ______ xml.etree.ElementTree as etree
# ______ j..
#
# c_ JSONConnector
#     ___ - filepath
#         ?data _ di..
#         w___ o.. ? mo.._'r' en.._ utf-8 __ f
#             ?d.. _ j__.l.. ?
#
#     ??
#     ___ parsed_data
#         r_ ?d..
#
# c_ XMLConnector
#     ___ - filepath
#         ?tree = et__.par.. ?
#
#     ??
#     ___ parsed_data
#         r_ ?t..
#
# ___ connection_factory filepath
#     __ ?.e_w_('json
#         connector = JC..
#     ____ ?.e_w_('xml
#         connector = XC..
#     ____
#         r_ V... 'Cannot connect to @'.f.. ?
#     r_ c.. ?
#
# ___ connect_to filepath
#     factory = N..
#     ___
#         factory = c_f.. ?
#     ________ V.. __ ve
#         print ?
#     r_ f..
#
# ___ main
#     sqlite_factory = c_t.. 'data/person.sq3'
#     print()
#
#     xml_factory = c_t.. 'data/person.xml'
#     xml_data = ?.p_d..
#     liars = x_d__.f_a.. ".//person[lastName='@']".f.. 'Liar'
#     print('found @ persons'.f.. le. ?
#     ___ liar __ ?
#         print('first name @'.f.. ?.fi.. 'firstName' .t..
#         print('last name @'.f.. ?.fi.. 'lastName' .t..
#         |print('phone number (@)'.f.. p.attrib | 'type'|| p.text) ___ p __ ?.fi.. 'phoneNumbers'
#     print()
#
#     json_factory = c_t. 'data/donut.json'
#     json_data = ?.p_d..
#     print('found @ donuts'.f.. le. ?
#     ___ donut __ ?
#         print('name @'.f.. ? 'name'
#         print('price $@'.f.. ? 'ppu'
#         |print('topping @ @'.f..(t 'id'| t|'type' ___ t __ ? 'topping'
#
# __ _______ __ _____
#     ?
