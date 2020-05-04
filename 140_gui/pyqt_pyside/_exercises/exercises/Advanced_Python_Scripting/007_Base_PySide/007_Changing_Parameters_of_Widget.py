# ____ ?.? ______ _
# ____ ? ? ______ _
#
# c_ simpleWindowClass QW..
#     ___ - ____
#         s.. ? ____ . -
#         layout = QVL.. ?   # zdes' sozdan LAyout no on ni kak neoboznachen kak layout nashego widgeta. Na samom
#         # self.setLayout(layout)     # dele zdes' ykazan v kachestve argymenta self. To est' parenta. I dlja layout eto
#                                      # avtomaticheski oboznachaet vstroitsja k nemy kak osnovnoj layout, esli tam yze
#                                      #  ne sychestvyet kakogoto layouta. To est' ne prishlos' dal'she pisat'
#                                      # Layout i Button mu ne kladjom v atribyt klassa, potomy shto nam ne prijdjotsja v
#                                      # v dal'nejshem k nemy obrachatsja i s nim rabotat'. Eti peremenue javljajytsja
#                                      # lokalnumi dlja konstryktora i v dal'nejshem bydyt ne dostypnu.
#                                      # S imenem layout nyzno but' ostoroznum. Delo v tom shto y klassa widgeta yze est'
#                                      # metod s takim ze imenem layout, kotoruj vozvrachaet ego central'nuj layout.
#                                      # I esli v dannom primere mu napishem self.layout mu perezapishem etot metod.
#                                      # Lychshe kak to ego pereimenovat'  esli mu hotim pomestit' ego v atribyt klassa.
#
#         label _ QL.. *Text  # nadpis label = QLabel objavljaetsja kak lokalnyjy peremenyjy. I mu ne polychaem
#                                      # prjmogo dostypa k etomy vidzety. Shto bu imet'  vozmoznost'  obratitsja k nemy
#                                      # s lybogo metoda, ego nado pomechat' v atribyt klassa - self.label
#         l__.aW.. ?
#         bu.. _ QPB.. *Press
#         l__.aW.. ?
#         bu__.c__.c.. a..    # Posle pervogo nazatija knopki, connect izmenitsja na zakrutie okna.
#                                                     # To est' mozno menjat' ne tol'ko tekst no i connectu i signalu,
#                                                     # to est' lybue svojstva
#
#     ___ action
#         l__.sT.. *New Text
#         b__.sT.. *Presseed
#         b__.c__.c.. ____.c..
#
# __ ______ __ _____
#     app = QA..
#     w = ?
#     ?.s..
#     ?.e..
