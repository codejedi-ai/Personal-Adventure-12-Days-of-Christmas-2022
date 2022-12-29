import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.zolo.ca/")
        # await page.get_by_label("Password").fill("secret-password")
        await page.locator("xpath=/html/body/main/section[3]/nav[1]/a[4]").click()
        await browser.close()

asyncio.run(main())
