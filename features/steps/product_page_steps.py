from selenium.webdriver.common.by import By
from behave import *

INDIVIDUAL_VISUALIZATION_TAB = (By.CSS_SELECTOR, 'div.w-tabs > div > a')

VISUALIZATION_TAB = (By.XPATH, "//div[contains(@class, 'tabs-menu-project w-tab-menu') and contains(@role, 'tablist')] //a")

TAB_LOCATOR = (By.CSS_SELECTOR, '.tabs-menu-project a')


@then('Verify there are {expected_result} options for visualization')
def verify_three_options_in_visualization(context, expected_result):
    expected_result = int(expected_result)
    actual_result = len(context.driver.find_elements(*VISUALIZATION_TAB))
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


@then('Verify the three options of visualization are {visualization_type_1}, {visualization_type_2}, {visualization_type_3}')
def verify_can_click_visualization(context, visualization_type_1, visualization_type_2, visualization_type_3):
    tab_elements = context.driver.find_elements(*TAB_LOCATOR)
    expected_texts = [visualization_type_1, visualization_type_2, visualization_type_3]
    actual_texts = [element.text for element in tab_elements]

    assert actual_texts == expected_texts, f'Expected {expected_texts} did not match actual {actual_texts}'


@then('Verify the options of visualization are clickable')
def verify_clickable_visualizations(context):
    visualization_types = context.driver.find_elements(*INDIVIDUAL_VISUALIZATION_TAB)

    expected_click_count = 3
    actual_click_count = 0

    for visualization_type in visualization_types:
        visualization_type.click()
        actual_click_count += 1

    assert actual_click_count == expected_click_count, f'Expected {expected_click_count} did not match actual {actual_click_count}'