import random

perks = {
    'looper': ['Sprint Burst', 'Dead Hard', 'Balanced Landing', 'Lithe', 'Windows of Opportunity', 'Quick & Quiet'],
    'selfcare': ['Self-Care', 'Botany Knowledge', 'Inner Strength', 'Adrenaline', 'Bond', 'Empathy'],
    'gerador': ['Prove Thyself', 'Resilience', 'This Is Not Happening', 'Leader', 'Spine Chill', 'Alert'],
    'helpful': ["We'll Make It", 'Borrowed Time', 'Kindred', 'Open-Handed', 'Iron Will', 'Premonition']
}

descriptions = {
    'Sprint Burst': 'When starting to run, break into a sprint at 150% of your normal running speed for a maximum of 3 seconds.',
    'Dead Hard': 'Activate to dash forward, avoiding damage. You become invulnerable during the dash.',
    'Balanced Landing': 'Stumbling upon obstacles makes you instantly sprint at 150% of your normal running speed for a maximum of 3 seconds.',
    'Lithe': 'Perform a quick vault while sprinting to activate Lithe. Performing a quick vault calls upon the entity to block that vault location for 16 seconds.',
    'Windows of Opportunity': 'Reveals pallets and vaults within a range of 20 meters.',
    'Quick & Quiet': 'You do not make as much noise as others when quickly vaulting over obstacles or hiding in lockers.',
    'Self-Care': 'Unlocks the ability to heal yourself without a med-kit at 50% of the normal healing speed.',
    'Botany Knowledge': 'Healing speed is increased by 33%.',
    'Inner Strength': 'After cleansing a totem, Inner Strength activates. You can then use it to heal yourself.',
    'Adrenaline': 'Once all generators are completed, you receive a sprint burst for 5 seconds and recover from the dying state.',
    'Bond': 'Reveals the auras of other survivors within a range of 36 meters.',
    'Empathy': 'Reveals the auras of injured or dying survivors within a range of 64 meters.',
    'Prove Thyself': 'When working on a generator with others, you get a bonus to repair speed.',
    'Resilience': 'While injured, receive a 9% boost to repair, healing, and sabotage speeds.',
    'This Is Not Happening': 'While injured, great skill check success zones are increased by 50%.',
    'Leader': 'When you are working on a generator with others, you all get a bonus to repair speed.',
    'Spine Chill': 'Get notified when the killer is looking directly in your direction and standing within 36 meters.',
    'Alert': 'See the killer\'s aura for 3 seconds when they break a pallet or generator within 36 meters.',
    "We'll Make It": 'Receive an additional speed bonus when healing survivors and grants them the speed bonus as well.',
    'Borrowed Time': 'Unhooking survivors will trigger the Endurance status effect for 15 seconds.',
    'Kindred': 'See the auras of other survivors and the killer when you are hooked.',
    'Open-Handed': 'Increases aura reading ranges by 4 meters.',
    'Iron Will': 'Grants the ability to reduce grunts from injuries by 50% while staying quiet.',
    'Premonition': 'The killer is alerted when looking in your direction within a range of 36 meters.',
}

def recomendar_build(estilo, num_pearks=4):
    if estilo not in perks:
        return 'Estilo não encontrado'
    
    if num_pearks <= 0 or num_pearks > 4:
        return 'Número de perks inválido. Escolha entre 1 e 4 perks'
    
    build_recomendada = random.sample(perks[estilo], num_pearks)
    print('Build recomendada para o estilo "{}" com {} perks:'.format(estilo, num_pearks))
    
    for perk in build_recomendada:
        print('\n{}: \n{}'.format(perk, descriptions.get(perk, 'Descrição não disponível')))
        
        


print('Bem-vindo ao DBD Build Generator!')
print('Escolha um estilo de jogo: looper, selfcare, gerador ou helpful e a quantidade de pearks 1 a 4')

gameplay = input('Estilo de jogo: ')
num_pearks = int(input('Número de perks: '))

recomendar_build(gameplay, num_pearks)
