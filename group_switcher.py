from playwright.sync_api import Playwright, sync_playwright, expect


class TestData:
    emails = []


def group_switcher(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,
                                         proxy={
                                             'server': '',
                                             'username': '',
                                             'password': '',
                                         })
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://frequency.administrativedistrict.com/login")
    page.get_by_placeholder("Email...").click()
    page.get_by_placeholder("Email...").fill("ross@kingbilly.com")
    page.get_by_placeholder("Пароль").fill("rP5s2$7shg")
    page.get_by_role("button", name="Вход").click()
    page.pause()

    for email in TestData.emails:
        page.get_by_role("textbox", name="Search").click()
        page.get_by_role("textbox", name="Search").fill(email)
        page.get_by_role("button", name="search").click()
        page.locator(
            'xpath=/html/body/div[5]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr/td[3]/a/span').first.click()
        page.get_by_role("button", name="Player").click()
        page.get_by_role("listbox").get_by_role("option", name="Test player").click()
        page.locator("#dataForm").get_by_role("button", name="Save").click()
        page.get_by_role("button", name="OK").click()
        page.get_by_role("link", name=" Players").click()
        print(f'{email} "is marked as test acc"')

    # ---------------------
    context.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        group_switcher(playwright)
