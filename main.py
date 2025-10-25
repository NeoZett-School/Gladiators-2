from console import PageRegistry, Game
from pages import (
    Menu, Settings
)

PageRegistry.build(Menu, Settings)
game = Game()
PageRegistry.load(game)
game.init("menu")
game.start()