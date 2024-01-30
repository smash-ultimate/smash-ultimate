import urllib.request
from urllib.parse import unquote
import json
from html.parser import HTMLParser


input("OVERWRITE!!!")
url_data = {'banjo_and_kazooie': '/Banjo%20&%20Kazooie/', 'bayonetta': '/Bayonetta/', 'bowser': '/Bowser/', 'bowser_jr': '/Bowser%20Jr./', 'byleth': '/Byleth/', 'captain_falcon': '/Captain%20Falcon/', 'charizard': '/Charizard/', 'chrom': '/Chrom/', 'cloud': '/Cloud/', 'corrin': '/Corrin/', 'dark_pit': '/Dark%20Pit/', 'diddy_kong': '/Diddy%20Kong/', 'donkey_kong': '/Donkey%20Kong/', 'dr_mario': '/Dr.%20Mario/', 'duck_hunt': '/Duck%20Hunt/', 'falco': '/Falco/', 'fox': '/Fox/', 'ganondorf': '/Ganondorf/', 'greninja': '/Greninja/', 'hero': '/Hero/', 'ice_climbers': '/Ice%20Climbers/', 'ike': '/Ike/', 'incineroar': '/Incineroar/', 'inkling': '/Inkling/', 'isabelle': '/Isabelle/', 'ivysaur': '/Ivysaur/', 'jigglypuff': '/Jigglypuff/', 'joker': '/Joker/', 'kazuya': '/Kazuya/', 'ken': '/Ken/', 'king_dedede': '/King%20Dedede/', 'king_k_rool': '/King%20K.%20Rool/', 'kirby': '/Kirby/', 'link': '/Link/', 'little_mac': '/Little%20Mac/', 'lucario': '/Lucario/', 'lucas': '/Lucas/', 'luigi': '/Luigi/', 'mario': '/Mario/', 'marth_(lucina)': '/Marth%20(Lucina)/', 'mega_man': '/Mega%20Man/', 'meta_knight': '/Meta%20Knight/', 'mewtwo': '/Mewtwo/', 'mii_brawler': '/Mii%20Brawler/', 'mii_gunner': '/Mii%20Gunner/', 'mii_swordfighter': '/Mii%20Swordfighter/', 'min_min': '/Min%20Min/', 'mr_game_and_watch': '/Mr.%20Game%20&%20Watch/', 'ness': '/Ness/', 'olimar': '/Olimar/', 'pac-man': '/Pac-Man/', 'palutena': '/Palutena/', 'peach_(daisy)': '/Peach%20(Daisy)/', 'pichu': '/Pichu/', 'pikachu': '/Pikachu/', 'piranha_plant': '/Piranha%20Plant/', 'pit': '/Pit/', 'pokémon_trainer': '/Pok%C3%A9mon%20Trainer/', 'pyra_and_mythra': '/Pyra%20&%20Mythra/', 'ridley': '/Ridley/', 'rob': '/R.O.B./', 'robin': '/Robin/', 'rosalina_and_luma': '/Rosalina%20&%20Luma/', 'roy': '/Roy/', 'ryu': '/Ryu/', 'samus_(dark_samus)': '/Samus%20(Dark%20Samus)/', 'sephiroth': '/Sephiroth/', 'sheik': '/Sheik/', 'shulk': '/Shulk/', 'simon_(richter)': '/Simon%20(Richter)/', 'snake': '/Snake/', 'sonic': '/Sonic/', 'sora': '/Sora/', 'squirtle': '/Squirtle/', 'steve': '/Steve/', 'terry': '/Terry/', 'toon_link': '/Toon%20Link/', 'villager': '/Villager/', 'wario': '/Wario/', 'wii_fit_trainer': '/Wii%20Fit%20Trainer/', 'wolf': '/Wolf/', 'yoshi': '/Yoshi/', 'young_link': '/Young%20Link/', 'zelda': '/Zelda/', 'zero_suit_samus': '/Zero%20Suit%20Samus/'}

class CharactersHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a" and len(attrs) == 2 and attrs[1][1] == "stretched-link":
            url = attrs[0][1]
            name = unquote(attrs[0][1])[1:-1].replace(".", "").lower().replace(" ", "_").lower().replace("-", "_").replace("&", "and")
            url_data[name] = url

class CharacterHTMLParser(HTMLParser):
    stages = []

    def handle_data(self, data):
        if data[0] == "#":
            self.stages.append(data.split(": ", 1)[1].strip())

    def clear_stages(self):
        self.stages.clear()
            
            

page = "https://www.ssbu-stage-guides.com"

parser = CharacterHTMLParser()
char_parser = CharactersHTMLParser()
# char_parser.feed(urllib.request.urlopen(page).read().decode("utf8"))

with open("data.json") as fp:
    data = json.load(fp)

for id_ in data:
    name = data[id_]["thumb_name"].replace(" ", "_")
    try:
        url = url_data[name]
    except:
        url = None
        for n in url_data:
            if name in n:
                url = url_data[n]
                break
        if url is None:
            name = data[id_]["name"].replace(" ", "_")
            for n in url_data:
                if name in n:
                    url = url_data[n]
                    break
        
        if url is None:
            print("Can't find:", name)
            print(list(url_data))
            print(id_)
            url = url_data[input("URL NAME:")]
        
    parser.clear_stages()
    parser.feed(urllib.request.urlopen(page+url).read().decode("utf8"))

    data[id_]["stages_url"] = url
    data[id_]["stages"] = parser.stages.copy()


with open("data.json", "w") as fp:
    json.dump(data, fp, indent=4)

## Prefered stages link (on chars)
## add yoshi island stage
## ref website "https://www.ssbu-stage-guides.com"
## Stage Counter Pick (stages.html)
"""
function Go(c){
    char = (new URLSearchParams(location.search)).get("char")
    if (char){
        window.location = "https://www.ssbu-stage-guides.com/"+char+"/"+c2
    } else {
        window.location += "&char="+c
    }
}
"""
## Add "Stage Counter Pick Against This Character" button -> /chars?option=stages&char=%CHAR%
## del base.html, character.html
# add discalmer
