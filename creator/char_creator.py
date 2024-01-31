info_base = """<html>
	<head>
		<title>Smash-Ultimate - Info - %NAME%</title>
		<link rel="stylesheet" href="./../css/dark-colors.css">
		<link rel="stylesheet" href="./../css/dark-mode.css">
		<link rel="stylesheet" href="./../css/main.css">
		<link rel="shortcut icon" href="https://www.smashbros.com/ja_JP/assets_v2/img/howtoplay/mode_label_ico01.svg">
	</head>

	<body>
		<center style="background-color:black;">
			<a href="./../index.html"><img src="./../res/lineup.png" alt="Smash Line Up" style="width:100%;max-width: 1000px;"></a>
			<br>

			<center class="bar">
				<a href="./../info.html" style="background-color:black;"> <button class="bar-button">Character Info</button></a>
				<a href="./../play.html" style="background-color:black;"> <button class="bar-button">How To Play A Character</button></a>
				<a href="./../main.html" style="background-color:black;"> <button class="bar-button">Find A Main</button></a>
				<a href="./../basics.html" style="background-color:black;"> <button class="bar-button">How TO Smash</button></a>
				<a href="./../stages.html" style="background-color:black;"> <button class="bar-button">Legal Stages</button></a>
				<a href="./../stagepick.html" style="background-color:black;"> <button class="bar-button">Stage Counter Picks</button></a>
				<a href="https://ultimateframedata.com/smash" style="background-color:black;"> <button class="bar-button">Frame Data</button></a>
				<a href="https://smasharchives.com/character" style="background-color:black;"> <button class="bar-button">MatchUp Vods</button></a>
			</center>

			<center>
				<h1 class="title" style="background-image:url(https://www.smashbros.com//assets_v2/img/fighter/thumb_h/%THUMB_NAME%.png);">%NAME%</h1>
			</center>
		</center>
		<div class="main-content">
		    <center>
                <a style="text-decoration: none;" href="https://ultimateframedata.com/%FRAMEDATA%"><button class="button">Ultimate Frame-Data</button></a>
                <br>
                <a style="text-decoration: none;" href="%MU%"><button class="button">Match Up Vods</button></a>
                <br>
                <a style="text-decoration: none;" href="https://www.ssbu-stage-guides.com/%STAGE_URL%"><button class="button">Stage Rankings</button></a>
                <br>
                <a style="text-decoration: none;" href="./../stagepick.html?opchar=%STAGE_URL%"><button class="button">Counter pick stage for this character</button></a>
		    </center>
		    
			<h1>Prefered Stages</h1>
			<div>
%GOOD_STAGES%
			</div>
			<h1>Unfavored Stages</h1>
			<div>
%BAD_STAGES%
			</div>

			<h1>Tips</h1>
			<ul>
%TIPS%
			</ul>
			
			<h1>Matchups</h1>
            <div style="margin-left: 50px;">
                %MUS%
            </div>

			<h1>Videos on How To Beat Them</h1>
			%VIDEO%
		</div>
	</body>
</html>
"""

play_base = """<html>
	<head>
		<title>Smash-Ultimate - Play - %NAME%</title>
		<link rel="stylesheet" href="./../css/dark-colors.css">
		<link rel="stylesheet" href="./../css/dark-mode.css">
		<link rel="stylesheet" href="./../css/main.css">
		<link rel="shortcut icon" href="https://www.smashbros.com/ja_JP/assets_v2/img/howtoplay/mode_label_ico01.svg">
	</head>

	<body>
		<center style="background-color:black;">
			<a href="./../index.html"><img src="./../res/lineup.png" alt="Smash Line Up" style="width:100%;max-width: 1000px;"></a>
			<br>

			<center class="bar">
				<a href="./../info.html" style="background-color:black;"> <button class="bar-button">Character Info</button></a>
				<a href="./../play.html" style="background-color:black;"> <button class="bar-button">How To Play A Character</button></a>
				<a href="./../main.html" style="background-color:black;"> <button class="bar-button">Find A Main</button></a>
				<a href="./../basics.html" style="background-color:black;"> <button class="bar-button">How TO Smash</button></a>
				<a href="./../stages.html" style="background-color:black;"> <button class="bar-button">Legal Stages</button></a>
				<a href="./../stagepick.html" style="background-color:black;"> <button class="bar-button">Stage Counter Picks</button></a>
				<a href="https://ultimateframedata.com/smash" style="background-color:black;"> <button class="bar-button">Frame Data</button></a>
				<a href="https://smasharchives.com/character" style="background-color:black;"> <button class="bar-button">MatchUp Vods</button></a>
			</center>

			<center>
				<h1 class="title" style="background-image:url(https://www.smashbros.com//assets_v2/img/fighter/thumb_h/%THUMB_NAME%.png);">Playing %NAME%</h1>
			</center>
		</center>
		<div class="main-content">
			<h2>Character Discord</h2>
			<a href="https://discord.com/invite/%DISCORD%">https://discord.com/invite/%DISCORD%</a>
			
			<h2>Guides</h2>
			%GUIDE%
		</div>
	</body>
</html>
"""
play_html = """<html>
	<head>
		<title>Smash-Ultimate - Play</title>
		<link rel="stylesheet" href="./css/dark-colors.css">
		<link rel="stylesheet" href="./css/dark-mode.css">
		<link rel="stylesheet" href="./css/main.css">
		<link rel="shortcut icon" href="https://www.smashbros.com/ja_JP/assets_v2/img/howtoplay/mode_label_ico01.svg">
	</head>
	<body>
		<center style="background-color:black;">
			<a href="./index.html"><img src="./res/lineup.png" alt="Smash Line Up" style="width:100%;max-width: 1000px;"></a>
			<br>
			
			<center class="bar">
				<a href="./info.html" style="background-color:black;"> <button class="bar-button">Character Info</button></a>
				<a href="./play.html" style="background-color:black;"> <button class="bar-button">How To Play A Character</button></a>
				<a href="./main.html" style="background-color:black;"> <button class="bar-button">Find A Main</button></a>
				<a href="./basics.html" style="background-color:black;"> <button class="bar-button">How TO Smash</button></a>
				<a href="./stages.html" style="background-color:black;"> <button class="bar-button">Legal Stages</button></a>
				<a href="./stagepick.html" style="background-color:black;"> <button class="bar-button">Stage Counter Picks</button></a>
				<a href="https://ultimateframedata.com/smash" style="background-color:black;"> <button class="bar-button">Frame Data</button></a>
				<a href="https://smasharchives.com/character" style="background-color:black;"> <button class="bar-button">MatchUp Vods</button></a>
			</center>
			
			<h1 class="title">Play Character</h1>
		</center>
		
		<div class="main-content" style="margin: 0px; max-width: 100%;">
			<center>
				%URLS%
			</center>
			
			<button id="to_top">«</button>
		</div>
	</body>
	
	<script src="js/back_to_top.js"></script>
</html>

"""

info_html = """<html>
	<head>
		<title>Smash-Ultimate - Info</title>
		<link rel="stylesheet" href="./css/dark-colors.css">
		<link rel="stylesheet" href="./css/dark-mode.css">
		<link rel="stylesheet" href="./css/main.css">
		<link rel="shortcut icon" href="https://www.smashbros.com/ja_JP/assets_v2/img/howtoplay/mode_label_ico01.svg">
	</head>
	<body>
		<center style="background-color:black;">
			<a href="./index.html"><img src="./res/lineup.png" alt="Smash Line Up" style="width:100%;max-width: 1000px;"></a>
			<br>
			
			<center class="bar">
				<a href="./info.html" style="background-color:black;"> <button class="bar-button">Character Info</button></a>
				<a href="./play.html" style="background-color:black;"> <button class="bar-button">How To Play A Character</button></a>
				<a href="./main.html" style="background-color:black;"> <button class="bar-button">Find A Main</button></a>
				<a href="./basics.html" style="background-color:black;"> <button class="bar-button">How TO Smash</button></a>
				<a href="./stages.html" style="background-color:black;"> <button class="bar-button">Legal Stages</button></a>
				<a href="./stagepick.html" style="background-color:black;"> <button class="bar-button">Stage Counter Picks</button></a>
				<a href="https://ultimateframedata.com/smash" style="background-color:black;"> <button class="bar-button">Frame Data</button></a>
				<a href="https://smasharchives.com/character" style="background-color:black;"> <button class="bar-button">MatchUp Vods</button></a>
			</center>
			
			<h1 class="title">Character Info</h1>
		</center>
		
		<div class="main-content" style="margin: 0px; max-width: 100%;">
			<center>
			    %URLS%
			</center>
			
			<button id="to_top">«</button>
		</div>
	</body>
	
	<script src="js/back_to_top.js"></script>
</html>

"""
stages_html = """<html>
	<head>
		<title>Smash-Ultimate - Match Ups</title>
		<link rel="stylesheet" href="./css/dark-colors.css">
		<link rel="stylesheet" href="./css/dark-mode.css">
		<link rel="stylesheet" href="./css/main.css">
		<link rel="shortcut icon" href="https://www.smashbros.com/ja_JP/assets_v2/img/howtoplay/mode_label_ico01.svg">
	</head>
	<body>
		<center style="background-color:black;">
			<a href="./index.html"><img src="./res/lineup.png" alt="Smash Line Up" style="width:100%;max-width: 1000px;"></a>
			<br>
			
			<center class="bar">
				<a href="./info.html" style="background-color:black;"> <button class="bar-button">Character Info</button></a>
				<a href="./play.html" style="background-color:black;"> <button class="bar-button">How To Play A Character</button></a>
				<a href="./main.html" style="background-color:black;"> <button class="bar-button">Find A Main</button></a>
				<a href="./basics.html" style="background-color:black;"> <button class="bar-button">How TO Smash</button></a>
				<a href="./stages.html" style="background-color:black;"> <button class="bar-button">Legal Stages</button></a>
				<a href="./stagepick.html" style="background-color:black;"> <button class="bar-button">Stage Counter Picks</button></a>
				<a href="https://ultimateframedata.com/smash" style="background-color:black;"> <button class="bar-button">Frame Data</button></a>
				<a href="https://smasharchives.com/character" style="background-color:black;"> <button class="bar-button">MatchUp Vods</button></a>
			</center>
			
			<h1 class="title" id="StageHeader">Pick who your playing</h1>
		</center>
		
		<div class="main-content" style="margin: 0px; max-width: 100%;">
			<center>
				%URLS%
			</center>
			
			<button id="to_top">«</button>
		</div>
	</body>
	
	<script src="js/back_to_top.js"></script>
	<script>
        function Go(c){
            mychar = (new URLSearchParams(location.search)).get("mychar")
            opchar = (new URLSearchParams(location.search)).get("opchar")
            if (mychar){
                window.location = "https://www.ssbu-stage-guides.com/matchups/"+mychar+"/"+c
            } else if (opchar){
                window.location = "https://www.ssbu-stage-guides.com/matchups/"+c+"/"+opchar
            } else {
                window.location += "?mychar="+c
            }
        }
        window.onload = function(){
            if ((new URLSearchParams(location.search)).get("mychar")) {
                document.getElementById("StageHeader").innerHTML = "Pick your opponent"
            }
        }
    </script>
</html>

"""


def video(id_):
    back = ord("\\")
    return f"""<iframe width="640" height = "400" src="https://www.youtube.com/embed/{id_.replace('"', chr(back) + '"')}"></iframe><br>"""


def char_link(url, thumb, name):
    return f"""<a href="./{url}.html"><button class="char-button" style="background-image:url(https://www.smashbros.com//assets_v2/img/fighter/thumb_h/{thumb}.png);">{name}</button></a>"""


def char_button(url, thumb, name):
    return f"""<button class="char-button" style="background-image:url(https://www.smashbros.com//assets_v2/img/fighter/thumb_h/{thumb}.png);" onclick="Go('{url}')">{name}</button>"""


def char_icon(c):
    return f"""<img width=40px height=40px src="https://smasharchives.com//assets/stock/{c}.png"></img>"""


def stage(name):
    stages = {
        "Battlefield": "stage_img1",
        "Final Destination": "stage_img3",
        "Small Battlefield": "stage_img104",
        "Dream Land": "stage_img8",
        "Smashville": "stage_img44",
        "Pokemon Stadium 2": "stage_img40",
        "Town and City": "stage_img85_en",
        "Hollow Bastion": "stage_addition_img11",
        "Kalos": "stage_img79",
        "Yoshi's Story": "stage_img19",
        "Lylat Cruise": "stage_img39",
        "Yoshi's Island": "stage_img37",
        "PS1": "stage_img24",
        "Unova": "stage_img62",
        "Wily Castle": "stage_img94",
    }
    return f"""<span class="stage">
        <img src="https://www.smashbros.com/assets_v2/img/stage/{stages[name]}.jpg" width=300 />
        <center>{name}</center>
    </span>"""


import json

with open("data.json") as fp:
    data = json.load(fp)

info_buttons = ""
play_buttons = ""
stage_buttons = ""

for full_name in data:
    if not full_name: continue
    char = data[full_name]["name"]

    d = data[full_name]
    id_ = d["number"]

    info_buttons += char_link("info/" + char, d["thumb_name"], d["name"]) + "\n"
    play_buttons += char_link("play/" + char, d["thumb_name"], d["name"]) + "\n"
    stage_buttons += char_button(d["stages_url"], d["thumb_name"], d["name"]) + "\n"

    mus = ""
    for mu in data[full_name]["matchups"]:
        if data[full_name]["matchups"][mu] and mu != "-":
            name = {"3": "Strong win (+3)", "2": "Easy win (+2)", "1": "Win (+1)", "0.5": "Slight win (+0.5)", "0": "Even (0)",
                    "-0.5": "Slight loss (-0.5)", "-1": "Loss (-1)", "-2": "Major Loss (-2)", "-3": "Not winning (-3)"}[mu]
            icons = "\n".join(char_icon(c) for c in data[full_name]["matchups"][mu])
            mus += f"<h2>{name}</h2><div style='margin-left: 50px;'>{icons}</div>"

    info = (
        info_base
        .replace("%NAME%", d["name"])
        .replace("%MU%", "https://smasharchives.com/character/" + str(id_))
        .replace("%THUMB_NAME%", d["thumb_name"])
        .replace("%FRAMEDATA%", d["frame"])
        .replace("%VIDEO%", "\n".join([video(v) for v in d["beat"]]))
        .replace("%STAGE_URL%", d["stages_url"])
        .replace("%GOOD_STAGES%", "\n".join([stage(s) for s in d["stages"][0:3]]))
        .replace("%BAD_STAGES%", "\n".join([stage(s) for s in d["stages"][-3:][::-1]]))
        .replace("%MUS%", mus)
    )

    if d["tips"]:
        info = info.replace("%TIPS%", "<li>" + ("</li>\n<li>".join(d["tips"])) + "</li>")
    else:
        info = info.replace("%TIPS%", "None")

    play = (
        play_base
        .replace("%NAME%", d["name"])
        .replace("%THUMB_NAME%", d["thumb_name"])
        .replace("%GUIDE%", "\n".join([video(v) for v in d["guides"]]))
        .replace("%DISCORD%", d["discord"])
    )

    with open("./../play/" + char + ".html", "w", encoding="UTF-8") as fp:
        fp.write(play)
    with open("./../info/" + char + ".html", "w", encoding="UTF-8") as fp:
        fp.write(info)
with open("./../play.html", "w", encoding="UTF-8") as fp:
    fp.write(play_html.replace("%URLS%", play_buttons))
with open("./../info.html", "w", encoding="UTF-8") as fp:
    fp.write(info_html.replace("%URLS%", info_buttons))
with open("./../stagepick.html", "w", encoding="UTF-8") as fp:
    fp.write(stages_html.replace("%URLS%", stage_buttons))
#

[
    "YL, TL"
    "WSep92_Z4CU",
    "BYIZBipUIIU",

    "YDYO5vVrsk8",
    "D0Ml1w6rUmo"
]
