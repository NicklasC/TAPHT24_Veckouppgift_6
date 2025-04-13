class NyvänPage:
    def __init__(self, page):
        self.page = page

        self.namn_edit = page.get_by_role("main").locator("div").filter(has_text="Namn").get_by_role("textbox")
        self.epost_edit = page.get_by_role("main").locator("div").filter(has_text="E-post").get_by_role("textbox")
        self.save_button = page.get_by_role("button", name="Spara")
