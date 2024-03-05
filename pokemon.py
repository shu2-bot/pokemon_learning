class Pokemon():
    def __init__(self, name:str, baseStats:list, effortValues:list, individualValue:list):
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

        # 実数値
        self.hitpoint:int = self.baseStat_hitPoint * self.effortValue_hitPoint
        self.attack:int = self.baseStat_attack * self.effortValue_attack

    def show_status(self):
        print(self.hitpoint, end=", ", )
        print(self.attack, sep="")

# __name__には, importして用いた時はmodule名, スクリプトとして実行したときは__main__が入力される
# 以下はテストコードとしてよく利用される
if __name__ == '__main__':
    offense_pokemon_1 = Pokemon("pikachu", [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0])

    print(offense_pokemon_1.name)
    print(offense_pokemon_1.baseStat_hitPoint)
    offense_pokemon_1.show_status()