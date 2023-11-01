from behave import when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ON_OFF_LINK = (By.CSS_SELECTOR, 'address.menu-twobutton > a'[0])
FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, 'div.cards-properties a:nth-child(1)')


@when('Click on off plan at the left side menu')
def click_onoff_plan_link(context):
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.driver.wait.until(EC.element_to_be_clickable(ON_OFF_LINK)).click()


@when('Click on the first product')
def click_on_first_product(context):
    context.driver.wait = WebDriverWait(context.driver, 30)
    context.driver.wait.until(EC.element_to_be_clickable(FIRST_PRODUCT_LINK)).click()


