info_base = """<html>
	<head>
		<title>Smash-Ultimate - Info - %NAME%</title>
		<link rel="stylesheet" href="./../css/dark-colors.css">
		<link rel="stylesheet" href="./../css/dark-mode.css">
		<link rel="stylesheet" href="./../css/main.css">
		<link rel="icon" type="image/x-icon" href="./../res/icon.ico">
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
				<a href="https://ultimateframedata.com/smash" style="background-color:black;"> <button class="bar-button">Frame Data</button></a>
				<a href="https://smasharchives.com/character" style="background-color:black;"> <button class="bar-button">MatchUp Vods</button></a>
			</center>
			
			<center>
				<h1 class="title" style="background-image:url(https://www.smashbros.com//assets_v2/img/fighter/thumb_h/%THUMB_NAME%.png);">%NAME%</h1>
			</center>
		</center>
		<div class="main-content">
			<h1>Prefered Stages</h1>
			<ul>
%STAGES%
			</ul>
			
			<h1>Strengths</h1>
			<ul>
%STR%
			</ul>
			
			<h1>Weaknesses</h1>
			<ul>
%WEAK%
			</ul>
			
			<h1>Notes</h1>
			<ul>
%NOTES%
			</ul>
			
			<h1>Video on How To Beat Them</h1>
			%VIDEO%
			
			<h1><a href="https://ultimateframedata.com/%FRAMEDATA%">Ultimate Frame-Data</a></h1>
			<h1><a href="%MU%">Match Up Vods</a></h1>
			<!--<center><embed id="framedata" src="https://ultimateframedata.com/%FRAMEDATA%" width="1000px" height="100%"></embed></center>-->
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
		<link rel="icon" type="image/x-icon" href="./../res/icon.ico">
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
				<a href="https://ultimateframedata.com/smash" style="background-color:black;"> <button class="bar-button">Frame Data</button></a>
				<a href="https://smasharchives.com/character" style="background-color:black;"> <button class="bar-button">MatchUp Vods</button></a>
			</center>
			
			<center>
				<h1 class="title" style="background-image:url(https://www.smashbros.com//assets_v2/img/fighter/thumb_h/%THUMB_NAME%.png);">Playing %NAME%</h1>
			</center>
		</center>
		<div class="main-content">
			<h2>General Guide</h2>
			%GUIDE%
			
			<h1>Combo Guide</h1>
			%COMBO%
			
			<h2>Character Discord</h2>
			<a href="https://discord.com/invite/%DISCORD%">https://discord.com/invite/%DISCORD%</a>
		</div>
	</body>
</html>
"""

def video(id_):
    return """<iframe width="640" height = "400" src="https://www.youtube.com/embed/"""+id_+""""></iframe><br>"""

			
#<!--https://www.youtube.com/watch?v=29c6-AJr8LY-->

import json

data = json.load(open("./data.json"))

for char in data:
    if not char: continue
    
    d = data[char]
    id_ = list(data).index(char) + 1

    info = (
        info_base
        .replace("%NAME%", d["name"])
        .replace("%MU%", "https://smasharchives.com/character/"+str(id_))
        .replace("%THUMB_NAME%", d["thumb_name"])
        .replace("%FRAMEDATA%", d["frame"])
        .replace("%VIDEO%", "\n".join([video(v) for v in d["beat"]]))
    )
    
    if d["stages"]:
        info = info.replace("%STAGES%", "<li>" + ("</li>\n<li>".join(d["stages"])) + "</li>")
    else:
        info = info.replace("%STAGES%", "None")
    
    if d["str"]:
        info = info.replace("%STR%", "<li>" + ("</li>\n<li>".join(d["str"])) + "</li>")
    else:
        info = info.replace("%STR%", "None")
    
    if d["weak"]:
        info = info.replace("%WEAK%", "<li>" + ("</li>\n<li>".join(d["weak"])) + "</li>")
    else:
        info = info.replace("%WEAK%", "None")
    
    if d["notes"]:
        info = info.replace("%NOTES%", "<li>" + ("</li>\n<li>".join(d["notes"])) + "</li>")
    else:
        info = info.replace("%NOTES%", "None")

    
    play = (
        play_base
        .replace("%NAME%", d["name"])
        .replace("%THUMB_NAME%", d["thumb_name"])
        .replace("%GUIDE%", "\n".join([video(v) for v in d["guide"]]))
        .replace("%COMBO%", "\n".join([video(v) for v in d["combo"]]))
        .replace("%DISCORD%", d["discord"])
    )

    with open("./play/"+char+".html", "w") as fp:
        fp.write(play)
    with open("./info/"+char+".html", "w") as fp:
        fp.write(info)

