from behave import given, when, then
from selenium.webdriver.common.by import By

base_url = "https://www.atitus.com.br/"

@when("eu acesso a página principal")
def acessar_site(context):
    context.web.get(base_url)

@then("deve ser mostrado um banner sobre o vestibular no topo")
def cbanner_vestibular(context):
    vestibular = context.web.find_element(By.LINK_TEXT, "Vestibular de verão 2024/1")

