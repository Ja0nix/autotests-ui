from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    # Блок подготовки - сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создание контекста
    page = context.new_page() # Создание страницы

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    # Используем сохраненное состояние в дальнейших тестах
    context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверить наличие и текст заголовка "Courses" 
    course_header = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_header).to_be_visible()
    expect(course_header).to_have_text("Courses")

    # Проверить наличие и текст блока "There is no results"
    no_result_block = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_result_block).to_be_visible()
    expect(no_result_block).to_have_text("There is no results")

    # Проверить наличие и видимость иконки пустого блока
    empty_block_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_block_icon).to_be_visible()

    # Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    block_for_results = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_for_results).to_be_visible()
    expect(block_for_results).to_have_text("Results from the load test pipeline will be displayed here")