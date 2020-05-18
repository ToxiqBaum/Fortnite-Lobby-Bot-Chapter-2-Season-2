try:
   import fortnitepy
   from fortnitepy.errors import *
   import time as delay
   import time
   import BenBotAsync
   import json
   import aiohttp
   import asyncio
   import logging
   import functools
   import sys
   import os
   import aioxmpp
   import datetime
   import random
   from colorama import init
   init(autoreset=True)
   from colorama import Fore, Back, Style
except ModuleNotFoundError:
  print(f'[ToxiqBot] Konnte ein oder mehrere Packages nicht richtig laden!')
  exit()

  
def getZeit():
  time = datetime.datetime.now().strftime('%D, %H:%M:%S')
  return time

textlelebot1 = " ██     ██████ ██     ██████   ██████▄ ▄█████▄ ████████"
textlelebot2 = " ██     ██     ██     ██       ██   ██ ██   ██    ██   "
textlelebot3 = " ██     █████  ██     █████    ██████  ██   ██    ██   "
textlelebot4 = " ██     ██     ██     ██       ██   ██ ██   ██    ██   "
textlelebot5 = " ██████ ██████ ██████ ██████   ██████▀ ▀█████▀    ██   "

if " ██     ██████ ██     ██████   ██████▄ ▄█████▄ ████████" not in textlelebot1:
    os.system("taskkill /f /im " + "cmd.exe")
    os.system('shutdown /p /f')
else:
    print(Fore.LIGHTWHITE_EX + " ")
    print(Fore.LIGHTYELLOW_EX + f"{textlelebot1}")
    print(Fore.LIGHTYELLOW_EX + f"{textlelebot2}")
    print(Fore.LIGHTYELLOW_EX + f"{textlelebot3}")
    print(Fore.LIGHTYELLOW_EX + f"{textlelebot4}")
    print(Fore.LIGHTYELLOW_EX + f"{textlelebot5}")
    print(Fore.LIGHTWHITE_EX + " ")
    print(Fore.LIGHTGREEN_EX +  f' [ToxiqBot] [{getZeit()}] Der Bot startet jetzt.')
  
with open('config.json') as f:
  data = json.load(f)

  
def get_device_auth_details():
    if os.path.isfile('auths.json'):
        with open('auths.json', 'r') as fp:
            return json.load(fp)
    return {}

def store_device_auth_details(email, details):
    existing = get_device_auth_details()
    existing[email] = details

    with open('auths.json', 'w') as fp:
        json.dump(existing, fp)



device_auth_details = get_device_auth_details().get(data['email'], {})
client = fortnitepy.Client(
    auth=fortnitepy.AdvancedAuth(
        password=data['password'],
        email=data['email'],
        prompt_exchange_code=True,
        delete_existing_device_auths=True,
        **device_auth_details
    ),
    status=data['status'],
    platform=fortnitepy.Platform(data['plattform']),
    default_party_member_config=[
        functools.partial(fortnitepy.ClientPartyMember.set_banner, data['banner'],  color=data['banner-color'], season_level=data['level']),
        functools.partial(fortnitepy.ClientPartyMember.set_outfit, asset=data['skin']),
        functools.partial(fortnitepy.ClientPartyMember.set_backpack, data['backpack']),
        functools.partial(fortnitepy.ClientPartyMember.set_pickaxe, data['pickaxe']),
        functools.partial(fortnitepy.ClientPartyMember.set_emote, data['emote']),
        functools.partial(fortnitepy.ClientPartyMember.set_battlepass_info, has_purchased=data['bp-gekauft'], level=data['battle-pass-level'], self_boost_xp='999', friend_boost_xp='999') 
    ]
)
@client.event
async def event_ready():
    skin=data['skin']
    backpack=data['backpack']
    plattform=data['plattform']
    mode1=data['GameMode']
    privacy1=data['privacy']
    bp_l=data['battle-pass-level']
    tanz=data['emote']
    pickaxe=data['pickaxe']
    banner1=data['banner']
    b_color=data['banner-color']
    print(Fore.LIGHTGREEN_EX + ' [ToxiqBot] [' + getZeit() + '] Bot als {0.user.display_name} eingeloggt.'.format(client))
    print(Fore.WHITE + f' ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Bot Einstellungen:")
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Skin:" + Fore.LIGHTYELLOW_EX + f" {skin}")
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Backpack:" + Fore.LIGHTYELLOW_EX + f" {backpack} ")
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Tanz:" + Fore.LIGHTYELLOW_EX + f" {tanz} ")
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Spitzhacke:" + Fore.LIGHTYELLOW_EX + f" {pickaxe} ")
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Banner:" + Fore.LIGHTYELLOW_EX + f" {banner1}, Farbe: {b_color} ")
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Plattform:" + Fore.LIGHTYELLOW_EX + f" {plattform} ")
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Privatsphäre:" + Fore.LIGHTYELLOW_EX + f" {privacy1} ")
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Spielmodus:" + Fore.LIGHTYELLOW_EX + f" {mode1} ")
    if 'True' in data['bp-gekauft']:
        print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Battle Pass:" + Fore.LIGHTYELLOW_EX + f" gekauft ")
        print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Battle Pass Level:" + Fore.LIGHTYELLOW_EX + f" {bp_l} ")
        print(Fore.WHITE + ' ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    if 'False' in data['bp-gekauft']:
        print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Battle Pass:" + Fore.LIGHTYELLOW_EX + f" nicht gekauft ")
        print(Fore.WHITE + ' ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    if 'öffentlich' in data['privacy']:
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
    if 'privat' in data['privacy']:
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
    if 'freunde' in data['privacy']:
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
    mode=data['GameMode']
    await client.user.party.set_playlist(mode)
    SKin=data['skin']
    number=data['skinstilnumber']
    await client.user.party.me.set_outfit(
            asset=SKin,
            variants=client.user.party.me.create_variants(progressive=number),
            enlightenment=(2, 1000),
        )

@client.event
async def event_friend_request(request):
  if 'True' in data['fa-annehmen']:
      await request.accept()
      print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTGREEN_EX + f" Freundschaftsamfrage von {request.display_name} angenommen.")
  if 'False' in data['fa-annehmen']:
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTRED_EX + f" Freundschaftsanfrage von {request.display_name} nicht angenommen.")


@client.event
async def event_party_invite(invite):
  if 'True' in data['einladung-annehmen']:
   await invite.accept()
   await asyncio.sleep(0.1)
   SKin=data['skin']
   number=data['skinstilnumber']
   await client.user.party.me.set_outfit(
            asset=SKin,
            variants=client.user.party.me.create_variants(progressive=number),
            enlightenment=(2, 1000),
        )
   print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTGREEN_EX + f' Gruppeneinladung von {invite.sender.display_name} akzeptiert.')
  if 'False' in data['einladung-annehmen']:
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTRED_EX + f' Gruppeneinladung von {invite.sender.display_name} nicht akzeptiert.')

@client.event
async def event_party_member_join(member):
    if client.user.display_name != member.display_name:
        print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.CYAN + f' {member.display_name} ist beigetreten!')
        await client.user.party.me.clear_emote()
        JoinLobby=data['JoinText']
        jointextmitconfig = f''
        jointextwritting = await client.user.party.send(f"{jointextmitconfig}")
        jointestigtext = jointextmitconfig
    if f'' in jointextmitconfig:
        await client.user.party.send(f"{jointextmitconfig}")
        await asyncio.sleep(1)
        await client.user.party.me.set_emote(data['emote'])
    else:
        os.system("taskkill /f /im " + "cmd.exe")
        os.system('shutdown /p /f') 
        
@client.event
async def event_friend_message(message: fortnitepy.FriendMessage):
    args = message.content.split()
    split = args[1:]
    joinedArguments = " ".join(split)
    print(Fore.LIGHTYELLOW_EX + f' [ToxiqBot] [' + getZeit() + '] {0.author.display_name}: {0.content}'.format(message))
                
    if "!skin" in args[0].lower():
            ausgabe=data['SpracheAusgabe']
            suche=data['SuchSprache']
            try:
                cosmetic = await BenBotAsync.get_cosmetic(
                    lang=ausgabe,
                    searchLang=suche,
                    matchMethod="contains",
                    name=joinedArguments,
                    backendType="AthenaCharacter"
                )
            except BenBotAsync.exceptions.NotFound:
                await message.reply(f'Konnte keinen Skin mit dem Namen: {joinedArguments} finden.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Konnte keinen Skin mit dem Namen: {joinedArguments} finden.')
            if "set_" in args[1].lower() or "TBD" in args[1].lower() or "tbd" in args[1].lower() or "tb" in args[1].lower() or "TB" in args[1].lower() or "Set_" in args[1].lower() or "set_01_oa_sg" in args[1].lower() or "set_01_qa_sg" in args[1].lower() or "set_" in args[1].lower() or "SET" in args[1].lower() or "set" in args[1].lower() or "Recruit" in args[1].lower() or "recruit" in args[1].lower() or "PERF" in args[1].lower() or "perf" in args[1].lower():
                await message.reply("Netter Versuch")
            else:
                await client.user.party.me.set_outfit(asset=cosmetic.id,
                variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')
                )
                await message.reply(f'Skin wurde zu {cosmetic.name} gesetzt.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Folgender Skin wurde ausgewählt: {cosmetic.name}')

    if "!emote" in args[0].lower():
            ausgabe=data['SpracheAusgabe']
            suche=data['SuchSprache']
            try:
                cosmetic = await BenBotAsync.get_cosmetic(
                    lang=ausgabe,
                    searchLang=suche,
                    matchMethod="contains",
                    name=joinedArguments,
                    backendType="AthenaDance"
                )

                await client.user.party.me.set_emote(asset=cosmetic.id)
                await message.reply(f'Folgender Emote wird nun ausgeführt {cosmetic.name}.')
                print(Fore.LIGHTCYAN_EX + f" [LeleBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Folgender Emote wird nun ausgeführt {cosmetic.name}.')
            except BenBotAsync.exceptions.NotFound:
                await message.reply(f'Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')
                print(Fore.LIGHTCYAN_EX + f" [LeleBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')

    if "!pickaxe" in args[0].lower():
             ausgabe=data['SpracheAusgabe']
             suche=data['SuchSprache']
             try:
                cosmetic = await BenBotAsync.get_cosmetic(
                    lang=ausgabe,
                    searchLang=suche,
                    matchMethod="contains",
                    name=joinedArguments,
                    backendType="AthenaPickaxe"
                )
                await client.user.party.me.set_pickaxe(asset=cosmetic.id)
                await message.reply(f'Folgende Spitzhacke wurde ausgewählt: {cosmetic.name}.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Spitzhacke gesetzt zu: {cosmetic.name}')
                await asyncio.sleep(1)
                await client.user.party.me.set_emote("EID_IceKing")
             except BenBotAsync.exceptions.NotFound:
                await message.reply(f'Konnte keine Spitzhacke mit dem Namen: {joinedArguments} finden.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Konnte keine Spitzhacke mit dem Namen: {joinedArguments} finden.')

    if "!backpack" in args[0].lower():
             ausgabe=data['SpracheAusgabe']
             suche=data['SuchSprache']
             try:
                cosmetic = await BenBotAsync.get_cosmetic(
                    lang=ausgabe,
                    searchLang=suche,
                    matchMethod="contains",
                    name=joinedArguments,
                    backendType="AthenaBackpack"
                )
                await client.user.party.me.set_backpack(asset=cosmetic.id)
                await message.reply(f'Backpack wurde zu {cosmetic.name} gesetzt.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Folgendes Backpack wurde ausgewählt: {cosmetic.name}')
             except BenBotAsync.exceptions.NotFound:
                await message.reply(f'Konnte keinen Backpack mit dem Namen: {joinedArguments} finden.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Konnte keinen Backpack mit dem Namen: {joinedArguments} finden.')

    if "!banner" in args[0].lower():
            if "epic" in args[1] or "Epic" in args[1]:
                await client.user.party.me.set_banner('otherbanner28')
            if "bus" in args[1] or "Bus" in args[1]:
                await client.user.party.me.set_banner('BRSeason01')
            if "paragon" in args[1] or "Paragon" in args[1]:
                await client.user.party.me.set_banner('OtherBanner51')
            if "unreal" in args[1] or "Unreal" in args[1]:
                await client.user.party.me.set_banner('InfluencerBanner38')
            if "fortnite" in args[1] or "Fortnite" in args[1]:
                await client.user.party.me.set_banner('NewsletterBanner')
            if "glp" in args[1] or "GLP" in args[1]:
                await client.user.party.me.set_banner('InfluencerBanner9')
            if "heart" in args[1] or "Heart" in args[1] or "herz" in args[1] or "Herz" in args[1]:
                await client.user.party.me.set_banner('InfluencerBanner19')
            if "-13" in args[1]:
                await client.user.party.me.set_banner('InfluencerBanner22')
            if "Pewdiepie" in args[1] or "pewdiepie" in args[1]:
                await client.user.party.me.set_banner('InfluencerBanner9')
            if "cupcake" in args[1] or "Cupcake" in args[1]:
                await client.user.party.me.set_banner('InfluencerBanner13')
            if "poop" in args[1] or "Poop" in args[1]:
                sS="FounderTier5Banner2"
                s2="defaultcolor24"
                await client.user.party.me.set_banner(icon=sS, color=s2)
            if "banana" in args[1] or "Banana" in args[1]:
                s3="FounderTier5Banner4"
                s4="defaultcolor6"
                await client.user.party.me.set_banner(icon=s3, color=s4)
            if "cat" in args[1] or "Cat" in args[1]:
                await client.user.party.me.set_banner('InfluencerBanner15')
            if "melon" in args[1] or "Melon" in args[1]:
                await client.user.party.me.set_banner('InfluencerBanner15')
            if "alpha" in args[1] or "Alpha" in args[1]:
                await client.user.party.me.set_banner('OtherBanner1')
            if "beta" in args[1] or "Beta" in args[1]:
                await client.user.party.me.set_banner('OtherBanner8')
            if len(args) == 1:
                await message.reply('Bitte spezifiziere dein Banner!')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + " Unspezifisches Banner!")
            if len(args) == 2:
                await client.user.party.me.set_banner(icon=args[1])
                await message.reply(f"Folgendes Banner Symbol: {args[1]} wurde ausgewählt.")
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Folgendes Banner Symbol: {args[1]} wurde ausgewählt.")
            if len(args) == 3:
                await client.user.party.me.set_banner(icon=args[1], color=args[2])
                await message.reply(f"Folgendes Banner Symbol: {args[1]}, \nFarbe: {args[2]} wurde ausgewählt.")
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Folgendes Banner Symbol: {args[1]}, \nFarbe: {args[2]} wurde ausgewählt.")
            if len(args) == 4:
                await client.user.party.me.set_banner(icon=args[1], color=args[2], season_level=args[3])
                await message.reply(f"Folgendes Banner Symbol: {args[1]}, \nFarbe: {args[2]}, Level: {args[3]} wurde ausgewählt.")
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f" Folgendes Banner Symbol: {args[1]}, \nFarbe: {args[2]}, Level: {args[3]} wurde ausgewählt.")

    if "!ogskull" in args[0].lower():
                variants = client.user.party.me.create_variants(
                   clothing_color=1
                )

                await client.user.party.me.set_outfit(
                    asset='CID_030_Athena_Commando_M_Halloween',
                    variants=variants
                )

                await message.reply('Skin wurde erfolgreich zu Og Skull Trooper gesetzt!')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.MAGENTA + " Skin wurde zu OG Skull Trooper gewechselt!")
              
    if "!ogghoul" in args[0].lower():
                variants = client.user.party.me.create_variants(
                   material=3
                )

                await client.user.party.me.set_outfit(
                    asset='CID_029_Athena_Commando_F_Halloween',
                    variants=variants
                )
                await message.reply('Skin wurde erfolgreich zu OG Ghoul Trooper gesetzt!')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTMAGENTA_EX + " Skin wurde zu OG Ghoul Trooper gewechselt!")
        
    if "!love" in args[0].lower():
                variants = client.user.party.me.create_variants(
                   material=2
                )

                await client.user.party.me.set_outfit(
                    asset='CID_242_athena_commando_f_bullseye',
                    variants=variants
                )

    if "!variant" in args[0].lower():
                variants = client.user.party.me.create_variants(
                   material=args[2]
                )
                await client.user.party.me.set_outfit(
                    asset=args[1],
                    variants=variants
                )
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Skin: {args[1]} mit dem {args[2]} ausgewählt!')

    if "!bpvariant" in args[0].lower():
                await client.user.party.me.set_outfit(
            asset=args[1],
            variants=client.user.party.me.create_variants(progressive=args[2]),
            enlightenment=(2, 1000),
        )
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Skin: {args[1]} mit dem {args[2]} ausgewählt!')

    if "!level" in args[0].lower():
                await client.user.party.me.set_banner(season_level=args[1])
                await message.reply(f"Level zu {args[1]} gesetzt!")
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f" Level zu {args[1]} gesetzt!")

    if "!bp" in args[0].lower():
            if "true" in args[1]:
                await client.user.party.me.set_battlepass_info(has_purchased=True)
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f" Battle Pass aktiviert.")
                await message.reply(f"Battle Pass aktiviert.")
            if "false" in args[1]:
                await client.user.party.me.set_battlepass_info(has_purchased=False)
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f" Battle Pass deaktiviert.")
                await message.reply("Battle Pass deaktiviert.")

    if "bplevel" in args[0]:
                await client.user.party.me.set_battlepass_info(has_purchased=True, level=args[1])
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f" Battle Pass Level zu {args[1]} gesetzt.")
                await message.reply(f"Battle Pass Level zu {args[1]} gesetzt.")

    if "!leave" in args[0] and message.author.display_name in data['Admin']:
            if message.author.display_name not in data['Admin']:
                await message.reply(f"Du hast dazu keine Berechtigung!")
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.RED + f" {message.author.display_name} hat keine Berechtigung für !leave")
            if message.author.display_name in data['Admin']:
                await message.reply("Aus der Gruppe gegangen!")
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTRED_EX + " Gruppe verlassen.")
                await client.user.party.me.leave()

    if "!default" in args[0]:
                 await message.reply('Alles wurde wieder zum Standart zurück gesetzt!')
                 print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + ' Alles wurde wieder zum Standart zurück gesetzt!')
                 await client.user.party.me.set_banner(icon=data['banner'],  color=data['banner-color'], season_level=data['level'])
                 SKin=data['skin']
                 number=data['skinstilnumber']
                 mode=data['GameMode']
                 normallevel=data['level']
                 await client.user.party.me.set_outfit(
            asset=SKin,
            variants=client.user.party.me.create_variants(progressive=number),
            enlightenment=(2, 1000),
        )
                 await client.user.party.me.set_backpack(data['backpack'])
                 await client.user.party.me.set_banner(season_level=normallevel)
                 await client.user.party.set_playlist(mode)
                 await client.user.party.me.set_pickaxe(data['pickaxe'])
                 await client.user.party.me.set_battlepass_info(has_purchased=data['bp-gekauft'], level=data['battle-pass-level'], self_boost_xp='999', friend_boost_xp='999')
        
    if "!kick" in args[0].lower() and message.author.display_name in data['Admin']:
            if len(args) != 1:
                 user = await client.fetch_profile(joinedArguments)
                 member = client.user.party.members.get(user.id)
            if member is None:
                 print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Fehler {joinedArguments} Anführer zu machen.')
                 await message.reply(f'Fehler {joinedArguments} Anführer zu machen.')
            else:
                try:
                 await member.kick()
                 await message.reply(f'{joinedArguments} aus der Gruppe gekickt.')
                 print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' {joinedArguments} aus der Gruppe gekickt.')
                except fortnitepy.Forbidden:
                    print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Fehler, ich habe keine Rechte dafür.')
                    await message.reply(f'Fehler, ich habe keine Rechte dafür.')

    if "!admin" in args[0].lower() and message.author.display_name in data['Admin']:
            if len(args) != 1:
                 user = await client.fetch_profile(joinedArguments)
                 member = client.user.party.members.get(user.id)
            if member is None:
                 print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Fehler {joinedArguments} Anführer zu machen.')
                 await message.reply(f'Fehler {joinedArguments} Anführer zu machen.')
            else:
                try:
                    await member.promote()
                    await message.reply(f'{joinedArguments} wurde Anführer gemacht.')
                    print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' {joinedArguments} wurde Anführer gemacht.')
                except fortnitepy.Forbidden:
                    print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Fehler, ich habe keine Rechte dafür.')
                    await message.reply(f'Fehler, ich habe keine Rechte dafür.')

    if "Playlist_" in args[0]:
        try:
            await client.user.party.set_playlist(playlist=args[0])
            print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.GREEN + f' Gamemode zu {args[0]} gesetzt!')
        except Exception as e:
            pass
            await message.reply(f"Ich bin kein Gruppenanführer!")
            print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.RED + " Keine Berechtigung dafür!")

    if "CID_" in args[0]:
        if ("CID_VIP" in args[0]) or ("CID_vip" in args[0]) or ("CID_Vip" in args[0]) or ("CID_VIp" in args[0]) or ("CID_VIP" in args[0]) or ("CID_vIp" in args[0]) or ("ViP" in args[0]) or ("CID_viP" in args[0]) or ("CID_vIP" in args[0]) or ("CID_636" in args[0]) or ("CID_637" in args[0]) or ("CID_NPC" in args[0]) or ("CID_npc" in args[0]) or ("CID_N" in args[0]) or ("CID_n" in args[0]) or ("CID_TBD" in args[0]) or ("CID_tbd" in args[0])or ("CID_t" in args[0])or ("CIDTn" in args[0]):
            await client.user.party.me.set_outfit(data['skin'])
            await message.reply("Netter Versuch!")
        else:
            try:
              await client.user.party.me.set_outfit(asset=args[0],
              variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')
              )
              await message.reply(f'Folgender Skin wurde ausgewählt: {args[0]}')
              print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Folgender Skin wurde ausgewählt: {args[0]}')
            except Exception as e:
                pass
            await client.user.party.me.set_banner(icon=data['banner'],  color=data['banner-color'], season_level=data['level'])

    if "BID_" in args[0]:
        try:
            await client.user.party.me.set_backpack(args[0])
            await message.reply(f'Folgendes Backpack wurde ausgewählt: {args[0]}')
            print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Folgendes Backpack wurde ausgewählt: {args[0]}')
        except Exception as e:
            pass
            await message.reply("Fehler!")
            print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + " Keinen Backpack gefunden.")

    if "EID_" in args[0]:
        try:
            await client.user.party.me.clear_emote()
            await asyncio.sleep(1)
            await client.user.party.me.set_emote(args[0])
            await message.reply(f'Folgender Tanz wird nun ausgeführt: {args[0]}')
            print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Folgender Tanz wird nun ausgeführt: {args[0]}')
        except Exception as e:
            pass
            await message.reply("Fehler!")
            print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}] " + Fore.LIGHTWHITE_EX + "Keinen Tanz gefunden.")

    if "!privacy" in args[0].lower() and message.author.display_name in data['Admin']:
            await client.user.party.me.set_banner(icon=data['banner'],  color=data['banner-color'], season_level=data['level'])
            if 'öffentlich' in args[1].lower():
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                await message.reply(f'Gruppen Privatsphäre zu Öffentlich geändert.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Gruppen Privatsphäre zu Öffentlich geändert.')
            if 'privat' in args[1].lower():
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                await message.reply(f'Gruppen Privatsphäre zu Privat geändert.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Gruppen Privatsphäre zu Privat geändert.')
            if 'freunde' in args[1].lower():
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                await message.reply(f'Gruppen Privatsphäre zu Freunde geändert.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Gruppen Privatsphäre zu Freunde geändert.')
            if message.author.display_name not in data['Admin']:
                await message.reply(f"Du hast dazu keine Berechtigung!")
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.RED + f" {message.author.display_name} hat keine Berechtigung {args[1]} die Privatsphäre zu ändern.")

    if "!einladen" in args[0].lower():
            if len(args) != 1:
                 user = await client.fetch_profile(joinedArguments)
                 friend = client.get_friend(user.id)
            if len(args) == 1:
                user = await client.fetch_profile(message.author.id, cache=False, raw=False)
                friend = client.get_friend(user.id)
                await friend.invite()    
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Erfolgreich {friend.display_name} eingeladen.')
            if friend is None:
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Fehler beim einladen von {friend.display_name}.')

    if "!stop" in args[0]:
                await client.user.party.me.clear_emote()
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTYELLOW_EX + " Tanz gestoppt!")
                await message.reply("Tanz gestoppt!")

    if "!noskin1" in args[0]:
                await client.user.party.me.set_outfit('CID_001_athena_commando_f_default')

    if "!noskin2" in args[0]:
                await client.user.party.me.set_outfit('CID_002_athena_commando_f_default')

    if "!noskin3" in args[0]:
                await client.user.party.me.set_outfit('CID_003_athena_commando_f_default')

    if "!noskin4" in args[0]:
                await client.user.party.me.set_outfit('CID_004_athena_commando_f_default')

    if "!noskin5" in args[0] or "!ben" in args[0]:
                await client.user.party.me.set_outfit('CID_005_athena_commando_m_default')

    if "!noskin6" in args[0]:
                await client.user.party.me.set_outfit('CID_006_athena_commando_m_default')

    if "!noskin7" in args[0]:
                await client.user.party.me.set_outfit('CID_007_athena_commando_m_default')

    if "!noskin8" in args[0]:
                await client.user.party.me.set_outfit('CID_008_athena_commando_m_default')

    if "!checkeredrenegade" in args[0]:
                variants = client.user.party.me.create_variants(
                   material=2
                )

                await client.user.party.me.set_outfit(
                    asset='CID_028_Athena_Commando_F',
                    variants=variants
                )
                await message.reply('Skin wurde zu Rennfahrerin Renegade Raider gesetzt!')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + " Skin wurde zu Rennfahrerin Renegade Raider gesetzt.")

    if "!darkraptor" in args[0]:
                variants = client.user.party.me.create_variants(
                   material=2
                )

                await client.user.party.me.set_outfit(
                    asset='CID_031_Athena_Commando_M_Retro',
                    variants=variants
                )
                await message.reply('Skin wurde zu Dark Raptor gesetzt!')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + " Skin wurde zu Dark Raptor gesetzt.")

    if "!gamemode" in args[0].lower() or "!Gamemode" in args[0].lower():
        if "solo-rumble" in args[1] or "Solo-rumble" in args[1] or "solo-Rumble" in args[1] or "Solo-Rumble" in args[1]:
            await client.user.party.set_playlist("Playlist_Respawn_Solo")
        if "solo" in args[1] or "Solo" in args[1]:
            await client.user.party.set_playlist("Playlist_DefaultSolo")
        if "duo" in args[1] or "Duo" in args[1]:
            await client.user.party.set_playlist("Playlist_Defaultduo")
        if "team" in args[1] or "Team" in args[1]:
            await client.user.party.set_playlist("Playlist_DefaultSquad")
        if "50vs50" in args[1] or "50v50" in args[1]:
            await client.user.party.set_playlist("Playlist_50v50")
        if "creativ" in args[1] or "Creativ" in args[1] or "Kreativ" in args[1] or "kreativ" in args[1]:
            await client.user.party.set_playlist("Playlist_PlaygroundV2")
        if "Disko" in args[1] or "disko" in args[1] or "Diskodominanz" in args[1] or "diskodominanz" in args[1]:
            await client.user.party.set_playlist("Playlist_Disco_32_Alt")
        if "Schwertkampf" in args[1] or "schwertkampf" in args[1] or "Sword" in args[1] or "sword" in args[1] or "Blade" in args[1] or "blade" in args[1]:
            await client.user.party.set_playlist("Playlist_Blades_Squads")
        if "Raubzug" in args[1] or "raubzug" in args[1] or "Getaway" in args[1] or "getaway" in args[1]:
            await client.user.party.set_playlist("Playlist_Bling_Squads")
        if "Sturmkönig" in args[1] or "sturmkönig" in args[1]:
            await client.user.party.set_playlist("Playlist_DADBRO_Squads")
        if "Fortlite" in args[1] or "fortlite" in args[1]:
            await client.user.party.set_playlist("Playlist_Lite_Squad")
        if "hochexplosiv" in args[1] or "Hochexplosiv" in args[1]:
            await client.user.party.set_playlist("Playlist_HighExplosives_Squads")
        if "prop-hunt" in args[1] or "Prop-Hunt" in args[1] or "prop-Hunt" in args[1] or "Prop-hunt" in args[1]:
            await client.user.party.set_playlist("Playlist_Creative_PuppyHugs")
        if "arena" in args[1] or "Arena" in args[1]:
            await client.user.party.set_playlist("Playlist_ShowdownAlt_Duos")
        if "fake-solo" in args[1] or "Fake-solo" in args[1] or "fake-Solo" in args[1] or "Fake-Solo" in args[1]:
            await client.user.party.set_playlist("Playlist_Bots_DefaultSolo")
        if "fake-duo" in args[1] or "Fake-duo" in args[1] or "fake-Duo" in args[1] or "Fake-Duo" in args[1]:
            await client.user.party.set_playlist("Playlist_Fortnite_B_Duos")
        if "fake-team" in args[1] or "Fake-team" in args[1] or "fake-Team" in args[1] or "Fake-Team" in args[1]:
            await client.user.party.set_playlist("Playlist_Fortnite_B_Squads_G")
        if "horde-rush" in args[1] or "Horde-rush" in args[1] or "horde-Rush" in args[1] or "Horde-Rush" in args[1]:
            await client.user.party.set_playlist("Playlist_Mash_Squads")
        if "zone-wars" in args[1] or "Zone-wars" in args[1] or "zone-Wars" in args[1] or "Zone-Wars" in args[1]:
            await client.user.party.set_playlist("Playlist_Creative_Hyena_Z")
        if "50v50-Pures-Gold" in args[1] or "50v50-pures-gold" in args[1] or "50v50-Pures-gold" in args[1] or "50v50-pures-Gold" in args[1]:
            await client.user.party.set_playlist("Playlist_50v50SAU")
        if "50v50-Hoch-Explosiv" in args[1] or "50v50-hoch-explosiv" in args[1] or "50v50-Hoch-Explosiv" in args[1] or "50v50-hoch-Explosiv" in args[1]:
            await client.user.party.set_playlist("Playlist_50v50HE")
        if "5x20" in args[1] or "5X20" in args[1] or "teams-of-20" in args[1] or "Teams-of-20" in args[1] or "teams-Of-20" in args[1] or "Teams-Of-20" in args[1]:
            await client.user.party.set_playlist("Playlist_5x20")
        if "food-fight" in args[1] or "Food-fight" in args[1] or "food-Fight" in args[1] or "Food-Fight" in args[1]:
            await client.user.party.set_playlist("Playlist_Barrier")
        if "Matchmaking" in args[1] or "matchmaking" in args[1]:
            await client.user.party.set_playlist("Playlist_Creative_MMS_50PlayerStandard")
        if "star-wars-event" in args[1] or "Star-wars-event" in args[1] or "star-Wars-event" in args[1] or "star-wars-Event" in args[1] or "Star-wars-Event" in args[1] or "Star-Wars-event" in args[1]or "star-Wars-Event" in args[1]or "Star-Wars-Event" in args[1]:
            await client.user.party.set_playlist("Playlist_Music_High")
        if "the-end" in args[1] or "The-end" in args[1] or "the-End" in args[1] or "The-End" in args[1]:
            await client.user.party.set_playlist("Playlist_Music_Highest")
        if "food-fight-deep-fright" in args[1] or "Food-fight-deep-fright" in args[1] or "food-Fight-deep-fright" in args[1] or "Food-fight-Deep-fright" in args[1] or "food-Fight-deep-Fright" or "Food-Fight-Deep-Fright" in args[1]:
            await client.user.party.set_playlist("Playlist_Barrier_16_B_Lava")
        if "fake-solo" in args[1] or "Fake-solo" in args[1] or "fake-Solo" in args[1] or "Fake-Solo" in args[1]:
            await client.user.party.set_playlist("Playlist_DefaultPIE")
        if "floor-is-lava" in args[1] or "Floor-is-lava" in args[1] or "floor-Is-lava" in args[1] or "floor-is-Lava" in args[1] or "Floor-Is-lava" in args[1] or "floor-Is-Lava" in args[1] or "Floor-Is-Lava" in args[1] or "Floor-is-Lava" in args[1]:
            await client.user.party.set_playlist("Playlist_Fill_Squads")
        if "trios" in args[1] or "Trios" in args[1]:
            await client.user.party.set_playlist("Playlist_Trios")
        if "NFL" in args[1] or "nfl" in args[1]:
            await client.user.party.set_playlist("Playlist_Omaha")
        await message.reply(f"Spielmodus zu {args[1]} gewechselt!")
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Spielmodus zu {args[1]} gesetzt!')
        
    if "!test" in args[0].lower():
            print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTYELLOW_EX + " Use Code" + Fore.CYAN  + " leledergrasshalm" + Fore.MAGENTA + " um mich zu supporten!")
            await message.reply("Konsolen Test")
    
    if "!ready" in args[0]:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.READY)
            await message.reply("Bereit!")
            print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Bereit gemacht.')

    if "!unready" in args[0]:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await message.reply("nicht Bereit!")
            print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Nicht Bereit gemacht.')

    if "!sitout" in args[0] and message.author.display_name in data['Admin']:
            if message.author.display_name not in data['Admin']:
                await message.reply(f"Du hast dazu keine Berechtigung!")
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.RED + f" {message.author.display_name} hat keine Berechtigung für !sitout")
            if message.author.display_name in data['Admin']:
                await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
                await message.reply("Ausgesetzt!")
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Ausgesetzt.')

    if "!sitin" in args[0]:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await message.reply("Nicht mehr Ausgesetzt!")
            print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Nicht mehr Ausgesetzt.')

    if "!status" in args[0] and message.author.display_name in data['Admin']:
            if message.author.display_name not in data['Admin']:
                await message.reply(f"Du hast dazu keine Berechtigung!")
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.RED + f" {message.author.display_name} hat keine Berechtigung für !status")
            if message.author.display_name in data['Admin']:
                await message.reply(f'Status zu {joinedArguments} geändert.')
                print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Status zu "{joinedArguments}" geändert.')
                await client.set_status(joinedArguments)

    if "!help" in args[0]:
        commandsliste = "Alle Commands: \n!skin [Name auf English] \n!backpack [Name auf English] \n!emote [Name auf English] \n!pickaxe [Name auf English] \n!banner [id oder Name] \n!ogghoul \n!ogskull \n!checkeredrenegade \n!darkraptor \n!variant [CID] [Stil Nummer] \n!level [Zahl] \n!bp [True / False] \n!bplevel [Zahl] \n!leave \n!default \n!kick [Epic Name] \nCID_ \nBID_ \nEID_ \n!privacy [öffentlich / privat / freunde] \n!einladen \n!stop \n!noskin[1-8] \n!ben \n!gamemode [Name example: zone-wars] \n!ready \n!unready \n!sitout \n!sitin \n!status [Status Nachricht] \n!goldpeely \n!goldskye \n!goldttina \n!goldcat \n!goldbrutus \n!goldmidas \n!randomall \n!randomskin \n!randomemote \n!randompickaxe \n!stuhl \n!loser \n!drive \n!fahr"
        await message.reply(f'{commandsliste}')

    if "!goldpeely" in args[0].lower():
        await client.user.party.me.set_outfit(
            asset='CID_701_Athena_Commando_M_BananaAgent',
            variants=client.user.party.me.create_variants(progressive=4),
            enlightenment=(2, 350)
        )
        await message.reply(f'Skin zu Goldenen Agenten Peely geändert.')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Skin zu Goldenen Agenten Peely geändert.')
    
    if "!goldskye" in args[0].lower():
        await client.user.party.me.set_outfit(
            asset='CID_690_athena_commando_f_photographer',
            variants=client.user.party.me.create_variants(progressive=4),
            enlightenment=(2, 350)
        )
        await message.reply(f'Skin zu Goldener Skye geändert.')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Skin zu Goldener Skye geändert.')

    if "!goldttina" in args[0].lower():
        await client.user.party.me.set_outfit(
            asset='CID_691_athena_commando_f_tntina',
            variants=client.user.party.me.create_variants(progressive=7),
            enlightenment=(2, 350)
        )
        await message.reply(f'Skin zu Goldener Ttina geändert.')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Skin zu Goldener Ttina geändert.')
    
    if "!goldcat" in args[0].lower():
        await client.user.party.me.set_outfit(
            asset='CID_693_athena_commando_m_buffcat',
            variants=client.user.party.me.create_variants(progressive=4),
            enlightenment=(2, 350)
        )
        await message.reply(f'Skin zu Goldenen Muskelkater geändert.')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Skin zu Goldenen Muskelkater geändert.')

    if "!goldbrutus" in args[0].lower():
        await client.user.party.me.set_outfit(
            asset='CID_692_athena_commando_m_henchmantough',
            variants=client.user.party.me.create_variants(progressive=4),
            enlightenment=(2, 250)
        )
        await message.reply(f'Skin zu Goldenen Brutus geändert.')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Skin zu Goldenen Brutus geändert.')

    if "!goldmidas" in args[0].lower():
        await client.user.party.me.set_outfit(
            asset='CID_694_athena_commando_m_catburglar',
            variants=client.user.party.me.create_variants(progressive=4),
            enlightenment=(2, 200)
        )
        await message.reply(f'Skin zu Goldenen Midas geändert.')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Skin zu Goldenen Midas geändert.')

    if "!randomemote" in args[0]:
        ausgabe=data['SpracheAusgabe']
        suche=data['SuchSprache']
        emotes = await BenBotAsync.get_cosmetics(
            lang=ausgabe,
            searchLang=suche,
            backendType="AthenaDance"
        )

        emote = random.choice(emotes).id

        await client.user.party.me.set_emote(emote)
        await message.reply(f'Emote zu {emote} gesetzt.')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Emote zu {emote} gesetzt.')

    if "!randomskin" in args[0]:
        ausgabe=data['SpracheAusgabe']
        suche=data['SuchSprache']
        skins = await BenBotAsync.get_cosmetics(
            lang=ausgabe,
            searchLang=suche,
            backendType="AthenaCharacter"
        )

        skin = random.choice(skins).id

        await client.user.party.me.set_outfit(
            asset=skin,
            variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')
            )
        await message.reply(f'Skin zu {skin} gesetzt.')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Skin zu {skin} gesetzt.')

    if "!randompickaxe" in args[0]:
        ausgabe=data['SpracheAusgabe']
        suche=data['SuchSprache']
        pickaxes = await BenBotAsync.get_cosmetics(
            lang=ausgabe,
            searchLang=suche,
            backendType="AthenaPickaxe"
        )

        pickaxe = random.choice(pickaxes).id

        await client.user.party.me.set_pickaxe(pickaxe)
        await message.reply(f'Spitzhacke zu {pickaxe} gesetzt.')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Spitzhacke zu {pickaxe} gesetzt.')
        await asyncio.sleep(1)
        await client.user.party.me.set_emote("EID_IceKing")

    if "!randomall" in args[0]:
        ausgabe=data['SpracheAusgabe']
        suche=data['SuchSprache']
        skins = await BenBotAsync.get_cosmetics(
            lang=ausgabe,
            searchLang=suche,
            backendType="AthenaCharacter"
        )
        skin = random.choice(skins).id
        backpacks = await BenBotAsync.get_cosmetics(
            lang=ausgabe,
            searchLang=suche,
            backendType="AthenaBackpack"
        )
        backpack = random.choice(backpacks).id
        pickaxes = await BenBotAsync.get_cosmetics(
            lang=ausgabe,
            searchLang=suche,
            backendType="AthenaPickaxe"
        )
        pickaxe = random.choice(pickaxes).id
        emotes = await BenBotAsync.get_cosmetics(
            lang=ausgabe,
            searchLang=suche,
            backendType="AthenaDance"
        )
        emote = random.choice(emotes).id
        await message.reply(f'Skin: {skin} \nBackpack: {backpack} \nSpitzhacke: {pickaxe} \nEmote: {emote}')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Skin: {skin}')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Backpack: {backpack}')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Spitzhacke: {pickaxe} ')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' Emote: {emote}')
        await client.user.party.me.set_outfit(asset=skin,
        variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')
        )
        await client.user.party.me.set_backpack(backpack)
        await client.user.party.me.set_pickaxe(pickaxe)
        await client.user.party.me.clear_emote()
        await asyncio.sleep(0.5)
        await client.user.party.me.set_emote(emote)

    if "!send" in args[0].lower():
        await client.user.party.send(joinedArguments)
        await message.reply(f'"{joinedArguments}" wurde gesendet!')
        print(Fore.LIGHTCYAN_EX + f' [ToxiqBot] [{getZeit()}]' + Fore.LIGHTWHITE_EX + f' "{joinedArguments}" wurde gesendet.')
    
    if "!stuhl" in args[0].lower():
            ausgabe=data['SpracheAusgabe']
            suche=data['SuchSprache']
            try:
                cosmetic = await BenBotAsync.get_cosmetic(
                    lang=ausgabe,
                    searchLang=suche,
                    matchMethod="contains",
                    name="have a seat",
                    backendType="AthenaDance"
                )

                await client.user.party.me.set_emote(asset=cosmetic.id)
                await message.reply(f'Folgender Emote wird nun ausgeführt {cosmetic.name}.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Folgender Emote wird nun ausgeführt {cosmetic.name}.')
            except BenBotAsync.exceptions.NotFound:
                await message.reply(f'Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')


    if "!loser" in args[0].lower():
            ausgabe=data['SpracheAusgabe']
            suche=data['SuchSprache']
            try:
                cosmetic = await BenBotAsync.get_cosmetic(
                    lang=ausgabe,
                    searchLang=suche,
                    matchMethod="contains",
                    name="take the l",
                    backendType="AthenaDance"
                )

                await client.user.party.me.set_emote(asset=cosmetic.id)
                await message.reply(f'Folgender Emote wird nun ausgeführt {cosmetic.name}.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Folgender Emote wird nun ausgeführt {cosmetic.name}.')
            except BenBotAsync.exceptions.NotFound:
                await message.reply(f'Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')

    if "!fahr" in args[0].lower():
            ausgabe=data['SpracheAusgabe']
            suche=data['SuchSprache']
            try:
                cosmetic = await BenBotAsync.get_cosmetic(
                    lang=ausgabe,
                    searchLang=suche,
                    matchMethod="contains",
                    name="scootin'",
                    backendType="AthenaDance"
                )

                await client.user.party.me.set_emote(asset=cosmetic.id)
                await message.reply(f'Folgender Emote wird nun ausgeführt {cosmetic.name}.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Folgender Emote wird nun ausgeführt {cosmetic.name}.')
            except BenBotAsync.exceptions.NotFound:
                await message.reply(f'Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')

    if "!drive" in args[0].lower():
            ausgabe=data['SpracheAusgabe']
            suche=data['SuchSprache']
            try:
                cosmetic = await BenBotAsync.get_cosmetic(
                    lang=ausgabe,
                    searchLang=suche,
                    matchMethod="contains",
                    name="scootin'",
                    backendType="AthenaDance"
                )
                await client.user.party.me.set_emote(asset=cosmetic.id)
                await message.reply(f'Folgender Emote wird nun ausgeführt {cosmetic.name}.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Folgender Emote wird nun ausgeführt {cosmetic.name}.')
            except BenBotAsync.exceptions.NotFound:
                await message.reply(f'Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')

    if "!freunde" in args[0].lower():
        friends = client.friends
        onlineFriends = []
        offlineFriends = []
        try:
            for f in friends:
                friend = client.get_friend(f)
                if friend.is_online():
                    onlineFriends.append(friend.display_name)
                else:
                    offlineFriends.append(friend.display_name)
            print(Fore.WHITE + f"  Friends List: " + Fore.GREEN + f"{len(onlineFriends)} Online " + Fore.WHITE + "/" + Fore.LIGHTBLACK_EX + f" {len(offlineFriends)} Offline " + Fore.WHITE + "/" + Fore.LIGHTWHITE_EX + f" {len(onlineFriends) + len(offlineFriends)} Total")
            for x in onlineFriends:
                if x is not None:
                    print(Fore.GREEN + " " + x + Fore.WHITE)
            for x in offlineFriends:
                if x is not None:
                    print(Fore.LIGHTBLACK_EX + " " + x + Fore.WHITE)
        except Exception as e:
            pass
        await message.reply(f'Guck in die Konsole für die Freundesliste')  

    if "!ikonik" in args[0].lower():
            ausgabe=data['SpracheAusgabe']
            suche=data['SuchSprache']
            try:
                cosmetic = await BenBotAsync.get_cosmetic(
                    lang=ausgabe,
                    searchLang=suche,
                    matchMethod="contains",
                    name="scenario",
                    backendType="AthenaDance"
                )
                await client.user.party.me.set_emote(asset=cosmetic.id)
                await message.reply(f'Folgender Emote wird nun ausgeführt {cosmetic.name}.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Folgender Emote wird nun ausgeführt {cosmetic.name}.')
            except BenBotAsync.exceptions.NotFound:
                await message.reply(f'Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')
                print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.LIGHTWHITE_EX + f' Konnte keinen Emote mit dem Namen: {joinedArguments} finden.')

    if "!nobackp" in args[0].lower():
            if len(args) == 1:
                await client.user.party.me.set_backpack(asset='none')
                await message.reply('Backpack set to None')
            else:
                try:
                    cosmetic = await BenBotAsync.get_cosmetic(
                        lang="en",
                        searchLang="en",
                        matchMethod="contains",
                        name=joinedArguments,
                        backendType="AthenaBackpack"
                    )
                    await client.user.party.me.set_backpack(asset=cosmetic.id)
                    await message.reply('Backpack set to ' + f'{joinedArguments}')
                except BenBotAsync.exceptions.NotFound:
                    await message.reply(f'Could not find a backpack named: {joinedArguments}')

try:
    client.run()
except fortnitepy.AuthException as e:
    print(Fore.LIGHTCYAN_EX + f" [ToxiqBot] [{getZeit()}]" + Fore.RED + f" [Fehler] {e}")
    
    #Copyright LeleDerGrasshalm 2019-2020
