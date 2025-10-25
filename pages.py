from Terminal.pages import Page, SubPage, MenuPage, Application
from Terminal import Terminal
from game import GameGlobal
from enums import Difficulty

class Menu(MenuPage):
    title = "Welcome to the $bluGladiators$res!"
    subtitle = "Options:"
    prompt = "Select one destination: "
    options = [
        "$greContinue$res",
        "$greSettings$res",
        "$redExit$res"
    ]
    tag = "menu"
    def render(self) -> None:
        self.build_ui()
        self.builder.render()
        match self.generate_options().strip():
            case "1":
                self.app.init("shop")
            case "2":
                self.app.init("settings")
            case "3":
                self.app.quit()

class Settings(MenuPage):
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
        self.builder.render()
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

class ShopPage(MenuPage):
    class Popup(SubPage, MenuPage):
        title = "---- {$briSHOP DIRECTORY$res} ----"
        subtitle = "Options:"
        prompt = "Select one option: "
        options = [
            "$greWeapons$res",
            "$greArmor$res",
            "$redBack$res"
        ]
        tag = "shop_directory"
        def render(self) -> None:
            self.build_ui()
            self.builder.render()
            match self.generate_options().strip():
                case "1":
                    Terminal.print("Buying is not implemented yet!", color=True)
                case "2":
                    Terminal.print("Buying is not implemented yet!", color=True)
                case "3":
                    self.app.init("shop")

    title = "---- {$bri$greSHOP$res} ----"
    subtitle = "Options:"
    prompt = "Select one option: "
    options = [
        "$greWeapons$res",
        "$greArmor$res",
        "$redBack$res"
    ]
    tag = "shop"
    def init(self, app: Application) -> None:
        super().init(app)
    def render(self) -> None:
        self.build_ui()
        self.builder.render()
        match self.generate_options().strip():
            case "1":
                Terminal.print("Buying is not implemented yet!", color=True)
            case "2":
                Terminal.print("Buying is not implemented yet!", color=True)
            case "3":
                self.app.init("menu")