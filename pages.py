from console import MenuPage
from game import GameGlobal
from enums import Difficulty
from Terminal import Terminal

class Menu(MenuPage):
    title = "Welcome to the $bluGladiators$res!"
    subtitle = "Options"
    prompt = "Select one destination: "
    options = [
        "$greContinue$res",
        "$greSettings$res",
        "$redExit$res"
    ]
    def render(self) -> None:
        self.build_ui()
        self.builder.print("Once you enter the game, go back to enter the shop.")
        self.builder.render()
        match self.generate_options().strip():
            case "2":
                self.game.init("settings")
            case "3":
                self.game.quit()

class Settings(MenuPage):
    title = "---- {$briSETTINGS$res} ----"
    subtitle = "Options:"
    prompt = "Select one option to chance: "
    options = [
        "$yelName$res",
        "$yelDifficulty$res",
        "$redBack$res"
    ]
    def render(self) -> None:
        self.build_ui()
        match self.generate_options([
            f" [$mag{GameGlobal.Settings.name}$res]",
            f" [$mag{GameGlobal.Settings.difficulty.title()}$res]"
        ]).strip():
            case "1":
                new_name = Terminal.input("Select a name: ", color=True)
                GameGlobal.Settings.name = new_name
            case "2":
                Terminal.space()
                Terminal.print("Difficulties:")
                for difficulty in Difficulty.__members__.values():
                    Terminal.print(f"$mag{difficulty.title()}$res")
                new_difficulty = None
                while not new_difficulty:
                    new_difficulty = Difficulty.get(
                        Terminal.input("Select one of the difficulties above: ")
                    )
                GameGlobal.Settings.difficulty = new_difficulty
            case "3": 
                self.game.init("menu")