class NyvänPage:
    def __init__(self, page):
        self.page = page

        self.namn_edit = page.get_by_role("main").locator("div").filter(has_text="Namn").get_by_role("textbox")



