import nature
import move

class Pokemon():
    def __init__(self, name:str, baseStats:list, effortValues:list, individualValue:list, nature:nature, level:int):
        # ポケモンの名前
        self.name:str = name

        # ポケモンの種族値
        self.baseStat_hitPoint:int = baseStats[0]
        self.baseStat_attack:int = baseStats[1]
        self.baseStat_defense:int = baseStats[2]
        self.baseStat_specialAttack:int = baseStats[3]
        self.baseStat_specialDefense:int = baseStats[4]
        self.baseStat_speed:int = baseStats[5]

        # ポケモンの努力値
        self.effortValue_hitPoint:int = effortValues[0]
        self.effortValue_attack:int = effortValues[1]
        self.effortValue_defense:int = effortValues[2]
        self.effortValue_specialAttack:int = effortValues[3]
        self.effortValue_specialDefense:int = effortValues[4]
        self.effortValue_speed:int = effortValues[5]

        # ポケモンの個体値
        self.individualValue_hitPoint:int = individualValue[0]
        self.individualValue_attack:int = individualValue[1]
        self.individualValue_defense:int = individualValue[2]
        self.individualValue_specialAttack:int = individualValue[3]
        self.individualValue_specialDefense:int = individualValue[4]
        self.individualValue_speed:int = individualValue[5]

        # 性格
        self.nature:nature = nature

        # レベル
        self.level = level

        # 実数値
        self.hitpoint:int = int(self.baseStat_hitPoint + self.individualValue_hitPoint/2 + self.effortValue_hitPoint/8) + 60
        self.attack:int = int(((self.baseStat_attack + self.individualValue_attack/2 + self.effortValue_attack/8) + 5) * self.nature.correctionFactor[0])
        self.defense:int = int(((self.baseStat_defense + self.individualValue_defense/2 + self.effortValue_defense/8) + 5) * self.nature.correctionFactor[1])
        self.defense:int = int(((self.baseStat_specialAttack + self.individualValue_specialAttack/2 + self.effortValue_specialAttack/8) + 5) * self.nature.correctionFactor[2])
        self.defense:int = int(((self.baseStat_specialDefense + self.individualValue_specialDefense/2 + self.effortValue_specialDefense/8) + 5) * self.nature.correctionFactor[3])
        self.defense:int = int(((self.baseStat_speed + self.individualValue_speed/2 + self.effortValue_speed/8) + 5) * self.nature.correctionFactor[4])

    def show_status(self):
        print(f"Name: {self.name} | Level: {self.level} | Nature: {self.nature.name}")
        print(f"HP: {self.hitpoint} | Attack: {self.attack} | Defense: {self.defense}")

# __name__には, importして用いた時はmodule名, スクリプトとして実行したときは__main__が入力される
# 以下はテストコードとしてよく利用される
if __name__ == '__main__':
    offense_pokemon_1 = Pokemon("ラムパルド", [97, 165, 60, 65, 50, 58], [0,0,0,0,0,0], [0,0,0,0,0,0], nature.Nature("いじっぱり", [1.1, 1.0, 1.0, 1.0, 0.9]), level=50)

    # print(offense_pokemon_1.name)
    offense_pokemon_1.show_status()