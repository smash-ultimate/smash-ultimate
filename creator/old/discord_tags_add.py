import json
from pprint import pprint

html_data="""<tbody>
<tr>
<td><a href="/Mario_(SSBU)" title="Mario (SSBU)"><img alt="MarioHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/0/0d/MarioHeadSSBU.png/20px-MarioHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/0/0d/MarioHeadSSBU.png/30px-MarioHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/0/0d/MarioHeadSSBU.png/40px-MarioHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Mario</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/xARdRQ3eGz">[27]</a>
</td></tr>
<tr>
<td><a href="/Donkey_Kong_(SSBU)" title="Donkey Kong (SSBU)"><img alt="DonkeyKongHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/b/ba/DonkeyKongHeadSSBU.png/20px-DonkeyKongHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/b/ba/DonkeyKongHeadSSBU.png/30px-DonkeyKongHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/b/ba/DonkeyKongHeadSSBU.png/40px-DonkeyKongHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Donkey Kong</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/qMzMf8g">[28]</a>
</td></tr>
<tr>
<td><a href="/Link_(SSBU)" title="Link (SSBU)"><img alt="LinkHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/a/aa/LinkHeadSSBU.png/20px-LinkHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/a/aa/LinkHeadSSBU.png/30px-LinkHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/a/aa/LinkHeadSSBU.png/40px-LinkHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Link</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/Wynbrkd">[29]</a>
</td></tr>
<tr>
<td><a href="/Samus_(SSBU)" title="Samus (SSBU)"><img alt="SamusHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/7/7f/SamusHeadSSBU.png/20px-SamusHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/7/7f/SamusHeadSSBU.png/30px-SamusHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/7/7f/SamusHeadSSBU.png/40px-SamusHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a><a href="/Dark_Samus_(SSBU)" title="Dark Samus (SSBU)"><img alt="DarkSamusHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/9/96/DarkSamusHeadSSBU.png/20px-DarkSamusHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/9/96/DarkSamusHeadSSBU.png/30px-DarkSamusHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/9/96/DarkSamusHeadSSBU.png/40px-DarkSamusHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Samus &amp; Dark Samus</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/b69G8H6">[30]</a>
</td></tr>
<tr>
<td><a href="/Yoshi_(SSBU)" title="Yoshi (SSBU)"><img alt="YoshiHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/0/03/YoshiHeadSSBU.png/20px-YoshiHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/0/03/YoshiHeadSSBU.png/30px-YoshiHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/0/03/YoshiHeadSSBU.png/40px-YoshiHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Yoshi</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/QKanWPU">[31]</a>
</td></tr>
<tr>
<td><a href="/Kirby_(SSBU)" title="Kirby (SSBU)"><img alt="KirbyHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/9/91/KirbyHeadSSBU.png/20px-KirbyHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/9/91/KirbyHeadSSBU.png/30px-KirbyHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/9/91/KirbyHeadSSBU.png/40px-KirbyHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Kirby</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/wDMG7sQ6EE">[32]</a>
</td></tr>
<tr>
<td><a href="/Fox_(SSBU)" title="Fox (SSBU)"><img alt="FoxHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/0/04/FoxHeadSSBU.png/20px-FoxHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/0/04/FoxHeadSSBU.png/30px-FoxHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/0/04/FoxHeadSSBU.png/40px-FoxHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Fox</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/UsXQhYQSKx">[33]</a>
</td></tr>
<tr>
<td><a href="/Pikachu_(SSBU)" title="Pikachu (SSBU)"><img alt="PikachuHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/f/fa/PikachuHeadSSBU.png/20px-PikachuHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/f/fa/PikachuHeadSSBU.png/30px-PikachuHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/f/fa/PikachuHeadSSBU.png/40px-PikachuHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Pikachu</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/UprygGD">[34]</a>
</td></tr>
<tr>
<td><a href="/Luigi_(SSBU)" title="Luigi (SSBU)"><img alt="LuigiHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/c/c6/LuigiHeadSSBU.png/20px-LuigiHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/c/c6/LuigiHeadSSBU.png/30px-LuigiHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/c/c6/LuigiHeadSSBU.png/40px-LuigiHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Luigi</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/sx7JWub">[35]</a>
</td></tr>
<tr>
<td><a href="/Ness_(SSBU)" title="Ness (SSBU)"><img alt="NessHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/0/0f/NessHeadSSBU.png/20px-NessHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/0/0f/NessHeadSSBU.png/30px-NessHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/0/0f/NessHeadSSBU.png/40px-NessHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Ness</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/GXvBCuN">[36]</a>
</td></tr>
<tr>
<td><a href="/Captain_Falcon_(SSBU)" title="Captain Falcon (SSBU)"><img alt="CaptainFalconHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/3/35/CaptainFalconHeadSSBU.png/20px-CaptainFalconHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/3/35/CaptainFalconHeadSSBU.png/30px-CaptainFalconHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/3/35/CaptainFalconHeadSSBU.png/40px-CaptainFalconHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Captain Falcon</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/0XG2K9WbH8VAFd8p">[37]</a>
</td></tr>
<tr>
<td><a href="/Jigglypuff_(SSBU)" title="Jigglypuff (SSBU)"><img alt="JigglypuffHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/9/95/JigglypuffHeadSSBU.png/20px-JigglypuffHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/9/95/JigglypuffHeadSSBU.png/30px-JigglypuffHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/9/95/JigglypuffHeadSSBU.png/40px-JigglypuffHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Jigglypuff</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/0Wj6QkUoh01KUVPn">[38]</a>
</td></tr>
<tr>
<td><a href="/Peach_(SSBU)" title="Peach (SSBU)"><img alt="PeachHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/d/d2/PeachHeadSSBU.png/20px-PeachHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/d/d2/PeachHeadSSBU.png/30px-PeachHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/d/d2/PeachHeadSSBU.png/40px-PeachHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a><a href="/Daisy_(SSBU)" title="Daisy (SSBU)"><img alt="DaisyHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/9/96/DaisyHeadSSBU.png/20px-DaisyHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/9/96/DaisyHeadSSBU.png/30px-DaisyHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/9/96/DaisyHeadSSBU.png/40px-DaisyHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Peach &amp; Daisy</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/gPq3gC4g2f">[39]</a>
</td></tr>
<tr>
<td><a href="/Bowser_(SSBU)" title="Bowser (SSBU)"><img alt="BowserHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/b/b5/BowserHeadSSBU.png/20px-BowserHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/b/b5/BowserHeadSSBU.png/30px-BowserHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/b/b5/BowserHeadSSBU.png/40px-BowserHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Bowser</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/0hwgnNR34wz6cSgX">[40]</a>
</td></tr>
<tr>
<td><a href="/Ice_Climbers_(SSBU)" title="Ice Climbers (SSBU)"><img alt="IceClimbersHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/8/8b/IceClimbersHeadSSBU.png/20px-IceClimbersHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/8/8b/IceClimbersHeadSSBU.png/30px-IceClimbersHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/8/8b/IceClimbersHeadSSBU.png/40px-IceClimbersHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Ice Climbers</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/6ha6HVF">[41]</a>
</td></tr>
<tr>
<td><a href="/Sheik_(SSBU)" title="Sheik (SSBU)"><img alt="SheikHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/3/37/SheikHeadSSBU.png/20px-SheikHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/3/37/SheikHeadSSBU.png/30px-SheikHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/3/37/SheikHeadSSBU.png/40px-SheikHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Sheik</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/MSbMHrY">[42]</a>
</td></tr>
<tr>
<td><a href="/Zelda_(SSBU)" title="Zelda (SSBU)"><img alt="ZeldaHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/c/c1/ZeldaHeadSSBU.png/20px-ZeldaHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/c/c1/ZeldaHeadSSBU.png/30px-ZeldaHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/c/c1/ZeldaHeadSSBU.png/40px-ZeldaHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Zelda</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/FTw5cVD">[43]</a>
</td></tr>
<tr>
<td><a href="/Dr._Mario_(SSBU)" title="Dr. Mario (SSBU)"><img alt="DrMarioHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/7/78/DrMarioHeadSSBU.png/20px-DrMarioHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/7/78/DrMarioHeadSSBU.png/30px-DrMarioHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/7/78/DrMarioHeadSSBU.png/40px-DrMarioHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Dr. Mario</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/pNk9UzP">[44]</a>
</td></tr>
<tr>
<td><a href="/Pichu_(SSBU)" title="Pichu (SSBU)"><img alt="PichuHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/d/d6/PichuHeadSSBU.png/20px-PichuHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/d/d6/PichuHeadSSBU.png/30px-PichuHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/d/d6/PichuHeadSSBU.png/40px-PichuHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Pichu</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/RgcFwQB">[45]</a>
</td></tr>
<tr>
<td><a href="/Falco_(SSBU)" title="Falco (SSBU)"><img alt="FalcoHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/2/2f/FalcoHeadSSBU.png/20px-FalcoHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/2/2f/FalcoHeadSSBU.png/30px-FalcoHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/2/2f/FalcoHeadSSBU.png/40px-FalcoHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Falco</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/HptPZcT">[46]</a>
</td></tr>
<tr>
<td><a href="/Marth_(SSBU)" title="Marth (SSBU)"><img alt="MarthHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/b/bd/MarthHeadSSBU.png/20px-MarthHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/b/bd/MarthHeadSSBU.png/30px-MarthHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/b/bd/MarthHeadSSBU.png/40px-MarthHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a><a href="/Lucina_(SSBU)" title="Lucina (SSBU)"><img alt="LucinaHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/0/04/LucinaHeadSSBU.png/20px-LucinaHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/0/04/LucinaHeadSSBU.png/30px-LucinaHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/0/04/LucinaHeadSSBU.png/40px-LucinaHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Marth &amp; Lucina</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/0bQ68KVbo2Pt5ISy">[47]</a>
</td></tr>
<tr>
<td><a href="/Young_Link_(SSBU)" title="Young Link (SSBU)"><img alt="YoungLinkHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/c/cd/YoungLinkHeadSSBU.png/20px-YoungLinkHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/c/cd/YoungLinkHeadSSBU.png/30px-YoungLinkHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/c/cd/YoungLinkHeadSSBU.png/40px-YoungLinkHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Young Link</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/zxC8Vzr">[48]</a>
</td></tr>
<tr>
<td><a href="/Ganondorf_(SSBU)" title="Ganondorf (SSBU)"><img alt="GanondorfHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/7/78/GanondorfHeadSSBU.png/20px-GanondorfHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/7/78/GanondorfHeadSSBU.png/30px-GanondorfHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/7/78/GanondorfHeadSSBU.png/40px-GanondorfHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Ganondorf</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/qhtPMHY">[49]</a>
</td></tr>
<tr>
<td><a href="/Mewtwo_(SSBU)" title="Mewtwo (SSBU)"><img alt="MewtwoHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/9/96/MewtwoHeadSSBU.png/20px-MewtwoHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/9/96/MewtwoHeadSSBU.png/30px-MewtwoHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/9/96/MewtwoHeadSSBU.png/40px-MewtwoHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Mewtwo</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/AUVSYqb">[50]</a>
</td></tr>
<tr>
<td><a href="/Roy_(SSBU)" title="Roy (SSBU)"><img alt="RoyHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/e/ed/RoyHeadSSBU.png/20px-RoyHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/e/ed/RoyHeadSSBU.png/30px-RoyHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/e/ed/RoyHeadSSBU.png/40px-RoyHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a><a href="/Chrom_(SSBU)" title="Chrom (SSBU)"><img alt="ChromHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/2/25/ChromHeadSSBU.png/20px-ChromHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/2/25/ChromHeadSSBU.png/30px-ChromHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/2/25/ChromHeadSSBU.png/40px-ChromHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Roy &amp; Chrom</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/dgJrPSK">[51]</a>
</td></tr>
<tr>
<td><a href="/Mr._Game_%26_Watch_(SSBU)" title="Mr. Game &amp; Watch (SSBU)"><img alt="MrGame&amp;WatchHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/6/6b/MrGame%26WatchHeadSSBU.png/20px-MrGame%26WatchHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/6/6b/MrGame%26WatchHeadSSBU.png/30px-MrGame%26WatchHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/6/6b/MrGame%26WatchHeadSSBU.png/40px-MrGame%26WatchHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Mr. Game &amp; Watch</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/fzWuqZ8">[52]</a>
</td></tr>
<tr>
<td><a href="/Meta_Knight_(SSBU)" title="Meta Knight (SSBU)"><img alt="MetaKnightHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/d/de/MetaKnightHeadSSBU.png/20px-MetaKnightHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/d/de/MetaKnightHeadSSBU.png/30px-MetaKnightHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/d/de/MetaKnightHeadSSBU.png/40px-MetaKnightHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Meta Knight</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/raEcZ8f">[53]</a>
</td></tr>
<tr>
<td><a href="/Pit_(SSBU)" title="Pit (SSBU)"><img alt="PitHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/a/aa/PitHeadSSBU.png/20px-PitHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/a/aa/PitHeadSSBU.png/30px-PitHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/a/aa/PitHeadSSBU.png/40px-PitHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a><a href="/Dark_Pit_(SSBU)" title="Dark Pit (SSBU)"><img alt="DarkPitHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/e/ed/DarkPitHeadSSBU.png/20px-DarkPitHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/e/ed/DarkPitHeadSSBU.png/30px-DarkPitHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/e/ed/DarkPitHeadSSBU.png/40px-DarkPitHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Pit &amp; Dark Pit</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/gJHHHR4urr">[54]</a>
</td></tr>
<tr>
<td><a href="/Zero_Suit_Samus_(SSBU)" title="Zero Suit Samus (SSBU)"><img alt="ZeroSuitSamusHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/7/71/ZeroSuitSamusHeadSSBU.png/20px-ZeroSuitSamusHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/7/71/ZeroSuitSamusHeadSSBU.png/30px-ZeroSuitSamusHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/7/71/ZeroSuitSamusHeadSSBU.png/40px-ZeroSuitSamusHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Zero Suit Samus</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/up3dbCf">[55]</a>
</td></tr>
<tr>
<td><a href="/Wario_(SSBU)" title="Wario (SSBU)"><img alt="WarioHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/0/05/WarioHeadSSBU.png/20px-WarioHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/0/05/WarioHeadSSBU.png/30px-WarioHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/0/05/WarioHeadSSBU.png/40px-WarioHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Wario</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/HRQWSZK">[56]</a>
</td></tr>
<tr>
<td><a href="/Snake_(SSBU)" title="Snake (SSBU)"><img alt="SnakeHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/9/9a/SnakeHeadSSBU.png/20px-SnakeHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/9/9a/SnakeHeadSSBU.png/30px-SnakeHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/9/9a/SnakeHeadSSBU.png/40px-SnakeHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Snake</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/3BXATDr">[57]</a>
</td></tr>
<tr>
<td><a href="/Ike_(SSBU)" title="Ike (SSBU)"><img alt="IkeHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/b/b2/IkeHeadSSBU.png/20px-IkeHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/b/b2/IkeHeadSSBU.png/30px-IkeHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/b/b2/IkeHeadSSBU.png/40px-IkeHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Ike</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/ggHCGgM">[58]</a>
</td></tr>
<tr>
<td><a href="/Pok%C3%A9mon_Trainer_(SSBU)" title="Pokémon Trainer (SSBU)"><img alt="PokémonTrainerHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/0/09/Pok%C3%A9monTrainerHeadSSBU.png/20px-Pok%C3%A9monTrainerHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/0/09/Pok%C3%A9monTrainerHeadSSBU.png/30px-Pok%C3%A9monTrainerHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/0/09/Pok%C3%A9monTrainerHeadSSBU.png/40px-Pok%C3%A9monTrainerHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Pokémon Trainer</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/tzNV4hF">[59]</a>
</td></tr>
<tr>
<td><a href="/Diddy_Kong_(SSBU)" title="Diddy Kong (SSBU)"><img alt="DiddyKongHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/3/36/DiddyKongHeadSSBU.png/20px-DiddyKongHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/3/36/DiddyKongHeadSSBU.png/30px-DiddyKongHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/3/36/DiddyKongHeadSSBU.png/40px-DiddyKongHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Diddy Kong</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/9trzxan">[60]</a>
</td></tr>
<tr>
<td><a href="/Lucas_(SSBU)" title="Lucas (SSBU)"><img alt="LucasHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/f/ff/LucasHeadSSBU.png/20px-LucasHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/f/ff/LucasHeadSSBU.png/30px-LucasHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/f/ff/LucasHeadSSBU.png/40px-LucasHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Lucas</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/Y5fjHed">[61]</a>
</td></tr>
<tr>
<td><a href="/Sonic_(SSBU)" title="Sonic (SSBU)"><img alt="SonicHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/7/76/SonicHeadSSBU.png/20px-SonicHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/7/76/SonicHeadSSBU.png/30px-SonicHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/7/76/SonicHeadSSBU.png/40px-SonicHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Sonic</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/z24Autr">[62]</a>
</td></tr>
<tr>
<td><a href="/King_Dedede_(SSBU)" title="King Dedede (SSBU)"><img alt="KingDededeHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/b/bb/KingDededeHeadSSBU.png/20px-KingDededeHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/b/bb/KingDededeHeadSSBU.png/30px-KingDededeHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/b/bb/KingDededeHeadSSBU.png/40px-KingDededeHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> King Dedede</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/fccCz2G">[63]</a>
</td></tr>
<tr>
<td><a href="/Olimar_(SSBU)" title="Olimar (SSBU)"><img alt="OlimarHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/9/91/OlimarHeadSSBU.png/20px-OlimarHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/9/91/OlimarHeadSSBU.png/30px-OlimarHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/9/91/OlimarHeadSSBU.png/40px-OlimarHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Olimar</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/GDpDJzK">[64]</a>
</td></tr>
<tr>
<td><a href="/Lucario_(SSBU)" title="Lucario (SSBU)"><img alt="LucarioHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/c/cd/LucarioHeadSSBU.png/20px-LucarioHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/c/cd/LucarioHeadSSBU.png/30px-LucarioHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/c/cd/LucarioHeadSSBU.png/40px-LucarioHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Lucario</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/ZvRt7CD">[65]</a>
</td></tr>
<tr>
<td><a href="/ROB_(SSBU)" title="ROB (SSBU)"><img alt="ROBHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/b/b3/ROBHeadSSBU.png/20px-ROBHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/b/b3/ROBHeadSSBU.png/30px-ROBHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/b/b3/ROBHeadSSBU.png/40px-ROBHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> R.O.B.</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/FkSQVBp">[66]</a>
</td></tr>
<tr>
<td><a href="/Toon_Link_(SSBU)" title="Toon Link (SSBU)"><img alt="ToonLinkHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/e/e6/ToonLinkHeadSSBU.png/20px-ToonLinkHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/e/e6/ToonLinkHeadSSBU.png/30px-ToonLinkHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/e/e6/ToonLinkHeadSSBU.png/40px-ToonLinkHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Toon Link</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/uvGBcTA">[67]</a>
</td></tr>
<tr>
<td><a href="/Wolf_(SSBU)" title="Wolf (SSBU)"><img alt="WolfHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/e/e8/WolfHeadSSBU.png/20px-WolfHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/e/e8/WolfHeadSSBU.png/30px-WolfHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/e/e8/WolfHeadSSBU.png/40px-WolfHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Wolf</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/mmE4NgS">[68]</a>
</td></tr>
<tr>
<td><a href="/Villager_(SSBU)" title="Villager (SSBU)"><img alt="VillagerHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/b/b9/VillagerHeadSSBU.png/20px-VillagerHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/b/b9/VillagerHeadSSBU.png/30px-VillagerHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/b/b9/VillagerHeadSSBU.png/40px-VillagerHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Villager</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/eA56cyJ">[69]</a>
</td></tr>
<tr>
<td><a href="/Mega_Man_(SSBU)" title="Mega Man (SSBU)"><img alt="MegaManHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/5/55/MegaManHeadSSBU.png/20px-MegaManHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/5/55/MegaManHeadSSBU.png/30px-MegaManHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/5/55/MegaManHeadSSBU.png/40px-MegaManHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Mega Man</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/fBfHuKS">[70]</a>
</td></tr>
<tr>
<td><a href="/Wii_Fit_Trainer_(SSBU)" title="Wii Fit Trainer (SSBU)"><img alt="WiiFitTrainerHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/8/87/WiiFitTrainerHeadSSBU.png/20px-WiiFitTrainerHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/8/87/WiiFitTrainerHeadSSBU.png/30px-WiiFitTrainerHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/8/87/WiiFitTrainerHeadSSBU.png/40px-WiiFitTrainerHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Wii Fit Trainer</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/CQ4NQ6r">[71]</a>
</td></tr>
<tr>
<td><a href="/Rosalina_(SSBU)" title="Rosalina (SSBU)"><img alt="RosalinaHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/e/e8/RosalinaHeadSSBU.png/20px-RosalinaHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/e/e8/RosalinaHeadSSBU.png/30px-RosalinaHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/e/e8/RosalinaHeadSSBU.png/40px-RosalinaHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Rosalina &amp; Luma</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/a5asHUc">[72]</a>
</td></tr>
<tr>
<td><a href="/Little_Mac_(SSBU)" title="Little Mac (SSBU)"><img alt="LittleMacHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/1/10/LittleMacHeadSSBU.png/20px-LittleMacHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/1/10/LittleMacHeadSSBU.png/30px-LittleMacHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/1/10/LittleMacHeadSSBU.png/40px-LittleMacHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Little Mac</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/ZjJUVNn">[73]</a>
</td></tr>
<tr>
<td><a href="/Greninja_(SSBU)" title="Greninja (SSBU)"><img alt="GreninjaHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/6/65/GreninjaHeadSSBU.png/20px-GreninjaHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/6/65/GreninjaHeadSSBU.png/30px-GreninjaHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/6/65/GreninjaHeadSSBU.png/40px-GreninjaHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Greninja</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/V9hnnSp">[74]</a>
</td></tr>
<tr>
<td><a href="/Mii_Brawler_(SSBU)" title="Mii Brawler (SSBU)"><img alt="MiiBrawlerHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/d/d8/MiiBrawlerHeadSSBU.png/20px-MiiBrawlerHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/d/d8/MiiBrawlerHeadSSBU.png/30px-MiiBrawlerHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/d/d8/MiiBrawlerHeadSSBU.png/40px-MiiBrawlerHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Mii Brawler</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/GBkjrd3">[75]</a>
</td></tr>
<tr>
<td><a href="/Mii_Swordfighter_(SSBU)" title="Mii Swordfighter (SSBU)"><img alt="MiiSwordfighterHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/e/ef/MiiSwordfighterHeadSSBU.png/20px-MiiSwordfighterHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/e/ef/MiiSwordfighterHeadSSBU.png/30px-MiiSwordfighterHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/e/ef/MiiSwordfighterHeadSSBU.png/40px-MiiSwordfighterHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Mii Swordfighter</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/muVX4h5">[76]</a>
</td></tr>
<tr>
<td><a href="/Mii_Gunner_(SSBU)" title="Mii Gunner (SSBU)"><img alt="MiiGunnerHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/3/3d/MiiGunnerHeadSSBU.png/20px-MiiGunnerHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/3/3d/MiiGunnerHeadSSBU.png/30px-MiiGunnerHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/3/3d/MiiGunnerHeadSSBU.png/40px-MiiGunnerHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Mii Gunner</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/7CdEzy9">[77]</a>
</td></tr>
<tr>
<td><a href="/Palutena_(SSBU)" title="Palutena (SSBU)"><img alt="PalutenaHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/a/a9/PalutenaHeadSSBU.png/20px-PalutenaHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/a/a9/PalutenaHeadSSBU.png/30px-PalutenaHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/a/a9/PalutenaHeadSSBU.png/40px-PalutenaHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Palutena</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/xRYxrgEAnf">[78]</a>
</td></tr>
<tr>
<td><a href="/Pac-Man_(SSBU)" title="Pac-Man (SSBU)"><img alt="Pac-ManHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/4/45/Pac-ManHeadSSBU.png/20px-Pac-ManHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/4/45/Pac-ManHeadSSBU.png/30px-Pac-ManHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/4/45/Pac-ManHeadSSBU.png/40px-Pac-ManHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Pac-Man</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/Khu27zPeaW">[79]</a>
</td></tr>
<tr>
<td><a href="/Robin_(SSBU)" title="Robin (SSBU)"><img alt="RobinHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/2/25/RobinHeadSSBU.png/20px-RobinHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/2/25/RobinHeadSSBU.png/30px-RobinHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/2/25/RobinHeadSSBU.png/40px-RobinHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Robin</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/qp2FYcm">[80]</a>
</td></tr>
<tr>
<td><a href="/Shulk_(SSBU)" title="Shulk (SSBU)"><img alt="ShulkHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/c/c1/ShulkHeadSSBU.png/20px-ShulkHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/c/c1/ShulkHeadSSBU.png/30px-ShulkHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/c/c1/ShulkHeadSSBU.png/40px-ShulkHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Shulk</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/NpXtA3f">[81]</a>
</td></tr>
<tr>
<td><a href="/Bowser_Jr._(SSBU)" title="Bowser Jr. (SSBU)"><img alt="BowserJrHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/0/07/BowserJrHeadSSBU.png/20px-BowserJrHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/0/07/BowserJrHeadSSBU.png/30px-BowserJrHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/0/07/BowserJrHeadSSBU.png/40px-BowserJrHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Bowser Jr.</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/98a5WGM">[82]</a>
</td></tr>
<tr>
<td><a href="/Duck_Hunt_(SSBU)" title="Duck Hunt (SSBU)"><img alt="DuckHuntHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/a/a1/DuckHuntHeadSSBU.png/20px-DuckHuntHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/a/a1/DuckHuntHeadSSBU.png/30px-DuckHuntHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/a/a1/DuckHuntHeadSSBU.png/40px-DuckHuntHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Duck Hunt</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/0lSgxaH91EeSdy6V">[83]</a>
</td></tr>
<tr>
<td><a href="/Ryu_(SSBU)" title="Ryu (SSBU)"><img alt="RyuHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/f/fb/RyuHeadSSBU.png/20px-RyuHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/f/fb/RyuHeadSSBU.png/30px-RyuHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/f/fb/RyuHeadSSBU.png/40px-RyuHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a><a href="/Ken_(SSBU)" title="Ken (SSBU)"><img alt="KenHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/7/72/KenHeadSSBU.png/20px-KenHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/7/72/KenHeadSSBU.png/30px-KenHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/7/72/KenHeadSSBU.png/40px-KenHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Ryu &amp; Ken</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/9zy9qqG">[84]</a>
</td></tr>
<tr>
<td><a href="/Cloud_(SSBU)" title="Cloud (SSBU)"><img alt="CloudHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/3/3b/CloudHeadSSBU.png/20px-CloudHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/3/3b/CloudHeadSSBU.png/30px-CloudHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/3/3b/CloudHeadSSBU.png/40px-CloudHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Cloud</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/fk7NWD5">[85]</a>
</td></tr>
<tr>
<td><a href="/Corrin_(SSBU)" title="Corrin (SSBU)"><img alt="CorrinHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/c/cf/CorrinHeadSSBU.png/20px-CorrinHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/c/cf/CorrinHeadSSBU.png/30px-CorrinHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/c/cf/CorrinHeadSSBU.png/40px-CorrinHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Corrin</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/FPgq8kb">[86]</a>
</td></tr>
<tr>
<td><a href="/Bayonetta_(SSBU)" title="Bayonetta (SSBU)"><img alt="BayonettaHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/6/6c/BayonettaHeadSSBU.png/20px-BayonettaHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/6/6c/BayonettaHeadSSBU.png/30px-BayonettaHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/6/6c/BayonettaHeadSSBU.png/40px-BayonettaHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Bayonetta</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/0hnEtng5sDAInh0c">[87]</a>
</td></tr>
<tr>
<td><a href="/Inkling_(SSBU)" title="Inkling (SSBU)"><img alt="InklingHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/f/f1/InklingHeadSSBU.png/20px-InklingHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/f/f1/InklingHeadSSBU.png/30px-InklingHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/f/f1/InklingHeadSSBU.png/40px-InklingHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Inkling</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/eJskccFuuU">[88]</a>
</td></tr>
<tr>
<td><a href="/Ridley_(SSBU)" title="Ridley (SSBU)"><img alt="RidleyHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/5/5b/RidleyHeadSSBU.png/20px-RidleyHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/5/5b/RidleyHeadSSBU.png/30px-RidleyHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/5/5b/RidleyHeadSSBU.png/40px-RidleyHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Ridley</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/3UJwxAh">[89]</a>
</td></tr>
<tr>
<td><a href="/Simon_(SSBU)" title="Simon (SSBU)"><img alt="SimonHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/d/df/SimonHeadSSBU.png/20px-SimonHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/d/df/SimonHeadSSBU.png/30px-SimonHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/d/df/SimonHeadSSBU.png/40px-SimonHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a><a href="/Richter_(SSBU)" title="Richter (SSBU)"><img alt="RichterHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/0/07/RichterHeadSSBU.png/20px-RichterHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/0/07/RichterHeadSSBU.png/30px-RichterHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/0/07/RichterHeadSSBU.png/40px-RichterHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Simon &amp; Richter</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/yHRz4fG">[90]</a>
</td></tr>
<tr>
<td><a href="/King_K._Rool_(SSBU)" title="King K. Rool (SSBU)"><img alt="KingKRoolHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/d/de/KingKRoolHeadSSBU.png/20px-KingKRoolHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/d/de/KingKRoolHeadSSBU.png/30px-KingKRoolHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/d/de/KingKRoolHeadSSBU.png/40px-KingKRoolHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> King K. Rool</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/Xqrchru">[91]</a>
</td></tr>
<tr>
<td><a href="/Isabelle_(SSBU)" title="Isabelle (SSBU)"><img alt="IsabelleHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/2/2f/IsabelleHeadSSBU.png/20px-IsabelleHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/2/2f/IsabelleHeadSSBU.png/30px-IsabelleHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/2/2f/IsabelleHeadSSBU.png/40px-IsabelleHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Isabelle</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/buV2XbFBWY">[92]</a>
</td></tr>
<tr>
<td><a href="/Incineroar_(SSBU)" title="Incineroar (SSBU)"><img alt="IncineroarHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/5/50/IncineroarHeadSSBU.png/20px-IncineroarHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/5/50/IncineroarHeadSSBU.png/30px-IncineroarHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/5/50/IncineroarHeadSSBU.png/40px-IncineroarHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Incineroar</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/3DDQ9tQ">[93]</a>
</td></tr>
<tr>
<td><a href="/Piranha_Plant_(SSBU)" title="Piranha Plant (SSBU)"><img alt="PiranhaPlantHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/3/38/PiranhaPlantHeadSSBU.png/20px-PiranhaPlantHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/3/38/PiranhaPlantHeadSSBU.png/30px-PiranhaPlantHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/3/38/PiranhaPlantHeadSSBU.png/40px-PiranhaPlantHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Piranha Plant</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/HfsFQ8j">[94]</a>
</td></tr>
<tr>
<td><a href="/Joker_(SSBU)" title="Joker (SSBU)"><img alt="JokerHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/2/25/JokerHeadSSBU.png/20px-JokerHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/2/25/JokerHeadSSBU.png/30px-JokerHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/2/25/JokerHeadSSBU.png/40px-JokerHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Joker</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/Pvwkbt8">[95]</a>
</td></tr>
<tr>
<td><a href="/Hero_(SSBU)" title="Hero (SSBU)"><img alt="HeroHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/3/3d/HeroHeadSSBU.png/20px-HeroHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/3/3d/HeroHeadSSBU.png/30px-HeroHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/3/3d/HeroHeadSSBU.png/40px-HeroHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Hero</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/Sf6EZuQ">[96]</a>
</td></tr>
<tr>
<td><a href="/Banjo_%26_Kazooie_(SSBU)" title="Banjo &amp; Kazooie (SSBU)"><img alt="Banjo&amp;KazooieHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/6/60/Banjo%26KazooieHeadSSBU.png/20px-Banjo%26KazooieHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/6/60/Banjo%26KazooieHeadSSBU.png/30px-Banjo%26KazooieHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/6/60/Banjo%26KazooieHeadSSBU.png/40px-Banjo%26KazooieHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Banjo &amp; Kazooie</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/gBhBsfm">[97]</a>
</td></tr>
<tr>
<td><a href="/Terry_(SSBU)" title="Terry (SSBU)"><img alt="TerryHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/f/f9/TerryHeadSSBU.png/20px-TerryHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/f/f9/TerryHeadSSBU.png/30px-TerryHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/f/f9/TerryHeadSSBU.png/40px-TerryHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Terry</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/3BvsNSwXu2">[98]</a>
</td></tr>
<tr>
<td><a href="/Byleth_(SSBU)" title="Byleth (SSBU)"><img alt="BylethHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/a/a2/BylethHeadSSBU.png/20px-BylethHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/a/a2/BylethHeadSSBU.png/30px-BylethHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/a/a2/BylethHeadSSBU.png/40px-BylethHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Byleth</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/byleth">[99]</a>
</td></tr>
<tr>
<td><a href="/Min_Min_(SSBU)" title="Min Min (SSBU)"><img alt="MinMinHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/d/de/MinMinHeadSSBU.png/20px-MinMinHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/d/de/MinMinHeadSSBU.png/30px-MinMinHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/d/de/MinMinHeadSSBU.png/40px-MinMinHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Min Min</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/P9QPeFr">[100]</a>
</td></tr>
<tr>
<td><a href="/Steve_(SSBU)" title="Steve (SSBU)"><img alt="Steve's stock icon." src="https://ssb.wiki.gallery/images/thumb/1/11/SteveHeadSSBU.png/20px-SteveHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/1/11/SteveHeadSSBU.png/30px-SteveHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/1/11/SteveHeadSSBU.png/40px-SteveHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Steve</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/BRSDm9U">[101]</a>
</td></tr>
<tr>
<td><a href="/Sephiroth_(SSBU)" title="Sephiroth (SSBU)"><img alt="Sephiroth's stock icon." src="https://ssb.wiki.gallery/images/thumb/5/5e/SephirothHeadSSBU.png/20px-SephirothHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/5/5e/SephirothHeadSSBU.png/30px-SephirothHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/5/5e/SephirothHeadSSBU.png/40px-SephirothHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Sephiroth</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/qqcCyUMBZE">[102]</a>
</td></tr>
<tr>
<td><a href="/Pyra_(SSBU)" title="Pyra (SSBU)"><img alt="PyraHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/7/79/PyraHeadSSBU.png/20px-PyraHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/7/79/PyraHeadSSBU.png/30px-PyraHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/7/79/PyraHeadSSBU.png/40px-PyraHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a><a href="/Mythra_(SSBU)" title="Mythra (SSBU)"><img alt="MythraHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/3/32/MythraHeadSSBU.png/20px-MythraHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/3/32/MythraHeadSSBU.png/30px-MythraHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/3/32/MythraHeadSSBU.png/40px-MythraHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Pyra &amp; Mythra</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/kX2usVD62C">[103]</a> <a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/wrrBRE7crE">[104]</a>
</td></tr>
<tr>
<td><a href="/Kazuya_(SSBU)" title="Kazuya (SSBU)"><img alt="KazuyaHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/6/67/KazuyaHeadSSBU.png/20px-KazuyaHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/6/67/KazuyaHeadSSBU.png/30px-KazuyaHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/6/67/KazuyaHeadSSBU.png/40px-KazuyaHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Kazuya</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/gvemyvhX6u">[105]</a>
</td></tr>
<tr>
<td><a href="/Sora_(SSBU)" title="Sora (SSBU)"><img alt="SoraHeadSSBU.png" src="https://ssb.wiki.gallery/images/thumb/0/0e/SoraHeadSSBU.png/20px-SoraHeadSSBU.png" decoding="async" width="20" height="20" srcset="https://ssb.wiki.gallery/images/thumb/0/0e/SoraHeadSSBU.png/30px-SoraHeadSSBU.png 1.5x, https://ssb.wiki.gallery/images/thumb/0/0e/SoraHeadSSBU.png/40px-SoraHeadSSBU.png 2x" data-file-width="64" data-file-height="64"></a> Sora</td>
<td><a target="_blank" rel="nofollow" class="external autonumber" href="https://discord.com/invite/Xkh9UTV9y4">[106]</a>
</td></tr></tbody>"""

from html.parser import HTMLParser

name = ""
i = 1
data = {}

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global name, i
        if tag == "a":
            if len(attrs) == 2 and attrs[1][0] == "title":
                name = attrs[1][1]
            if len(attrs) == 4 and attrs[3][0] == "href" and attrs[3][1].startswith("https://discord.com/invite/"):
                #data[name] = attrs[3][1][len("https://discord.com/invite/"):]
                print(i, attrs[3][1][len("https://discord.com/invite/"):], name)
                data[i] = attrs[3][1][len("https://discord.com/invite/"):]
                i += 1
                if name == "Pokémon Trainer (SSBU)":
                    i += 2
parser = MyHTMLParser()
parser.feed(html_data)

with open("data.json") as fp:
    file_data = json.load(fp)

for f in file_data:
    n = file_data[f]["number"]
    if n.endswith("e"):
        n = n[:-1]
    n = int(n)
    file_data[f]["discord"] = data[n]

with open("data.json", "w") as fp:
    json.dump(file_data, fp, indent=4)


#pprint(data)
#
