from Terminal import Pages
from pages import (
    Menu, Settings
)

Pages.PageRegistry.build(Menu, Settings)
game = Pages.Application()
Pages.PageRegistry.load(game)
game.init("menu")
game.start()