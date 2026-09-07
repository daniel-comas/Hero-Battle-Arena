# Hero Battle Arena

A turn-based, text-based RPG battle game written in Python. Pick a hero class, then fight a randomly generated enemy or a second player at the same keyboard.


## Game Modes

1. **Fight an Enemy (solo)** — You pick a hero and battle a randomly chosen enemy controlled by simple AI.
2. **Two-Player Battle** — Two players each pick a hero and trade turns on the same machine.

## Hero Classes

| Class | HP | ATK | SPATK | Mana | SP Cost | DEF | ATK Luck | SPATK Luck |
|---|---|---|---|---|---|---|---|---|
| Wizard | 100–110 | 11–13 | 25–28 | 90 | 20 | 6–8 | 90% | 75% |
| Avatar | 85–95 | 11–13 | 30–34 | 160 | 35 | 3–5 | 85% | 80% |
| Warrior | 120–130 | 14–16 | 18–20 | 70 | 25 | 10–12 | 92% | 65% |
| Rogue | 75–85 | 13–15 | 22–25 | 100 | 25 | 2–4 | 95% | 85% |

Stats are rolled randomly within the listed ranges at the start of each game, so no two runs are identical.

- **Wizard** — accurate but works with a thin mana pool. Cheapest special attack.
- **Avatar** — glass cannon. Fireballs hit hardest, but low defense and HP.
- **Warrior** — tank. Highest HP and defense; Power Strike is strong but unreliable.
- **Rogue** — fastest and luckiest. Shadowstrike rarely misses, but the Rogue can't take a hit.

## Enemies

| Enemy | HP | ATK | SPATK | Mana | DEF |
|---|---|---|---|---|---|
| Goblin | 60–70 | 9–11 | 12–15 | 50 | 2–4 |
| Troll | 115–130 | 13–16 | 10–13 | 40 | 8–10 |
| Dark Sorcerer | 80–90 | 9–11 | 28–32 | 120 | 4–6 |

The enemy is picked at random each solo run. On its turn it uses its special attack roughly 50% of the time when it has the mana, otherwise it attacks normally.

## Turn Options

On your turn you can:

1. **Attack** — basic hit, gated by your ATK Luck roll.
2. **Special Attack** — costs mana, deals more damage, gated by SPATK Luck.
3. **Use Potion** — restores 30 HP or 50 mana. You start with 3 of each.
4. **Display Stats** — free action; shows your current stats and returns you to the menu.

Entering anything else forfeits your turn.

## Combat Rules

- Damage taken is `incoming damage - defender's DEF`, with a floor of 0. A defender can never be healed by an attack.
- Missed attacks deal 0 damage, but a special attack still spends mana on a miss.
- Potions never overheal past your maximum HP or mana.
- The battle ends the moment one fighter's HP reaches 0.
