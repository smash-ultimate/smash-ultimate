info_base = """<html>
	<head>
		<title>Smash-Ultimate - Info - %NAME%</title>
		<link rel="stylesheet" href="./../css/dark-colors.css">
		<link rel="stylesheet" href="./../css/dark-mode.css">
		<link rel="stylesheet" href="./../css/main.css">
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
			<iframe width="1000px" height = "500px"
				src="https://www.youtube.com/embed/%VIDEO%">
			</iframe>
			
			<!--https://www.youtube.com/watch?v=29c6-AJr8LY-->
			
			<h1>Ultimate Frame-Data</h1>
			<center><embed type="text/html" src="https://ultimateframedata.com/%FRAMEDATA%" width="1000px" height="15250px"></center>
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
			</center>
			
			<center>
				<h1 class="title" style="background-image:url(https://www.smashbros.com//assets_v2/img/fighter/thumb_h/%THUMB_NAME%.png);">Playing %NAME%</h1>
			</center>
		</center>
		<div class="main-content">
			<h2>General Guide</h2>
			<iframe width="640" height = "400"
				src="https://www.youtube.com/embed/%GUIDE%">
			</iframe>
			<br>
			
			<h1>Combo Guide</h1>
			<iframe width="640" height = "400"
				src="https://www.youtube.com/embed/%COMBO%">
			</iframe>
			<br>
			
			<h2>Character Discord</h2>
			<a href="https://discord.com/invite/%DISCORD%">https://discord.com/invite/%DISCORD%</a>
		</div>
	</body>
</html>
"""


import json

data = json.load(open("./data.json"))

for char in data:
    if not char: continue
    
    d = data[char]

    info = info_base.replace("%NAME%", d["name"]).replace("%THUMB_NAME%", d["thumb_name"]).replace("%FRAMEDATA%", d["frame"]).replace("%VIDEO%", d["beat"])
    if d["stages"]:
        info = info.replace("%STAGES%", "<li>" + ("</li><li>".join(d["stages"])) + "</li>")
    else:
        info = info.replace("%STAGES%", "None")
    
    if d["str"]:
        info = info.replace("%STR%", "<li>" + ("</li><li>".join(d["str"])) + "</li>")
    else:
        info = info.replace("%STR%", "None")
    
    if d["weak"]:
        info = info.replace("%WEAK%", "<li>" + ("</li><li>".join(d["weak"])) + "</li>")
    else:
        info = info.replace("%WEAK%", "None")
    
    if d["notes"]:
        info = info.replace("%NOTES%", "<li>" + ("</li><li>".join(d["notes"])) + "</li>")
    else:
        info = info.replace("%NOTES%", "None")

    
    play = play_base.replace("%NAME%", d["name"]).replace("%GUIDE%", d["guide"]).replace("%COMBO%", d["combo"]).replace("%DISCORD%", d["discord"])

    with open("./play/"+char+".html", "w") as fp:
        fp.write(play)
    with open("./info/"+char+".html", "w") as fp:
        fp.write(info)

