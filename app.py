from playwright.sync_api import sync_playwright


def scrape_basic_info():
    with sync_playwright() as p:
        # Launch browser (like opening Chrome manually)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to website (like typing URL in address bar)
        page.goto("https://pycoin24.com")

        # Extract information (like reading text on the page)
        title = page.title()
        heading = page.locator("h2").text_content()

        # Take a ScreenShot of the webpage
        page.screenshot(path="pycoin24.png")

        print(f"Page title: {title}")
        print(f"Main heading: {heading}")

        browser.close()


scrape_basic_info()
