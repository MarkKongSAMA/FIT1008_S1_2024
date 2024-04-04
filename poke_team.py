from pokemon import *
import random
from typing import List
from battle_mode import BattleMode
from pokemon_base import *


class PokeTeam:
    random.seed(20)
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()

    def __init__(self):
        self.team = []# change None value if necessary
        self.team_count = 0

    def choose_manually(self):
        print("Choose your team of 6 Pokemon from the following list:")
        print(self.POKE_LIST)
        for i in range(self.TEAM_LIMIT):
            poke = input("Enter the name of the Pokemon you want to add to your team: ")
            while poke not in self.POKE_LIST:
                print("Invalid Pokemon name. Please try again.")
                poke = input("Enter the name of the Pokemon you want to add to your team: ")
            self.team.append(Pokemon(poke))

    def choose_randomly(self) -> None:
        all_pokemon = get_all_pokemon_types()
        self.team_count = 0
        for i in range(self.TEAM_LIMIT):
            rand_int = random.randint(0, len(all_pokemon)-1)
            self.team.append(all_pokemon[rand_int]())
            self.team_count += 1

    def regenerate_team(self, battle_mode: BattleMode, criterion: str = None) -> None:
        for i in self.team:
            Pokemon(i).get_health = Pokemon(i).health

    def assign_team(self, criterion: str = None) -> None:
        raise NotImplementedError

    def assemble_team(self, battle_mode: BattleMode) -> None:
        raise NotImplementedError

    def special(self, battle_mode: BattleMode) -> None:
        raise NotImplementedError

    def __getitem__(self, index: int):
        return self.team[index]

    def __len__(self):
        return len(self.team)

    def __str__(self):
        team_members = "\n".join(str(pokemon) for pokemon in self.team)
        return team_members

class Trainer:

    def __init__(self, name) -> None:
        self.name = name
        self.team = PokeTeam()
        self.pokedex = []

    def pick_team(self, method: str) -> None:
        if method == "Random":
            self.team.choose_randomly()
        elif method == "Manual":
            self.team.choose_manually()
        else:
            raise ValueError("Invalid team selection method. Please choose either 'Random' or 'Manual'.")

    def get_team(self) -> PokeTeam:
        return self.team

    def get_name(self) -> str:
        return self.name

    def register_pokemon(self, pokemon: Pokemon) -> None:
        self.pokedex.append(pokemon.get_type())

    def get_pokedex_completion(self) -> float:
        unique_types = set(self.pokedex)
        total_types = len(PokeTeam.POKE_LIST)
        completion_ratio = len(unique_types) / total_types
        return round(completion_ratio, 2)

    def __str__(self) -> str:
        return f"Trainer {self.name} Pokedex Completion: {self.get_pokedex_completion() * 100}%"

if __name__ == '__main__':
    
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())
    