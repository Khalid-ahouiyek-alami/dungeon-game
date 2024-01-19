import time, math, random
playeratack = 1
player_defense = 0
player_health = 3

# === [kamer 1] === #✔
print('ben je er klaar voor')
time.sleep(1)
print('Door de twee grote deuren loop je een gang binnen.')
time.sleep(1)
print('Het ruikt hier muf en vochtig.')
time.sleep(1)
print('Je ziet een deur voor je.')
time.sleep(1)
print('veel succes')
time.sleep(3)


# === [kamer 2] === # ✔
num1=random.randint(10, 25)
num2=random.randint(-5, 75)
juisteantwoord = num1 + num2

print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
print(f'Daarboven zie je een som staan {num1}+{num2}=?')
antwoord = int(input('Wat toest je in?'))

if antwoord == num1 + num2:
    print('Het stadbeeld laat de sleutel vallen en je pakt het op')
    sleutel = True
else:
    print('Er gebeurt niets....')
    sleutel= False

print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(1)

# === [kamer 4.1] === #
randomitem= random.randint(1,2)
if randomitem == 1:
    print('je hebt een schild gekregen je hebt nu een extra punt op je defence')
    randomitem = 'schild'
    player_defense += 1
else:
    print('je hebt een swaard gekregen je hebt nu een extra punt op je attack')
    randomitem = 'swaard'
    playeratack =+ 2

zombie_attack = 2
zombie_defense = 0
zombie_health = 3
print(f'Dapper met je nieuwe {randomitem} loop je de kamer binnen.')
print('Je loopt tegen een sterke mummy aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (playeratack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)    
# === [kamer 3] === #✔



randomitem= random.randint(1,2)
if randomitem == 1:
    print('je hebt een schild gekregen je hebt nu een extra punt op je defence')
    randomitem = 'schild'
    player_defense += 1
else:
    print('je hebt een swaard gekregen je hebt nu een extra punt op je attack')
    randomitem = 'swaard'
    playeratack =+ 2
    


print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {randomitem}.')
print(f'Je pakt het {randomitem} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #✔
zombie_attack = 1
zombie_defense = 0  
zombie_health = 2
print(f'Dapper met je nieuwe {randomitem} loop je de kamer binnen.')
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (playeratack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)                     

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if sleutel == True:
    print("Laatste kamer: Je hebt de sleutel en opent de schatkist. Je wint het spel!")
else:
    print("Laatste kamer: Helaas, je hebt geen sleutel. Je verliest het spel.")