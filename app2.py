async def handle_complex_interactions(page):
    # Fill out search forms
    await page.fill('input[name="q"]', "data scientist")
    await page.select_option('select[name="location"]', "Athens")

    # Click search button and wait for results
    await page.click('button[type="submit"]')
    await page.wait_for_load_state("networkidle")

    # Handle pagination
    page_number = 1
    while page_number <= 3:  # Scrape first 3 pages
        print(f"Scraping page {page_number}")

        # Extract data from current page
        # await 'extract_current_page_data(page)'

        # Try to go to next page
        next_button = page.locator('a[aria-label="Next"]')
        if await next_button.count() > 0:
            await next_button.click()
            await page.wait_for_load_state("networkidle")
            page_number += 1
        else:
            break
