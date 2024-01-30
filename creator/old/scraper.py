import re

import scrapetube

chars_text = """1
MARIO
2
DONKEY KONG
3
LINK
4
SAMUS
4e
DARK SAMUS
5
YOSHI
6
KIRBY
7
FOX
8
PIKACHU
9
LUIGI
10
NESS
11
CAPTAIN FALCON
12
JIGGLYPUFF
13e
PEACH
13
DAISY
14
BOWSER
15
ICE CLIMBERS
16
SHEIK
17
ZELDA
18
DR. MARIO
19
PICHU
20
FALCO
21
MARTH
21e
LUCINA
22
YOUNG LINK
23
GANONDORF
24
MEWTWO
25
ROY
25e
CHROM
26
MR. GAME AND WATCH
27
META KNIGHT
28
PIT
28e
DARK PIT
29
ZERO SUIT SAMUS/ZSS/ZERO SUIT SAMUS
30
WARIO
31
SNAKE
32
IKE
33
Squirtle/POKéMON TRAINER/PT/POKEMON TRAINER
33
Ivysaur/POKéMON TRAINER/PT/POKEMON TRAINER
33
Charizard/POKéMON TRAINER/PT/POKEMON TRAINER
36
DIDDY KONG
37
LUCAS
38
SONIC
39
KING DEDEDE
40
OLIMAR
41
LUCARIO
42
ROB/R.O.B.
43
TOON LINK
44
WOLF
45
VILLAGER
46
MEGA MAN
47
Wii Fit TRAINER
48
ROSALINA AND LUMA
49
LITTLE MAC
50
GRENINJA
51
Mii Brawler/mii_fighter
52
Mii Swordfighter/mii_fighter
53
Mii Gunner/mii_fighter
54
PALUTENA
55
PAC-MAN
56
ROBIN
57
SHULK
58
BOWSER JR.
59
DUCK HUNT
60
RYU/KEN
61
CLOUD
62
CORRIN
63
BAYONETTA
64
INKLING
65
RIDLEY
66
SIMON/RICHTER
67
KING K. ROOL
68
ISABELLE/shizue
69
INCINEROAR/gaogaen
70
PIRANHA PLANT/packun_flower
71
JOKER
72
HERO/dq_hero
73
BANJO/BANJO AND KAZOOIE
74
TERRY
75
BYLETH
76
MIN MIN/minmin
77
STEVE
78
SEPHIROTH
79
PYRA/homura
79
MYTHRA/homura
81
KAZUYA
82
SORA"""

weakness_str = """Mario: 
Punish his poor recovery
Mario’s jump (a lot) so intercept that
Bait out fair, then up-b to intercept
Donkey Kong: 
Keep him in the air
Punish his landing
Punish his recovery, you can hit his head
He gets combo’d easily, so use that to your advantage
Look out for his side-b, if you see it spot dodge, it’s a shield breaker, and it’ll bury you 
Link: 
Jump over the projectile rain
Once through, fight him close-up where he can't set up projectiles but watch out for his long lingering up smash and forward smashes.  
Walk, don't run. You can shield while walking but not during the initial dash. 
Slow ground game
Shield grab
Samus: 
Punish her cooldowns
Always keep charge shot in the back of your mind, be ready for it
Poor horizontal recovery
Samus players normally like to camp at beginning until opponent is at high percent so try to stay up close with them
Dark Samus: 
Same thing as Samus, but when punishing her jumps you should expect her to go a bit higher than Samus (floaty)
Yoshi: 
Shielding his dair, Ivysaurs up air goes through yoshi’s dair. There are a lot of characters that do go through it but it's a lot harder to do than with ivysaurs. Bait out the dair and punish because it has pretty long end lag
Space him out, preferably with a long disjoint
Watch out for that offstage game, avoid him offstage unless you’re above him
Always look out for that fair, high damage and it spikes
Don’t try to intercept start of double jump due to super armor
Kirby: 
Out range and/or use speed
Hammer hits twice in the air, look out for that, but it has a little more ending lag then usual ending lag so go for a tilt punish when they land
Almost all of Kirby's special moves have a lot of end lag. Just wait/bait out their special attacks and punish from there
Try and gimp when offstage due to up B coming back down
Watch for up B landing on stage (some characters can intercept with a wind box)
Be careful when edge guarding; his Up B can spike at any percent
Fox: 
Punish his recovery
Beware nair -> jab
Use shield more than usual due to lack of good kill throws or combo throws
Poor edgeguarding other than shine spike
Watch out for dash attack and nair
Easily comboed as he is a fast faller
Pikachu: 
Watch out for b-air off stage, it can drag you to the blast zone
Always avoid Pikachu when he’s coming at you off stage, recover low, high, or just die so you don’t get b-air chained to the blast zone
Watch out for lighting loops
I would explain how to escape nair loops, but this video explains it much better than I can. yay video
Try and mix up how u react to neutral b - don’t always jump or shield as he can usually get a grab or an aerial
Luigi: 
Don’t get grabbed at 0% (avoid grabs in general), taking damage is better than getting grabbed so just jump around, stay on platforms till you’re like 10% depending on weight and fall speed and then start playing the game
After Green Missile his recovery his painfully easy to gimp, so just wait until he’s across then hit him with pretty much anything
Don’t get too close to his shield at 70% due to Up B oos
Ness:
Always shield PK Fire, then grab him as he goes in for an attack
Try to intercept his PK Thunder with a reflector if you have one
Lots of Ness mains go for either a grab, or do another PK Fire after a PK Fire, so either shield again or go for that spot dodge and get the punish
Always try and intercept his jump offstage then go for gimping his up B
Watch out for pk thunder 2 on stage. If you hit the head of pk thunder it will stop it
Watch out for yoyo on ledge
Ness is very very floaty so force him to jump and take advantage in air and off stage
If your character has a counter, use it against Ness’s recovery
Captain Falcon: 
Space him out with projectiles before punishing a whiffed Side B 
Captain Falcon has a similar moveset to Ganondorf and like with ganondorf if they try to falcon punch you, go for the counter.
Expect side b, grab, and nair most in the neutral, so bait each out with whatever your character has to offer like disjoints, projectiles, dash back, spotdodge, etc and keep in mind that falcon is fairly easy combo food.
ROCKCROCKING. Basically punishing his up b recovery by teching it off a wall (if the stage has it) into an easy edgeguard (or just intercept it with a safe aerial if they recover at a bad angle)
Falcon doesn’t have much against shield pressure behind him, or many great out of shield options in general. Nair doesn’t hit behind him and can sometimes whiff on really small characters (Pichu privilege). Up b has quite a bit of startup on the ground and can be reacted to and can be easily punished. Grab is fast but only in front of Falcon.
In general Falcon’s disadvantage is pretty bad so once you force him into it try to keep him there.
Always di away for down throw
Combo food
Jigglypuff: 
Punish missed aerials, be careful of late hit boxes
Good spacing will punish hard
Try to parry rest (nice try Jiggs mains, just shield rest unless you want max style points) or counter it.
Is really light, you can take a stock off her earlier most of the time. Also shield-breakers are able to instantly kill her as well.
Sing and Rest are really easy to punish once blocked or whiffed.
Her rollout tends to be pretty predictable at times, so countering it would be an optimal choice.
Watch out for the sing hitbox. it’s bigger than it seems. It even hits under platforms, if the Jiggs is singing on the platform.
Beat out her aerials due to poor priority
Easy to edge guard
Bad airdodge
Easy to edgeguard
Poor ground game
Bad grabs and throws
Pound (sideB) is actually a disjointed hitbox, so it will win Jiggs a number of trades. Furthermore, it does significant shield damage (only taking 2-3 to break a shield). Luckily though, it is very punishable. If your shield is strong, block it and punish. If your shield is weak, stay evasive until the shield recovers.
Peach: 
As soon as they get a turnip, play safe (safer than usual vs Daisy)
Predict and punish float (over) usage with a good aerial/anti-air
Pay attention to their down-b to see if they got a Mr.Saturn or Bob-omb
Sword characters have an advantage over peach since they have a bigger hitbox then her.Space her out and she won’t be able to get you
Watch out for down tilt
Daisy: 
Same as Peach
Daisy has a thicker hitbox than Peach but Peach has a taller one
Bowser: 
Heavy start/end lag on a lot of attacks, take opportunities to punish
Probably the easiest character to juggle/combo in the game. Just try not to get hit. 
Don’t stay in shield, Bowsers love side B
Up Smash and down smash has super armor, try to stay away when he’s charging, get the punish after the attack
Bowser has little to do when dealing with zoners.If your character has projectiles use them to force shield or neural b
Tough guy allows him at low percentages to take no knockback from weak moves. Meaning try to stay away from reactable moves like rapid jab before you get punished.
Watch out for Bowser mains trying to land with down air. It has a large hitbox but can be predictable so just wait in shield to then punish after they land if you see them going for it (has a landing hitbox that’s really big on the ground so it’s best to just wait till he lands and don’t run into it)
Watch out for up b out of shield
Watch out for down b out of shield as it can shield break
Ice Climbers: 
Kill Nana for easy wins
Without Nana the player has a little mac recovery
Watch out for de syncs
Poor approach game
You can spam Pikachu’s and Pichu’s neutral special to gimp their up-special.
Sheik: 
She is a light character and she has very few kill moves
Poor high percent kill throws
Watch out for f throw bouncing fish
Grab more than usual as it is easier to lay hits on her after a grab
Zelda: 
Get in close and don’t let her catch her breath
Din’s Fire and The Phantom (her JoJo stand) can be reflected against her.
Nayru’s Love is easy to bait out or shield. Punish accordingly
Poor horizontal aerial hitboxes
Dr. Mario: 
Gimp,gimp,gimp
Gimp Again
Out space (and, of course, gimp)
An even worse recovery than Mario's up b so it’s even easier to gimp.(Keep in mind that Dr Mario has more kill power though.)
Punish the double jump to leave him with only his lackluster Up+B
Unless you’re playing a super heavy hitter, Dr Mario will be at an advantage with most trades. Don’t opt to trade blows unless he’s at kill% or near off-stage.
Try to pick stages with higher platforms, or no platforms at all, that way d-throw->downB no longer works for Doc as a true low% combo.
Pichu: 
Ask Sakurai to nerf (I mean pichu has been falling off lately and is the lightest in the game)
Disjoints are your best friends
Go for kills earlier, since Pichu’s glaring weakness is being a lightweight.
Pichu has a very small hurtbox and can be annoying to deal with.Use downtilts more that side tilt and use range whether it is projectiles or a fat hitbox to your advantage
Pichu’s recovery(Up B) has no hitbox so when off stage predict where pichu is going to be and attack or even better, spike pichu
Pichu can’t deal with opponents with very large hurtboxes.(E.g Ike’s Nair)Since pichu doesn't have the range to deal with stuff space pichu out.
Pichu has one of the worst disadvantages in the game if the opponent is a stock higher than them.But also has the strongest advantages in the game (If the opponent has a stock less than them). Pichu’s game plan is rather aggressive so let the pichu go for you then after they attack punish.
Falco: 
Punish recovery
Watch out for up tilt
Side B is shieldable
Marth: 
Gimp the recovery
Avoid the tip
Is a shittier version of Lucina.
Rushdown more than lucina
Lucina: 
Gimp the recovery
Always hold shield against dancing sword (her side-b) because you’ll either block all the hits, or she’ll stop and have a lot of ending lag giving you time to leave shield and punish
Young Link: 
Pray to God they can’t ladder projectiles into Up B
Shield a lot, but don’t shield to the point your shield will inevitably break.
Look out for those down angled boomerangs to f-air, it kills at around 80 if your near the edge of the stage 
Watch out for arrows
Pressure with close combat since young link prefers to camp
Very light character so go for kill moves early
Ganondorf: 
Heavy start/end lag on attacks, take opportunity to punish
Poor recovery, bait out double jump then just one hit could do it
If your character has a counter, use it against his smash attacks
Avoid Warlock punch because it has a good amount of super armour, it can turn as well, but it has to start turning right away or it will not - A grab will cancel it so you can punish that way
Don’t forget to counter Warlock Punch because he instantly gets yeeted once that happens. (A free stock for you)
For Gods sake stop shielding his up tilt (big explosion kick = shield breaky-breaky)
Any spammable projectile can deal with his slow approach and large size (g&w chef for example).
Watch out for f smash and nair hitboxes as they go behind him
Mewtwo: 
Has to use his jump a lot and is a very weak character in the air just like little mac.
Mewtwo is pretty light and has a rather large hitbox.Use this to your advantage
Watch out for shadow ball as it can confirm into other hits as well as kill by itself
If you have a disjoint, keep in mind that if you use it against mewtwo upair/bair you will straight out win every time if timed properly. His tail is one massive hurtbox. Even without disjoints you can usually trade with those two moves
Trading IS GREAT against Mewtwo for midweights and heavyweights. Mewtwo is very light so he will reach kill percent before you if you are able to do smart trades with him.
Keep Mewtwo’s specials in the back of your mind. Most of them are pretty situational, but you may still be caught off guard by down b or up b in neutral. Also keep in mind that side b reflects and depending on character Mewtwo can confirm it into Fair at 150+ and kill you.
Roy: 
Try to stay spaced, his sword does more damage closer to the hilt
Watch out for side b is basically cross slash
Easy to gimp
Chrom: 
Bait out double jump and can gimp super early
Easy method for gimping is (if you have one) to counter. Almost guaranteed kill (sometimes they get lucky when they are hit and can airdodge to stage or their up b will barely sweetspot stage and not hit you by pixels sometimes). If you don’t have a counter, some spikes are pretty guaranteed if you hit Chrom at the max height of up b.
Also some rapid jabs if they are disjointed
 Mr. Game and Watch: 
Can hit hard, but one of the lighter characters in the game
Careful with spamming ranged into his bucket
Shield when he D-airs, and then grab if he’s in front. 
The bomb f-air can be instantly dispersed by literally every single move.
His bomb f-air can be reflected
Be very wary with his neutral air, it’s a larger disjoint than you might expect, plus it combos well into upair/upb/bair.
Down smash buries at the edges of the hammer (sweetspot), but the sourspot towards the middle is survivable / techable and allows you to reset to neutral if need be. Don’t roll towards the game and watch though, as that could lead you into another down smash. Down smash has long bury time and leads into early kills with f smash
Do NOT try to edgeguard game and watch. They have a better recovery than you, and can reverse edgeguard you with ease.
Do NOT challenge up b, it comes out as a frame 3 out of shield option with startup invincibility frames. Do not be surprised if your throw to upair combos don’t work because of this move. Always shield near a game and watch, as it’s more likely that they will up b rather than grab you.
Down b (bucket) both reflects and absorbs, but has some endlag upon use. Try to punish them when their bucket is out.
Watch out for up b oos
Neutral b (chef) is deceptively great on ledge. It’s controllable by tilting left and right, meaning if you try to approach g&w with it being used, they can angle it upwards like a wall to combo you back into the attack. Also, it can very easily two frame on ledge, and due to up b, a game and watch can up b if you eventually get behind their chef. The best way to approach is to time the small food gap that occurs with high end lag (around every 4 or 5 pieces of food should have a gap in timing).
Game and watch does not have a lot of kill options, so you should get used to recognizing them.
Drag down nair into ftilt/dilt, it’s a true combo so you won’t be able to shield the final hit.
2 pieces of chef near ledge into a runup ftilt.
(Tri-platforms only) Upb (below top platform) -> Upair -> Upb (doesn’t connect, g&w is now on the top platform) -> Upair. This can kill you off the top if you aren’t careful.
Fair bomb into reverse f-tilt.
Downthrow into nair into judge at lower percents.
Nair into bair into bair into upb next to the blast zone, this is g&w’s wall of pain, and you need to DI towards the blast zone to avoid the last hit of upb if you want to survive.
Downsmash burying into upsmash or fsmash (sweetspot0, very spammable and hard to punish. Honestly, this is probably the most reliable kill move for g&w, so expect this the most. You need to mash HARD if you want to escape the bury state. Above 75%, you’re likely dead though.
Meta Knight: 
Keep him at arm’s length and careful when offstage, that’s mk’s strength
All of his special moves leave him at a fall state and have quite a bit of ending lag. Punish after shielding move.
Watch out for up air ladders into up b
Pit: 
Don’t forget to reflect his arrows if you have a reflector
Try to keep this MU on the ground unless you have a good air character
Shield side-b, then punish. Punish harder. Punish ultra-hard.
Easy to gimp up b
Dark Pit: 
Arrows don’t have as much control, so jump and weave around them.
One of the major things that makes him different to Pit is that his side b has more killing power than Pit whereas Pit has more combo potential.So avoid getting side b near edges and punish after evading the move.
Zero Suit Samus: 
Down air has quite a bit of end lag so try to punish it when they overuse it as an option for getting back to stage
Poor grab and throws except for up throw past 150%
Watch out for nair into down b at ledge
Watch out for up b oos
Wario: 
Wall him out, preferably with disjoints.
Be wary of Waft.
Try to escape u-tilt and u-air strings if you can. But mostly be cautious of u-air and n-air.
Try and get his bike and protect it as he becomes very easy to gimp
Watch out for f-tilt when hanging at ledge
Watch out for d-tilt into dash attack
Snake: 
Stay up close and personal, his ranged game is insane
A strong hit--like a spike--is usually enough to hit Snake off Cypher. And maybe you can hit him out of a C4 recovery if you predict his DI.
You can slide under grenades or throw them back at Snake, so don’t be afraid. But don’t be reckless by trading or straight-up running into explosions, either.
Always watch where he places c-4
Ike: 
Hug the edges; use range
Punish slow smash attacks
Punish Landings after an aerial
Anti-airs for nair
Hit his up b while he’s at the apex of the move
Attack Ike either before he n-airs (during the start up of the move as he jumps up) or punish it oos
Ike is forced to use side b for horizontal recovery.Use this to your advantage and counter or spike
Ike’s up b can be countered, leaving him at an even worse position
Watch out for nair into bair or up air at high percents
Mix up landings and airdodges as up air is huge
Pokemon Trainer: 
Bear in mind whatever he’ll want to go for with each of his Pokémon and adapt accordingly.
Squirtle: 
Avoid obvious combo starters and punish them if they are too repetitive
Very light
Lack of kill power
Watch out for water gun
Poor recovery
Ivysaur: 
Avoid up air/down air
Start parrying razorleaf
Don’t underestimate his d-air hitbox
Dair at ledge
Watch out for up air  juggles
Razor leaf has poor priority
Watch out for down throw into up b as it kills around 75%
Stay away from above ivysaur, up b and upair can combo into kill super early (jump less)
Charizard: 
Punish Flare Blitz (it is such a bad move right now and is super easy to read and punish)
He can kill you easily at high percent, so try to keep him off of you as much as possible.
Combo food
Poor recovery
Big hurtbox
Bad hitboxes
Watch out for Forward Tilt. Kills early and has great range
Diddy Kong: 
Steal his bananas and use them for yourself
Pretty light.(This isn’t smash 4 Diddy Kong so Kill him)
Easy to gimp up b
Can't kill easily
Throws have poor follow ups
Bair and fair lag
Watch out for nair into dair at ledge kills around 50%
Lucas: 
PK Freeze can be easily punished if the move whiffs.
PK Fire is also punishable if misspaced, so shield it.
Gimp pk thunder
Sonic: 
Easily gimpable recovery. Sonic players usually need to use up b to go back to the stage.Use this to your advantage.
side/down B lose to jabs. If they’re charging at you with a spin dash just hold a jab out and they’ll get stopped dead
Shield spin dashes
King Dedede: 
Punish his cooldowns
Gordos can be easily reflected, even neutral moves seem to do the trick.
Really easy to juggle and has a huge ass hitbox for some reason.
Olimar: 
If he only has 1 or no pikmin punish quickly because it is easy to get more.
No up b hitbox
Smashes are reflectable. Go for reads if you’re feeling brave
Lucario: 
Kill him as early as you can, but keep in mind a high-Aura Aura Sphere or b-air.
Lucario is a generally versatile fighter, so make sure you’re ready to adapt to his style. Lucario isn’t a gimmick anymore.
Lucario has a good combo game at low percent and good kill power when at higher percent.Kill him asap. (Note if you die to a high level aura lucario his combo game is not as good because he does more knockback)
R.O.B.: 
Deny their gyro and beams
Punish side B's
Avoid predictable projectiles, as they will just be reflected back
Recovery can get easily gimped with no hitbox
Big hurt box
Combo food
His only fast aerials are fair and uair. All of the others have some lag before coming out, which should telegraph them. Neutral airdodge is your friend against these while not off-stage (Neutral airdodge has fewer punishable frames than directional airdodge)
Toon Link: 
He can’t land very well (floaty, few landing options)
Slow on ground
Wolf: 
Gimp (watch out for up b hitbox and side b spike)
Wolf’s side b spikes at the end and tip of the move so try not to be in front of him when he recovers horizontally. Furthermore, he can angle it downwards to try to sweetspot you while you are standing on the stage (this works against most characters, except for really short ones). You can purposely sit at this distance to try to bait it out for a shield->punish option.
Villager: 
Punish recovery (It has a glaring hitbox that will surely gimp him)
Watch out for up air
Watch out for tree
Villager got a nerf recently and you are able to shield most of villager’s projectiles.
Villager’s grab is a bit more range than most players but has a lot of end lag if missed
Megaman: 
Up-B punish like Sonic.
Get good at catching his neutral B
Close range is dangerous af. Out space him.
All smashes have horrible lag. Punish that.
Stay out of jab range, it's where a lot of hits can connect.
If he starts charging an fsmash, he’s stuck in place about to shoot a projectile. You can stand right in front of him and reflector, and he won’t be able to cancel it. Same with downB, locking him in place. These options make megaman into reflector food, and he’ll likely be resorting on neutralB and sideB after you punish these a couple of times, limiting his projectile options.
Wii Fit Trainer: 
Be aggressive to not let them charge sunlight
If sunlight is below half charge it is not super scary, little knock back and not crazy damage so do not worry about it too much. After half charge watch out for it, it can kill now and will beat out most projectiles you throw.
Side B can be TERRIFYING if they know what they’re doing. Always keep an eye out for it
When down b is charged run as it is very powerful
Rosalina and Luma: 
Kill Luma when possible and then deal with Rosalina separately
Very tall, very lightweight. Treat her similarly to Mewtwo but she’s got more disjoints
Watch out for luma
Little Mac: 
Punish recovery, if you bait out double jump it is a free kill
Get him in the air, he can’t contest 
Grab him ,yeet him off stage and win
Spam projectiles like you’re trying to get banned from online
Watch out for super armour
Camp on the ledge when he has ko punch
Greninja: 
Pay attention to and punish side b whiffs
Poor rising hitboxes
Be careful when recovering as his counter spikes
Slow grab
Palutena: 
Watch out for up air and nair
Get a feel for when they side b and punish the heavy end lag.
2 frame recovery as it has no hitbox
Poor ground game
Watch out for d-tilt as it 2- frames
Pac-Man: 
Side B is very predictable and has lots of end lag to punish
Aside from projectiles and thousand-IQ plays, his shield pressure isn’t great
Watch out for side b super armour
Poor grab
Pressure when charging projectile
Robin: 
Pay attention to thunder, it is a solid combo starter/kill move/ shield breaker depending on the charge
He can’t spam those projectiles forever, it will be pretty easy to capitalize on him once he runs out on the tomes and Levin Sword, since he’s relatively weak without them.
Shulk: 
When a shulk attempts to side b you shield it then punish
All his arts last around ~8 seconds on average. You can stall him out if necessary
Up b does not clip to ledge try and counter or hit him
Fairly slow ground game
Bowser Jr.: 
Bowser Jr isn’t a hot character right now and loves spacing you out. Just go in close and use large hitboxes to annoy him back
He can’t do squat against shields. Hold your guard up and don’t get grabbed
Remember that you can grab the Mechakoopa(Bowser Jr’s down B) and you can use it for yourself
Duck Hunt: 
Stay aggressive, do not let him set up his specials with can/gun man/etc. 
There is not much he can do up close.
You could try to seperate the can and him, then rush the dog down
Original poster child for Easy Gimp. Get him offstage
His neutralB only bounces in one direction. Whether you attack it, or Duck Hunt attacks it, will change the direction that it bounces. Use this to keep it out of the fight, or use it against to your advantage.
Ryu: 
Read Ken
Ken:  
Don’t jump above him and expect not to get shoryu’d, they always shoryu
Out space
When they start playing safe and stay near ledge, be careful with your moves, if you whiff once they’ll start down-tilting you and doing those SF combos which get you to 999% and then shoryu you 
Don’t stay in shield too long, Ryu has a shieldbreaker move and Ken has a shieldbreaker combo
If they don’t know their SF combos, it’s a free game
Gimp them
Learn the player’s pattern when Ken/Ryu is in the air, they can use their focus to take a hit and go left or right, so keep that in mind
Parry Hadouken, jumping also works (keep in mind point 2) but parry gives style points
Cloud: 
Gimp
Punish trash linear recovery (just hit him once)
Punish all those whiffed fairs
Start parrying bc Cloud players are often really linear
Learn to parry last hit of CS against shield, it’s pretty easy
Pick Pichu/Pikachu (free game)
Don’t let him breathe, picking fast characters makes this easy
Don’t use your jump off-stage early (I mean you shouldn’t do that in general) bc then he can just walk off nair your ass 
When a stock down, don’t try to gimp him off stage from above, or he’ll CH suicide you
When he has limit, be careful, like in general. Generally when you’re just avoiding him we’ll just attempt to hit you with limit BB, which 9 out of 10 times wont hit but we’re still crying about limit nerfs so we do it anyways. 
You should probably be more careful about your landing when he has limit, Finishing Touch will kill everyone at like 70% so Clouds will be looking to bait out your move and clap you with it. It has a shit ton of startup and endlag though so if you see him attempt to use it close to you (and you’re not in endlag yourself) you can just tap him out of it with a fast move (like a nair)
If you’re still practicing parrying vs Cloud, shielding is also good, his grab is trash with literally no follow ups
dtilt->(utilt or uair) isn’t a true combo. Hold shield immediately after they unfortunately hit you with the dtilt to insta-airdodge the follow  up.
Dash attack kill power is extremely di dependent
Corrin:  
Hold shield through their side-b, and remember that they can reverse side-b
Make sure to either stay really close, or really, really far, the f-smash tipper is devastating  
Poor recovery
Watch for chainsaw on smash attacks
Watch for neutral b bite
Bayonetta: 
Bayonetta likes to combo but her moves have a lot of lag. Be fairly liberal with shields, dodges and counters
Can’t kill
Up b doesn’t clip to ledge
Inkling: 
Avoid ink if you can and attack them when they are trying to recharge their ink
Side B has a lot of end lag.Use this to your advantage and shield or spot dodge when you know it is coming and punish
Apply constant rundown pressure if the Inkling is ever 100% completely out of ink. They desperately want breathing space in this moment, as a significant part of their kit is nerfed until they find a gap to get some ink: smashes weaker, jab weaker, f-throw weaker, no specials other than recovery.
Not the best kill power
Watch for nair strings
Watch out for roller ← Roller is extremely unsafe on shield, so block and punish if applicable.
Ridley: 
Punish down b due to lot of end lag
Look out for the Up-B spike
He is lighter than you think (Fun fact he has the same weight as Ike)
He’s big, combo food
Neutral B can be hit while charging to cause Ridley to take damage and be stunned- will take no knock back
Watch out for nair and fair strings
Has very poor landing and recovery options, so keep him juggled but don’t overcommit so you can punish his options.
Jump over side b then punish
Easy to gimp due to poor jumps and high up b start up
Remember that when Ridley side b’s you, you can mash out to get out of it a low percentages
Simon: 
Punish recovery
Will try to stay near the edge and projectile spam. Be patient and wait for an opening to get close.
Remember that Holy Water will activate any bomb-related projectiles, so be careful of throwing them against a Simon.
Richter: 
Punish recovery
Will try to stay near the edge and projectile spam. Be patient and wait for an opening to get close.
Small hitboxes
King K. Rool: 
Careful of super armor, attempt to punish neutral b/side b due to lots of lag
If your character deals a lot of damage, try to break his super armor, it’s easier than you think sometimes
Don’t get suck ‘n cucked, though they mostly just do that online 
He has one of the worst disadvantages in the game, abuse that
Combo food
Watch out for up b as it hits through the stage
Crown is very powerful if you can keep it yourself
Poor ledge options
Can't land
Isabelle: 
Punish recovery 
Neutral game excluding the projectiles can be pretty shoddy at times. Try to get close to Isabelle, where your attacks will actually connect.
Not everybody gets this, but Fishing Rod can actually be blocked. Once blocked, Isabelle is immobile and also open to any attack.
Incineroar: 
Bait out double jump and punish
Incineroar has a pretty poor recovery and can get easily gimped.Throw him off stage as much as possible
Grab gets rid of Revenge stacks, that’s nice
If they manage to get Revenge you can either time it out, grab them, or deal 30% damage to them to remove it.
Revenge stacks multiple times. The maximum damage Incineroar can do from this is 72%.
If your character has a counter, use it against Incineroar recovery for an effective and hilarious edge guard
Piranha Plant: 
Block often; attack from behind
Head is not safe during recovery, easy edge guard
All moves are pretty obvious and you can avoid them easily.
His down B is a hitbox so you can hit his head when he is coming for you.
All aerials have a lot of end lag.Bait them out and punish
Joker: 
Forced to recover low in both forms, use to advantage
Is relatively weak without Arsene, try to capitalize on that. Also, whenever he tries to do Rebel’s Guard, try to immediately grab him instead of feeding him the extra meter. If the Joker is too much RG happy, you can bait a rebel guard by charging a smash attack and just waiting. He can keep rebel guard for max 1 second and it has quite a long lag, so just hold smash and release on reaction as soon as RG ends
Don’t be afraid to rush him down when he’s got Arsene, dealing damage to him makes him lose the persona faster
Joker mains have a weird fetish for the dash attack for some reason, which can be easily punished (for example: shield)
Joker is especially susceptible to shield pressure, only oos option to really worry about is bair which isn't even that good
Arséne’s Up B has no hitbox, although it has I-Frames at the start of the move, after this it is very vulnerable, easy spike if timed.
Hero:
Pressure Hero 
His sword is pretty small and he has a lot of end-lag on most moves so punish that
His move set takes time to be executed so punish that as well
Watch out for hatchet man, it can break shields
Banjo:
Shield pressure him
Watch out for side B
Grab combos work well
Terry:
Punish linear recovery(most Terry players can’t snap ledge consistently so get easy two frames)
Sdi kills jab jab power dunk
Be very watchful when using shield as he has many mixups to poke or break your shield. To that end, unless you have incredible oos, jump out of shield and try to punish the setup. 
Try to kill terry as early as possible to not allow GO to be a factor
Terry can buster wolf off of neutral getup so hold shield and do reaction based ledgetrapping
BEWARE THE LEDGE!!! Terry has very strong ledgetrapping and it's how Terry gets most of his absurdly early kills. Unfortunately for you he has incredible options against all normal options so focus on mixing up your timings and don't be afraid to hold ledge
Don’t approach frequently because terry’s projectile is trash 
Byleth:
Missing Info
Min Min:
Missing Info
Steve:
Horrible vertical recovery
Slow
Needs to spend time mining
If mining interrupted then stats don't increase
If minecart is used then go up and b- down to avoid being trapped or jump over.
Recovery can be blocked whilst flying
Can combo you any time so prepare to die
Sephiroth:
Laggy moves, If they are not spaced, punish them
Up B can be interrupted whilst being charged, if you can get to him before he starts, you can punish him
Bad OOS, best he got is Nair, witch if your pressure is spaced, can be avoided and punished
Missing Info / More Info Need
Pyra:
Poor Recovery
Mythra Side B is easily shielded and punished.
Watch out for Neutral B. It lasts longer than expected.
Pyra has poor out of shield options (14 frames)
Pyra is vulnerable after Side B
Pyra is easily punished.
Watch out for pyra dair into up air
Watch out for any mythra aerial
Final Smash has more reach than expected
Watch out for F Smash
Mythra:
Poor Recovery
Mythra Side B is easily shielded and punished.
Watch out for Neutral B. It lasts longer than expected.
Pyra has poor out of shield options (14 frames)
Pyra is vulnerable after Side B
Pyra is easily punished.
Watch out for pyra dair into up air
Watch out for any mythra aerial
Final Smash has more reach than expected
Watch out for F Smash
Mii Brawler: 
Gimp
Some of his moves are easily punishable. To add salt to the wound, sometimes they even whiff frequently.
Mii Swordfighter: 
Avoid tornado, since they can be easily chained to kill moves such as “Hero Spin” and “Discount Ivysaur UP-air”
Is a zoner at heart, so keep your shield up and keep an eye out for gale strike (tornado) and chakram (disc). Try to punish the tornado, which has a lot of end lag after it’s thrown out. 
Watch out for the short range chackram as it has aloooot of hits
Mii Gunner: 
Has a really shitty neutral game if you take away her projectiles. Try to go for a rushdown tactic and don’t let her breath.
"""
chars_lines = chars_text.split("\n")

print("VIDEOS")

videos_learn = {}
videos_beat = {}

print("IZAW")
izaw = "https://www.youtube.com/channel/UC3SM8yOKKwU8PYqwsNP5rGA/"
for video in scrapetube.get_channel("UC3SM8yOKKwU8PYqwsNP5rGA"):
    title = video['title']['runs'][0]["text"]
    if ("art of" in title.lower() or "how to" in title.lower()) and "smash 4" not in title.lower():
        url = video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'][len("/watch?v="):].split("&")[0]
        videos_learn[title] = video['videoId']
        print(end=".")

print("COMBOS")
fl = "https://www.youtube.com/playlist?list=PL_muj8ZcinN6RxpSAEwB54XJ7At-GACrw"
for video in scrapetube.get_playlist("PL_muj8ZcinN6RxpSAEwB54XJ7At-GACrw"):
    url = video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'][len("/watch?v="):].split("&")[0]
    title = video['title']['runs'][0]["text"]
    videos_learn[title] = url
    print(end=".")

print("TRAV")
trav_beat = "https://www.youtube.com/playlist?list=PLlguqIn_UgrLvgqzn_w2yIoQR8Hs2HfMC"
for video in scrapetube.get_playlist("PLlguqIn_UgrLvgqzn_w2yIoQR8Hs2HfMC"):
    url = video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'][len("/watch?v="):].split("&")[0]
    title = video['title']['runs'][0]["text"]
    videos_beat[title] = url
    print(end=".")

print("TWEEK")
tweek_beat = "https://www.youtube.com/playlist?list=PL16ovc51nGk0kiop0uPSdqP8Y17QslH-P"
for video in scrapetube.get_playlist("PL16ovc51nGk0kiop0uPSdqP8Y17QslH-P"):
    url = video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'][len("/watch?v="):].split("&")[0]
    title = video['title']['runs'][0]["text"]
    videos_beat[title] = url
    print(video)
    print(end=".")

print("WEAK")
tips = {}
weakness_lines = weakness_str.split("\n")
char = ""
for line in weakness_lines:
    if line.strip().endswith(":"):
        char = line.lower().strip()[:-1]
        tips[char] = []
    else:
        tips[char].append(line)

print("JSON")
data = {}



i = 0
while i < len(chars_lines):
    num = chars_lines[i]
    full_name = chars_lines[i+1]
    names = full_name.lower().split("/")
    tip = []
    beat = []
    guide = []

    for name in names:
        for n in tips:
            if len(re.findall(r"\b"+re.escape(name)+r"\b", n, re.IGNORECASE)):
                tip.extend(tips[name])
    for name in names:
        for vid in videos_beat:
            if len(re.findall(r"\b"+re.escape(name)+r"\b", vid, re.IGNORECASE)):
                beat.append(videos_beat[vid])
    for name in names:
        for vid in videos_learn:
            if len(re.findall(r"\b"+re.escape(name)+r"\b", vid, re.IGNORECASE)):
                guide.append(videos_learn[vid])

    thumb = names[-1].replace(" ", "_").replace(".", "").replace("-", "_")
    data[full_name] = {
        "name": names[0],
        "thumb_name": thumb,
        "frame": names[0].replace(" ", "_"),
        "tips": tip,
        "guides": guide,
        "beat": beat,
        "discord": "",
        "stages": [],
        "number": num
    }

    i += 2

print("FILE")
import json

with open("data.json", "w") as fp:
    json.dump(data, fp, indent=4)
