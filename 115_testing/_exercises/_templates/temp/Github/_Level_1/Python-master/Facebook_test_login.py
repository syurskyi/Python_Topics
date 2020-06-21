# ______ sys
# ____ selenium ______ webdriver
# ____ selenium.webdriver.common.keys ______ Keys
# ______ u__
# ______ time
# ____ selenium.webdriver.chrome.options ______ Options
# ____ selenium.common.exceptions ______ StaleElementReferenceException
# ____ selenium.common.exceptions ______ NoSuchElementException
#
#
# c_ PruebaLoginBusqueda?.?
# #Creamos el driver que manipula la web
# #utilizamos el driver para abrir una url
#     ___ setUp
#       drive _ webdriver.Chrome()
#       driver _ webdriver.Chrome()
#       #self.driver.implicitly_wait(30)
#       #self.driver.maximize_window()
#       driver.get("http://www.facebook.com")
#       time.sleep(4.0)
#     #def testTitle(self):
#       titulo _ driver.find_element_by_id("pageTitle") #verificamos si estamos en el sitio correcto atraves de su titulo
#       #print(str (self.titulo))
#       __ titulo __ 'Facebook - Connexion ou inscription':
#          print("Estamos en facebook!")
#          time.sleep(1)
#       ____:
#          print("No estamos en facebook, o el titulo esta mal!")
#
#     ___ testLogin
#         ___
#             elem _ driver.find_element_by_id("email") #Buscamos el campo para inserir el usuario
#         _____ NoSuchElementException __ exception:
#             print("No encontramos el elemento:", exception)
#         ____:
#             time.sleep(2.0)
#             print("Elemento email --> OK!")
#         elem.send_keys("email") #Escrebimos el nombre de usuario
#
#         time.sleep(1) #Esperamos un segundo
#         elem _ driver.find_element_by_id("pass") #Buscamos el campo para inserir el password
#         elem.send_keys("pass") #Escrebimos el password
#         elem.send_keys(Keys.RETURN)
#         webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#         time.sleep(2) #Esperamos un segundo
#         print("Login 'OK'")
#         time.sleep(5.0)
#         elem _ driver.find_element_by_name("q")
#         elem.send_keys("nombre a buscar")
#         elem.send_keys(Keys.RETURN)
#         print("Busqueda 'OK'")
#         time.sleep(5.0)
#         driver.close()
#
# __ _____ __ _____
#     ?.?