import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверить наличие и текст заголовка "Courses" 
    course_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_header).to_be_visible()
    expect(course_header).to_have_text("Courses")
    
    # Проверить наличие и текст блока "There is no results"
    no_result_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_result_block).to_be_visible()
    expect(no_result_block).to_have_text("There is no results")
    
    # Проверить наличие и видимость иконки пустого блока
    empty_block_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_block_icon).to_be_visible()
    
    # Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    block_for_results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_for_results).to_be_visible()
    expect(block_for_results).to_have_text("Results from the load test pipeline will be displayed here")
