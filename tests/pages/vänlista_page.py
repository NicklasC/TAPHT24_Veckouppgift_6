class VänlistaPage:
    def __init__(self, page):
        self.page = page
        self.sök_namn = page.get_by_role("textbox",name="Sök namn")


