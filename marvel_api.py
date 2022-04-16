from genericpath import exists
import requests
import json

# api call to retrieve cards from marveldb.com, output to file
def api_marvel_cd(url,payload,headers):
    api_url = url
    payload= {}
    headers = {}

    response = requests.get(api_url, headers=headers, data=payload)

    if response.status_code == 200:
        cards = response.json()
        with open('marvel_champions.json', 'w') as json_file:
            json.dump(cards, json_file, indent=2)

    else:
        print(f"There was a problem getting your data.\nError: {response.status_code}")

# open the json file containing marvel cards
def open_marvel_cdb_file():
    with open('marvel_champions.json', 'r') as marvel_cdb:
        cards = json.load(marvel_cdb)
    return cards

# request packs when making api call
def request_packs():
    url = 'https://www.marvelcdb.com/api/public/packs/'
    payload= {}
    headers = {}

    api_marvel_cd(url,payload,headers)

# request cards when making api call
def request_cards():
    url = 'https://www.marvelcdb.com/api/public/cards/'
    payload= {}
    headers = {}

    api_marvel_cd(url,payload,headers)

# list and count all heroes
def count_heroes():
    cards = open_marvel_cdb_file()
    count = 0

    for card in cards:
        try:
            if card["type_code"] == "hero" and card["linked_to_name"]:
                print(card["card_set_name"])
                count += 1
        except:
            continue
    
    print(f'\nHeroes = {count}')

# list and count any type of player card
def count_player_cards(type_entered):
    cards = open_marvel_cdb_file()
    all_unique_count = 0
    all_total_count = 0

    if type_entered == "all":
        type_entered = ["event","resource","support","upgrade"]
    
    else:
        type_entered = [type_entered]
    
    for type in type_entered:
        type_unique_count = 0
        type_total_count = 0

        for card in cards:
            if card["type_code"] == type:
                print(f'{card["name"]} x{card["quantity"]}')
                type_unique_count += 1
                type_total_count += card["quantity"]
        
        print(f'\nUnique {type}s = {type_unique_count}')
        print(f'Total {type}s = {type_total_count}\n')
        all_unique_count += type_unique_count
        all_total_count += type_total_count
 
    if len(type_entered) > 1:
        print(f'Unique cards = {all_unique_count}')
        print(f'Total cards = {all_total_count}\n')    


# list and count all encounter cards
def count_encounter_cards(type_entered):
    cards = open_marvel_cdb_file()
    all_unique_count = 0
    all_total_count = 0

    if type_entered == "all":
        type_entered = ["attachment","minion","side_scheme","treachery","support","upgrade"]
    
    else:
        type_entered = [type_entered]
    
    for type_code in type_entered:
        type_unique_count = 0
        type_total_count = 0

        for card in cards:
            if card["type_code"] == type_code and "boost" in card:
                print(f'{card["name"]} x{card["quantity"]}')
                type_unique_count += 1
                type_total_count += card["quantity"]
        
        print(f'\nUnique {type_code}s = {type_unique_count}')
        print(f'Total {type_code}s = {type_total_count}\n')
        all_unique_count += type_unique_count
        all_total_count += type_total_count
 
    if len(type_entered) > 1:
        print(f'Unique cards = {all_unique_count}')
        print(f'Total cards = {all_total_count}\n')    


# uncomment function you want to run
#count_heroes()
#count_player_cards("all")
count_encounter_cards("all")
#request_packs()
#request_cards()