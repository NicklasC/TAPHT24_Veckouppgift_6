class HeaderPage:
    def __init__(self, page):
        self.page = page

        self.start_link = page.locator("text=Start")
        self.vänlista_link = page.locator("text=Vänlista")
        self.ny_vän_link = page.locator("text=Ny vän")
