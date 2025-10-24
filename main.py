from console import PageRegistry, Game
from pages import (
    Menu, Settings
)

PageRegistry.build({
    # Correlate string identification with the correct page
    "menu": Menu,
    "settings": Settings
})
game = Game()
PageRegistry.load(game)
game.init("menu")
game.start()