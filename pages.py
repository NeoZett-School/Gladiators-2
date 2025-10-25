from game import GameGlobal
from enums import Difficulty
from Terminal import Terminal, Pages

class Menu(Pages.MenuPage):
    title = "Welcome to the $bluGladiators$res!"
    subtitle = "Options"
    prompt = "Select one destination: "
    options = [
        "$greContinue$res",
        "$greSettings$res",
        "$redExit$res"
    ]
    tag = "menu"
    def render(self) -> None:
        self.build_ui()
        self.builder.print("Once you enter the game, go back to enter the shop.")
        self.builder.render()
        match self.generate_options().strip():
            case "2":
                self.app.init("settings")
            case "3":
                self.app.quit()

class Settings(Pages.MenuPage):
    title = "---- {$briSETTINGS$res} ----"
    subtitle = "Options:"
    prompt = "Select one option to chance: "
    options = [
        "$yelName$res",
        "$yelDifficulty$res",
        "$redBack$res"
    ]
    tag = "settings"
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
                    Terminal.print(f"$mag{difficulty.title()}$res", color=True)
                new_difficulty = None
                while not new_difficulty:
                    user_input = Terminal.input("Select one of the difficulties above: ", color=True)
                    new_difficulty = Difficulty.get(user_input)
                    if not new_difficulty:
                        Terminal.print(f"$redInvalid$res. Please select a valid option, not \"{user_input}\".", color=True)
                GameGlobal.Settings.difficulty = new_difficulty
            case "3": 
                self.app.init("menu")

class ShopPage(Pages.MenuPage):
    title = "---- {$bri$greSHOP$res} ----"
    subtitle = "Options:"
    prompt = "Select one option: "
    options = [
        "$greBuy$res",
        "$redBack$res"
    ]
    tag = "shop"
    def render(self) -> None:
        self.build_ui()
        match self.generate_options().strip():
            case "1":
                Terminal.print("Buying is not implemented yet!", color=True)
            case "2":
                self.app.init("menu")