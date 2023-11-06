from behave import given, when, then
from selenium.webdriver.common.by import By
import pdb

base_url = "https://www.magazineluiza.com.br/"
inpt_busca = '#search-container input'
produto_slc = "//*[contains(@class, 'sc-APcvf eJDyHN')]"

@given(u'que esteja na página inicial da Magazine Luiza')
def acessar_site(context):
    context.web.get(base_url)

@when(u"buscar pelo produto '{produto}'") 
def pesquisar_produto(context, produto):
    context.web.find_element(By.ID, inpt_busca).click()
    context.web.find_element(By.ID, inpt_busca).clear()
    context.web.find_element(By.ID, inpt_busca).send_keys(produto)

@when(u'selecionar o primeiro produto') 
def selecionar_produto(context):
    pdb.set_trace()
   

@then('deverá ser direcionado para a página do produto') 
def validar_produto(context):
    assert "magazineluiza.com.br/produto" in context.driver.current_url
    pdb.set_trace()
