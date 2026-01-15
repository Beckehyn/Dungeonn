import random

hp1 = 100
hp2 = 100
runde = 1

def get_action(player):
    action = input(f"Spieler {player} (A=Angriff, B=Block, H=Heilen): ").lower()
    if action not in ["a", "b", "h"]:
        print("Ungültige Aktion! -> Angriff")
        return "a"
    return action

print("🥊 MINI FIGHTING GAME 🥊")
print("Aktionen: A = Angriff | B = Block | H = Heilen\n")

while hp1 > 0 and hp2 > 0:
    print(f"--- Runde {runde} ---")

    a1 = get_action(1)
    a2 = get_action(2)

    dmg1 = random.randint(10, 20)
    dmg2 = random.randint(10, 20)
    heal = random.randint(8, 15)

    # Spieler 1 Aktion
    if a1 == "a":
        if a2 == "b":
            hp2 -= dmg1 // 2
            print("Spieler 2 blockt den Angriff!")
        else:
            hp2 -= dmg1
            print(f"Spieler 1 trifft! Schaden: {dmg1}")

    elif a1 == "h":
        hp1 += heal
        print(f"Spieler 1 heilt sich um {heal}")

    # Spieler 2 Aktion
    if a2 == "a":
        if a1 == "b":
            hp1 -= dmg2 // 2
            print("Spieler 1 blockt den Angriff!")
        else:
            hp1 -= dmg2
            print(f"Spieler 2 trifft! Schaden: {dmg2}")

    elif a2 == "h":
        hp2 += heal
        print(f"Spieler 2 heilt sich um {heal}")

    hp1 = min(hp1, 100)
    hp2 = min(hp2, 100)

    print(f"❤️ Spieler 1 HP: {max(hp1,0)}")
    print(f"❤️ Spieler 2 HP: {max(hp2,0)}\n")

    runde += 1

if hp1 <= 0 and hp2 <= 0:
    print("🤝 Double KO! Unentschieden!")
elif hp1 <= 0:
    print("🏆 Spieler 2 gewinnt!")
else:
    print("🏆 Spieler 1 gewinnt!")
