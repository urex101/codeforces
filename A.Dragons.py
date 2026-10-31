#230A

strength , number = map(int, input().split())
enemty_strength_Boost = dict()

enemies_beat = 0
for i in range(number):
    enemy_strength1, enemy_boost1 = map(int, input().split())
    if enemy_strength1 in enemty_strength_Boost:
        enemty_strength_Boost[enemy_strength1] += enemy_boost1
    else:
        enemty_strength_Boost[enemy_strength1] = enemy_boost1
enemysortedfromweaktostrong = sorted(enemty_strength_Boost.items(), key=lambda x: x[0])
for enemy_strength, enemy_boost in enemysortedfromweaktostrong:
    if strength > enemy_strength:
        strength += enemy_boost
        enemies_beat += 1
    else:
        break
if len(enemty_strength_Boost) == enemies_beat:
    print("YES")
else:
    print("NO")



