from Terminal import Pages
from pages import (
    Menu, Settings, ShopPage
)

Pages.PageRegistry.build(Menu, Settings, ShopPage)
game = Pages.Application()
Pages.PageRegistry.load(game)
game.init("menu")
game.start()