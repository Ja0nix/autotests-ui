import pytest  
from playwright.sync_api import sync_playwright, expect, Page

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage): # Теперь используем фикстуру
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form('user@gmail.com', 'username', 'password')
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title_visability()
