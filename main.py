from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)
    page = browser.new_page()
    page.goto("https://books.toscrape.com")
    page.wait_for_selector("article")
    tweets = page.query_selector_all("article a")
    for t in tweets:
        print(t.inner_text().strip())
    browser.close()
