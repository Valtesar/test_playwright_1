from playwright.async_api import Page


class WebPage(object):
    def __init__(self, page: Page):
        self.page = page

    async def reload(self):
        await self.page.reload(wait_until='load')

    async def close_page(self):
        await self.page.close()

    async def go_to_page(self, url):
        await self.page.goto(url, wait_until='load')

    async def change_tab(self, function):
        with self.page.context.expect_page(function) as new_page:
            await function()
        new_page = new_page.value
        return new_page
