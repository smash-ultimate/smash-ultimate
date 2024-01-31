import json
from pprint import pprint

chars = "Steve	Pyra/Mythra	Joker	R.O.B.	Sonic	Roy	Kazuya	Wolf	Palutena	Fox	PAC-MAN	Pikachu	Cloud	Peach/Daisy	Mr. Game & Watch	Snake	Shulk	Min Min	Pokemon Trainer	Diddy Kong	Lucina	Wario	Samus/Dark Samus	Mario	Young Link	Zero Suit Samus	Sephiroth	Yoshi	Terry	Olimar	Greninja	Byleth	Mii Brawler	Sora	Ness	Ryu	Sheik	Falco	Mega Man	Ken	Inkling	Bayonetta	Captain Falcon	Luigi	Chrom	Corrin	Rosalina & Luma	Hero	Link	Bowser	Pichu	Wii Fit Trainer	Lucas	Toon Link	Incineroar	Ice Climbers	Marth	Meta Knight	Jigglypuff	Pit	Dark Pit	Robin	Mewtwo	Ridley	Ike	Simon/Richter	Mii Gunner	Duck Hunt	Donkey Kong	Villager	Bowser Jr.	Banjo & Kazooie	Dr. Mario	Lucario	Isabelle	Kirby	King K. Rool	Zelda	Piranha Plant	Mii Swordfighter	King Dedede	Little Mac	Ganondorf".split("\t")

def F(n): return n.strip().replace(" ", "_").replace(".", "").lower().replace("&", "and")

def match_name(name, array, dbg=0):
    names = name.split("/")
    for name in names:
        for item in array:
            for n in item.split("/"):
                if dbg:
                    print(repr(F(n)), "==", repr(F(name)))
                if F(n) == F(name):
                    return item
    return None

with open("data.json") as fp:
    data = json.load(fp)

i = 0
while i < len(chars):
    name = match_name(chars[i], data)
    if F(chars[i]) == "pokemon_trainer":
        name = "Squirtle"
    elif name is None:
        print(name, match_name(chars[i], data, 1))
    
    chars[i] = data[name]["number"]
    i += 1


raw_mu_data = []

with open("data.txt") as fp:
    for line in fp:
        raw_mu_data.append(line.strip().split("\t"))

mu_data = {}

NA = "-"
WINNING = "3"
EASY_WIN = "2"
WIN = "1"
SLIGHT_WIN = "0.5"
EVEN = "0"
LIGHT_LOSS = "-0.5"
LOSE = "-1"
BIG_LOSS = "-2"
NOT_WINNING = "-3"

for i, char in enumerate(chars):
    mu_data[char] = {NA: [], WINNING: [], EASY_WIN: [], WIN: [], SLIGHT_WIN:[], EVEN: [], LIGHT_LOSS: [], LOSE: [], BIG_LOSS: [], NOT_WINNING: []}
    for char_i, placement in enumerate(raw_mu_data[i]):
        mu_data[char][placement].append(chars[char_i])


for char in data:
    num = data[char]["number"]
    if num == "4e": num = "4"
    if num == "13e": num = "13"
    data[char]["matchups"] = mu_data[num]
    





if True:
    char = "GANONDORF"
    def char_icon(c):
        return f"""<img width=40px height=40px src="https://smasharchives.com//assets/stock/{c}.png"></img>"""
    nl = "\n"
    print(f"""
<h1>Matchups {char_icon(data[char]["number"])}</h1>
<div style="margin-left: 50px;">
    {"<h2>Strong win (+3)</h2><div style='margin-left: 50px;'>" if len(data[char]["matchups"]["3"]) else ""}
    {nl.join(char_icon(c) for c in data[char]["matchups"]["3"])}
    {"</div>" if len(data[char]["matchups"]["3"]) else ""}
    
    {"<h2>Easy win (+2)</h2><div style='margin-left: 50px;'>" if len(data[char]["matchups"]["2"]) else ""}
    {nl.join(char_icon(c) for c in data[char]["matchups"]["2"])}
    {"</div>" if len(data[char]["matchups"]["2"]) else ""}
    
    {"<h2>Win (+1)</h2><div style='margin-left: 50px;'>" if len(data[char]["matchups"]["1"]) else ""}
    {nl.join(char_icon(c) for c in data[char]["matchups"]["1"])}
    {"</div>" if len(data[char]["matchups"]["1"]) else ""}
    
    {"<h2>Slight win (+0.5)</h2><div style='margin-left: 50px;'>" if len(data[char]["matchups"]["0.5"]) else ""}
    {nl.join(char_icon(c) for c in data[char]["matchups"]["0.5"])}
    {"</div>" if len(data[char]["matchups"]["0.5"]) else ""}
    
    {"<h2>Even (0)</h2><div style='margin-left: 50px;'>" if len(data[char]["matchups"]["0"]) else ""}
    {nl.join(char_icon(c) for c in data[char]["matchups"]["0"])}
    {"</div>" if len(data[char]["matchups"]["0"]) else ""}
    
    {"<h2>Slight loss (-0.5)</h2><div style='margin-left: 50px;'>" if len(data[char]["matchups"]["-0.5"]) else ""}
    {nl.join(char_icon(c) for c in data[char]["matchups"]["-0.5"])}
    {"</div>" if len(data[char]["matchups"]["-0.5"]) else ""}
    
    {"<h2>Loss (-1)</h2><div style='margin-left: 50px;'>" if len(data[char]["matchups"]["-1"]) else ""}
    {nl.join(char_icon(c) for c in data[char]["matchups"]["-1"])}
    {"</div>" if len(data[char]["matchups"]["-1"]) else ""}
    
    {"<h2>Major Loss (-2)</h2><div style='margin-left: 50px;'>" if len(data[char]["matchups"]["-2"]) else ""}
    {nl.join(char_icon(c) for c in data[char]["matchups"]["-2"])}
    {"</div>" if len(data[char]["matchups"]["-2"]) else ""}

    {"<h2>Not winning (-3)</h2><div style='margin-left: 50px;'>" if len(data[char]["matchups"]["-3"]) else ""}
    {nl.join(char_icon(c) for c in data[char]["matchups"]["-3"])}
    {"</div>" if len(data[char]["matchups"]["-3"]) else ""}
</div>""")

else:    
    with open("data.json", "w") as fp:
        json.dump(data, fp, indent=4)
