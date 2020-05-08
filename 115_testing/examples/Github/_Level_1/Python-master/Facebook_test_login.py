import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException


class PruebaLoginBusqueda(unittest.TestCase):
#Creamos el driver que manipula la web
#utilizamos el driver para abrir una url
    def setUp(self):
      drive = webdriver.Chrome()
      self.driver = webdriver.Chrome()
      #self.driver.implicitly_wait(30)
      #self.driver.maximize_window()
      self.driver.get("http://www.facebook.com")
      time.sleep(4.0)
    #def testTitle(self):
      self.titulo = self.driver.find_element_by_id("pageTitle") #verificamos si estamos en el sitio correcto atraves de su titulo
      #print(str (self.titulo))
      if self.titulo == 'Facebook - Connexion ou inscription': 
         print("Estamos en facebook!")
         time.sleep(1)
      else:
         print("No estamos en facebook, o el titulo esta mal!")

    def testLogin(self):
        try:
            self.elem = self.driver.find_element_by_id("email") #Buscamos el campo para inserir el usuario
        except NoSuchElementException as exception:
            print("No encontramos el elemento:", exception)
        else:
            time.sleep(2.0)
            print("Elemento email --> OK!")
        self.elem.send_keys("email") #Escrebimos el nombre de usuario
        
        time.sleep(1) #Esperamos un segundo
        self.elem = self.driver.find_element_by_id("pass") #Buscamos el campo para inserir el password
        self.elem.send_keys("pass") #Escrebimos el password
        self.elem.send_keys(Keys.RETURN)
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(2) #Esperamos un segundo
        print("Login 'OK'")
        time.sleep(5.0)
        self.elem = self.driver.find_element_by_name("q")
        self.elem.send_keys("nombre a buscar")
        self.elem.send_keys(Keys.RETURN)
        print("Busqueda 'OK'")
        time.sleep(5.0)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()