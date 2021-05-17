from symbol.symbol import Symbol


class Player:
    def __init__(self, name: str):
        self.name = name
        self.symbol = None
        self.turn = None
        self.results = {"wins": 0, "losses": 0, "draws": 0}

    def __repr__(self):
        return f"Player({self.name}"

    def __str__(self):
        results = '\n  - '.join([f"{key}: {val}" for key, val in self.results.items()])
        return f"{self.name}: \n  - {results}"

    def show_name(self):
        return self.name.upper()

    def set_symbol(self, value: Symbol):
        self.symbol = value

    def set_turn(self, value: int):
        self.turn = value

    def wins_a_game(self):
        self.results["wins"] += 1

    def looses_a_game(self):
        self.results["losses"] += 1

    def draws_a_game(self):
        self.results["draws"] += 1
