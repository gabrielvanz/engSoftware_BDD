from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://www.uol.com.br/esporte/"
xpath_link_noticia = "//*[contains(@class, 'image-right col-md-22')]"
xpath_page_noticia = "//*[contains(@class, 'solar-kicker is-default web regular-text-2')]" 
xpath_txt_noticia = "//*[contains(text(), 'Torcida pede, Luciano entra e dá vitória ao São Paulo contra o Cruzeiro')]"
xpath_assinar_uol = "//*[contains(text(), 'Assine UOL')]"

@given("que esteja na página inicial do UOL Esporte")
def acessar_site(context):
    context.web.get(base_url)

@when('selecionar uma notícia')
def step_impl(context):    
    context.web.find_element(By.XPATH, xpath_link_noticia).click()

@then('deverá ser direcionado para a página da notícia selecionada')
def valida_msg(context):      
    try:
        carregar_page = EC.presence_of_element_located((By.XPATH, xpath_page_noticia))
        WebDriverWait(context.web, 10).until(carregar_page)
        context.web.find_element(By.XPATH, xpath_txt_noticia)
        context.web.find_element(By.XPATH, xpath_assinar_uol)
    except NoSuchElementException:
        raise AssertionError('Elemento não encontrado')