import pokemon
import move
import z3

class Calc_z3():
    random_num = [0.85, 1.0]
    damage_ans_list = []

    def __init__(self):
        pass

    def clac_damage(self, offense_pokemon:pokemon.Pokemon, defense_pokemon:pokemon.Pokemon, move:move.Move):
        damage_1 = int(offense_pokemon.level * 2 / 5 + 2)
        if move.classofocation == "physical":
            damage_2 = int(damage_1 * move.power * offense_pokemon.attack / defense_pokemon.defense)
        else:
            damage_2 = int(damage_1 * move.power * offense_pokemon.baseStat_specialAttack / defense_pokemon.baseStat_specialDefense)
        damage_3 = int(damage_2 / 50 + 2)
        damage_ans_list = [damage_3 * self.random_num[0], damage_3 * self.random_num[1]]

        return damage_ans_list
