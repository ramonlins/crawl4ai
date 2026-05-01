# Dota 2 Patch 7.25
# Source: https://www.dota2.com/patches/7.25

Gameplay Update
7.25
General Updates
All Pick hero picking has been reworked. It now has 5 rounds, each round Radiant and Dire pick 1 hero each at the same time and the selections each team makes is hidden until the next round. If a duplicate pick occurs, the player who picked it second will be given some extra time to select another hero.
Reworked how hero banning works in All Pick. Previously half of the voted heroes would get banned. Now each ban has a 50% chance of succeeding. If there are less than 10 heroes banned, heroes will automatically roll for banning based on their ban rate at your MMR bracket.
  

Power Runes initially spawn at 4 minutes now (subsequent spawns are still every 2 minutes)
Power Runes no longer spawn on both sides of the map at 40 minutes
  

Removed the team based rubber band mechanic for hero kills (formula reworked and simplified below)
  

Old Hero Kill AoE Gold:
=
Definitions:
- NWRankingFactor = 1.6 -> 0.4 based on the killer's NW rank within the team
- NWPoorFactor = 1.2->0.6 based on the victims NW rank within their team
- ComebackFactor = 1 if the team is behind, 0 if ahead
  

1 Hero: NWPoorFactor* NWRankingFactor * ( 126 + 4.5 * VictimLevel + ComebackFactor * ( VictimNetWorth * 0.026 + 70) / 1 ) )
  

2 Hero: NWPoorFactor* NWRankingFactor * ( 63 + 3.6 * VictimLevel + ComebackFactor * ( VictimNetWorth * 0.026 + 70) / 2 ) )
  

3 Hero: NWPoorFactor* NWRankingFactor * ( 31.5 + 2.7 * VictimLevel + ComebackFactor * ( VictimNetWorth * 0.026 + 70) / 3 ) )
  

4 Hero: NWPoorFactor* NWRankingFactor * ( 22.5 + 1.8 * VictimLevel + ComebackFactor * ( VictimNetWorth * 0.026 + 70) / 4 ) )
  

5 Hero: NWPoorFactor* NWRankingFactor * ( 18 + 0.9 * VictimLevel + ComebackFactor * ( VictimNetWorth * 0.026 + 70) / 5 ) )
  

New Hero Kill AoE Gold:
=
( 50 + VictimNetWorth*0.03 ) / #Heroes
  

Hero kill sprees gold bounty increased from 60->480 to 200->690
Hero kill sprees xp bounty increased from 400->1800 to 500->2040
  

Captain's Mode now has ban counts per phase changed from 3/2/1 to 4/1/1
Random Draft hero pool reduced from 50 to 40
  

Radiant Ancient creeps are now easier to stack
Tier 1 neutral item drop rates increased from 10 to 14%
Fountain attack damage increased from 275 to 300
Neutral creep Ice Armor slow reduced from 30 to 25
Neutral creep Ice Armor armor reduced from 6 to 5
Illusion rune now has similar cast mechanics as Manta (shuffle, dispel, dodge)
Neutral Creep Updates
Item Updates
Town Portal Scroll
Cost increased from 50 to 90
Boots of Travel
No longer has an active
Upgrades Town Portal Scroll while equipped. Reduces its cooldown to 40 seconds, allows it to target units, and does not consume a charge on usage.
Movement speed increased from 32/35% to 38/44%
  

Javelin
Damage reduced from 100 to 80
Mjollnir
Attack speed reduced from +75 to +65
  

Orb of Venom
Damage per second reduced from 5 to 2
Melee slow increased from 12% to 15%
Slow duration reduced from 3 to 2
  

Ring of Regen
Cost reduced from 250 to 225
Headdress
No longer requires an Iron Branch
No longer provides +3 All Stats
HP regen increased from 2 to 2.5
Sage's Mask
Mana regeneration increased from 0.75 to 1
Cost reduced from 250 to 225
Ring of Basilius
No longer requires an Iron Branch
No longer provides +3 All Stats
Mana regen aura increased from 1.25 to 1.4
Buckler
No longer requires an Iron Branch
No longer provides +3 All Stats
Recipe cost reduced from 300 to 225
Armor increased from 2 to 2.5 (heroes and player units only)
Vladmir's Offering
All Stats reduced from +6 to +5
Mana regen increased from 1.25 to 1.5
Veil of Discord
Mana regen increased from 1.25 to 1.5
  

Bloodthorn
Now requires Hyperstone instead of Crystalys
Attack Damage reduced from +75 to +30
Attack Speed increased from 30 to 85
No longer has a passive critical strike chance
  

Battle Fury
Now requires Broadsword and Mithril Hammer instead of Demon Edge and Recipe
Broadsword
Cost reduced from 1200 to 1000
Damage reduced from +18 to +16
  

Crystalys
Recipe cost increased from 500 to 700
Damage reduced from 45 to 34
Critical Strike chance increased from 20% to 30%
  

Vanguard
No longer has a 200 gold recipe
Crimson Guard
Recipe cost increased by 200
Abyssal Blade
Recipe cost increased by 200
  

Eaglesong
Cost reduced from 3200 to 3000
Butterfly
Agility reduced from 35 to 30
Ethereal Blade
Ether Blast primary attribute damage reduced from 200% to 150%
Ether Blast base damage increased from 75 to 125
  

Kaya and Sange
Mana loss reduction increased from 16% to 18%
Spell amplification increased from 12% to 14%
Yasha and Kaya
Mana loss reduction increased from 16% to 18%
Spell amplification increased from 12% to 14%
  

Nullifier
No longer mutes enemies
Now continuously dispels the target
Duration reduced from 6 to 5
Slow reduced from 100% for 0.4 seconds to 80% for 0.5 seconds
Cooldown reduced from 13 to 11
Cast range increased from 600 to 900
Armor increased from +5 to +8
Damage increased from +65 to +80
  

Force Staff
Cast range reduced from 750 to 550 (850 for enemies)
Hurricane Pike
Allied cast range reduced from 800 to 550
Force Staff
No longer undispellable
Glimmer Cape
Cast range reduced from 800 to 550
Hurricane Pike
No longer undispellable
Observer Ward
Vision reduced from 1600 to 1400
Holy Locket
Recipe reduced from 800 to 500
Necronomicon
Gold and XP bounties reduced from 100/150/200 to 50/100/150
Recipe cost reduced from 1300 to 1250
Aeon Disk
Cooldown reduced from 115 to 105
Silver Edge
Debuff now reduces regen and heals by 50%
  

Clarity
Duration reduced from 50 to 30 seconds
Mana regeneration increased from 4.5 to 6
Infused Raindrops
Mana regen increased from +0.75 to +0.9
Bottle
Cost reduced from 650 to 625
Medallion of Courage
Mana regeneration increased from 0.75 to 1.25
Solar Crest
Mana regeneration increased from 1.5 to 1.75
Ring of Health
Health regen increased from 6 to 6.5
Cost reduced from 850 to 825
Void Stone
Cost reduced from 850 to 825
Perseverance
Health regen increased from 6 to 6.5
Hood of Defiance
Health regeneration increased from 8 to 8.5
Pipe of Insight
Health regeneration increased from 8 to 8.5
No longer provides +3 All Stats
Lotus Orb
Manacost increased from 75 to 150
Helm of Iron Will
Health regen increased from 3.5 to 5
Cost increased from 900 to 925
Ring of Tarrasque
Cost reduced from 700 to 600
Health regen increased from 3.75 to 4.5
Tranquil Boots
Health regen reduced from 16 to 14
  

Neutral Item Updates
Faded Broach
Mana reduced from 225 to 200
Iron Talon
Now works on Ancients
Poor Man's Shield
Agility increased from 7 to 8
Philosopher's Stone
Gold income increased from +60 to +70
Grove Bow
Attack Speed increased from 10 to 15
Nether Shawl
Magic resistance increased from 20% to 25%
Spider Legs
Turn rate increased from +30% to +50%
Passive movement speed increased from 24% to 28%
Repair Kit
Self regen increased from +17 to +20
Enchanted Quiver
Cooldown reduced from 8 to 6
Havoc Hammer
Knockback area increased from 300 to 350
Slow now affects attack speed
Flicker
Cooldown reduced from 5 to 4
Range reduced from 600 to 450
The Leveller
Attack speed increased from 50 to 60
Minotaur Horn
Spell immunity duration increased from 1.75 to 2
Witless Shako
Health increased from 1000 to 1200
Seer Stone
Now provides +10 Mana Regen
Ballista
Knockback pure damage increased from 30 to 40
Woodland Striders
Health regen increased from 50 to 60
  

  

Hero Updates
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/abaddon.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Abaddon
Talents
Level 25 Talent increased from 375 AoE Mist Coil to 425
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/alchemist.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Alchemist
Agility gain increased from 1.2 to 1.5
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/arc_warden.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Arc Warden
Base movement speed increased from 280 to 285
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/batrider.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Batrider
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/batrider_firefly.png%20)
Firefly
Movement speed reduced from 5/10/15/20% to 4/8/12/16%
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/batrider_flamebreak.png%20)
Flamebreak
Impact damage reduced from 50/75/100/125 to 30/60/90/120
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/beastmaster.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Beastmaster
Base attack speed increased from 100 to 110
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/beastmaster_wild_axes.png%20)
Wild Axes
Damage type changed from Physical to Magical
Debuff duration increased from 10 to 12
No longer pierce Spell Immunity
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/bloodseeker.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Bloodseeker
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/bloodseeker_bloodrage.png%20)
Bloodrage
Heal rescaled from 13/17/21/25% to 10/15/20/25%
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/bounty_hunter.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Bounty Hunter
Reworked Scepter. Now applies Jinada to Shuriken Toss, increases cast range to 650 and lowers cooldown to 6.
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/bounty_hunter_shuriken_toss.png%20)
Shuriken Toss
Manacost from 135 to 120/125/130/135
Talents
Level 15 Talent changed from +50 Attack Speed to +75 Shuriken Toss Damage
Level 20 Talent changed from +125 Shuriken Toss Damage to +60 Attack Speed
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/brewmaster.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Brewmaster
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/brewmaster_primal_split.png%20)
Primal Split
Fire brewling damage increased from 80/120/160 to 80/130/180
Fire Permanent Immolation interval changed from 1 to 0.5
Talents
Level 20 Talent increased from +1500 Health to Primal Split Units to +1750
Level 25 Talent increased from -65s Primal Split Cooldown to -75s
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/broodmother.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Broodmother
Talents
Level 10 Talent increased from +200 Health to +250
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/chaos_knight.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Chaos Knight
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/chaos_knight_phantasm.png%20)
Phantasm
Cooldown reduced from 145 to 145/135/125
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/chaos_knight_reality_rift.png%20)
Reality Rift
Cast range increased from 475/550/625/700 to 550/600/650/700
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/clinkz.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Clinkz
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/clinkz_death_pact.png%20)
Death Pact
No longer has a neutral level requirement
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/clinkz_burning_army.png%20)
Burning Army
Damage increased from 28% to 30%
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/crystal_maiden.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Crystal Maiden
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/crystal_maiden_freezing_field.png%20)
Freezing Field
Scepter Frostbite timer reduced from 2.5 to 2.0
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/dark_seer.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Dark Seer
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/dark_seer_surge.png%20)
Surge
Movement speed changed from 70% to +250
Cooldown increased from 16/14/12/10 to 19/16/13/10
Talents
Level 10 Talent changed from +90 Damage to +125 Ion Shell Radius
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/dazzle.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Dazzle
Reworked Scepter. When you cast an ability, you automatically launch an attack on 8 enemy units (up to 800 units away).
Talents
Level 10 Talent reduced from +75 Damage to +60
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/death_prophet.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Death Prophet
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/death_prophet_exorcism.png%20)
Exorcism
Now provides a 20% movement speed increase
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/dragon_knight.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Dragon Knight
Base movement speed increased by 5
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/drow_ranger.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Drow Ranger
Attack animation improved from 0.65 to 0.55
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/earth_spirit.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Earth Spirit
Agility gain increased from 1.5 to 2.4
Talents
Level 10 Talent increased from +50 Damage to +65
Level 10 Talent increased from +300 Rolling Boulder Distance to +400
Level 20 Talent increased from +15% Spell Amplification to +20%
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/elder_titan.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Elder Titan
Talents
Level 15 Talent increased from +15% Magic Resistance to +20%
Level 20 Talent increased from +100 Echo Stomp Damage to +125
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/ember_spirit.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Ember Spirit
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/ember_spirit_searing_chains.png%20)
Searing Chains
Cooldown reduced from 14/12/10/8 to 11/10/9/8
Manacost rescaled from 110 to 80/90/100/110
Talents
Level 10 Talent increased from +275 Flame Guard Absorption to +350
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/enchantress.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Enchantress
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/enchantress_bunny_hop.png%20)
Sproink
Distance increased from 450 to 500
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/enigma.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Enigma
Base intelligence increased by 3
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/enigma_black_hole.png%20)
Black Hole
Damage increased from 50/100/150 to 100/150/200
Talents
Level 15 Talent increased from +40 Malefice Instance Damage to +100
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/grimstroke.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Grimstroke
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/grimstroke_ink_creature.png%20)
Phantom's Embrace
Rend damage increased from 80/170/260/350 to 120/200/280/360
Talents
Level 15 Talent increased from +15% Spell Amplification to +20%
Level 20 Talent increased from +600 Stroke of Fate Cast Range to +800
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/gyrocopter.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Gyrocopter
Attack backswing reduced from 0.97 to 0.65
Strength gain increased from 2.3 to 2.5
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/gyrocopter_flak_cannon.png%20)
Flak Cannon
Attack count from 3/4/5/6 to 2/3/4/5
Cooldown reduced from 40 to 20
Duration reduced from 15 to 10
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/gyrocopter_call_down.png%20)
Call Down
Missile two damage increased from 100/150/200 to 200/275/350
Cooldown increased from 55/50/45 to 90
Talents
Level 20 Talent increased from -25s Call Down Cooldown to -50s
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/huskar.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Huskar
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/huskar_berserkers_blood.png%20)
Berserker's Blood
Max attack speed reduced from 160/220/280/340 to 140/200/260/320
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/juggernaut.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Juggernaut
Reworked Scepter. Grants Swift Slash. Performs a mini omnislash that lasts 0.8 seconds. Cast Range 650. Cooldown 15. Manacost 100
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/keeper_of_the_light.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Keeper of the Light
Talents
Level 10 Talent changed from +6% Spell Amplification to -3s Blinding Light Cooldown
Level 15 Talent changed from +1 Will-O-Wisp Health Count to +2 Will-O-Wisp Flicker
Level 20 Talent changed from +40% Magic Resistance to +250 Will-O-Wisp AoE
Level 25 Talent changed from +3 Will-O-Wisp Flicker to +3 Will-O-Wisp Health Count
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/kunkka.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Kunkka
Talents
Level 10 Talent increased from +6 Armor to +7
Level 25 Talent increased from +60% Tidebringer Cleave to +80%
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/legion_commander.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Legion Commander
Talents
Level 15 Talent increased from +65 Overwhelming Odds Hero Damage to +80
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/leshrac.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Leshrac
Agility gain increased from 2.3 to 2.8
Attack backswing reduced from 0.77 to 0.6
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/leshrac_pulse_nova.png%20)
Pulse Nova
Activation cost reduced from 70/90/110 to 70
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/lina.png)
Attack point reduced from 0.75 to 0.65
Attack backswing reduced from 0.78 to 0.6
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/lone_druid.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Lone Druid
Talents
Level 10 Talent changed from +125 Attack Range to +30 Spirit Bear Movement Speed
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/luna.png)
Base strength increased from 18 to 21
Base intelligence increased from 18 to 23
Agility gain reduced from 3.6 to 3.4
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/lycan.png)
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/lycan_feral_impulse.png%20)
Feral Impulse
Health regen increased from 1/3/5/7 to 2/4/6/8
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/lycan_shapeshift.png%20)
Shapeshift
Duration increased from 18 to 22
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/magnataur.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Magnus
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/magnataur_shockwave.png%20)
Shockwave
Slow duration increased from 0.75 to 0.9
Talents
Level 10 Talent increased from +200 Health to +250
Level 15 Talent increased from +75 Shockwave Damage to +100
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/mars.png)
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/mars_gods_rebuke.png%20)
God's Rebuke
Scepter now always lowers the cooldown rather than just during Arena of Blood
Scepter cooldown from 1.4 to 3.5
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/medusa.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Medusa
Talents
Level 15 Talent increased from +25% Mystic Snake Mana Gain to +40%
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/mirana.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Mirana
Base damage increased by 2
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/mirana_arrow.png%20)
Sacred Arrow
Damage increased from 40/120/200/280 to 60/150/240/330
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/furion.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Nature's Prophet
Attack backswing reduced from 0.77 to 0.6
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/furion_wrath_of_nature.png%20)
Wrath of Nature
Cooldown increased from 60 to 85
Now provides you with +4/5/6 damage per unit killed for 50 seconds.
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/night_stalker.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Night Stalker
Base intelligence increased by 2
Base health regen increased by 0.5
Movement speed increased from 295 to 300
Talents
Level 15 Talent increased from +15% Lifesteal to +25%
Level 25 Talent increased from -40s Dark Ascension Cooldown to -60s
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/ogre_magi.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Ogre Magi
Base armor reduced by 1
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/phoenix.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Phoenix
Base health regen increased from 0.5 to 1
Base damage increased by 2
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/puck.png)
Base damage reduced by 2
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/pudge.png)
Base health regen increased from 0 to 1
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/pudge_innate_graft_flesh.png%20)
Flesh Heap
Now provides 8/10/12/14% Magic Resistance instead of health regen
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/pugna.png)
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/pugna_nether_ward.png%20)
Nether Ward
Mana drain rescaled from 0.3/0.6/0.9/1.2% to 0.6/0.8/1/1.2%
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/pugna_life_drain.png%20)
Life Drain
Damage reduced from 175/275/375 to 150/225/300
Cooldown reduced from 22 to 7
Scepter now also increases damage to 200/300/400
Break distance reduced from 1000 to 900
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/queenofpain.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Queen of Pain
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/queenofpain_shadow_strike.png%20)
Shadow Strike
Slow increased from 20/30/40/50% to 20/35/50/65%
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/queenofpain_sonic_wave.png%20)
Sonic Wave
Cooldown reduced from 135 to 125
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/riki.png)
Talents
Level 15 Talent reduced from +35 Damage to +30
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/rubick.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Rubick
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/rubick_fade_bolt.png%20)
Fade Bolt
Manacost increased from 120/130/140/150 to 135/140/145/150
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/sand_king.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Sand King
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/sandking_caustic_finale.png%20)
Caustic Finale
Slow duration increased from 3 to 3/3.5/4/4.5
Now reduces attack speed as well
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/sandking_epicenter.png%20)
Epicenter
Damage per pulse increased from 110 to 110/120/130
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/shadow_demon.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Shadow Demon
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/shadow_demon_demonic_purge.png%20)
Demonic Purge
Damage increased from 250/350/450 to 300/400/500
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/silencer.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Silencer
Intelligence steal is now part of Glaives of Wisdom instead of being innate
Talents
Level 15 Talent increased from +12% Arcane Curse Slow to +14%
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/slark.png)
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/slark_pounce.png%20)
Pounce
Scepter distance reduced from 1200 to 1100
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/snapfire.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Snapfire
Added Scepter ability, Gobble Up. Allows you to swallow an allied creep or hero and spit it towards enemies, stunning enemies in the area for 1.5 seconds and leaving a glob on the floor dealing 100 DPS for 3 seconds. Units can stay in his belly up to 3 seconds. Impact radius 400. Cooldown 40 seconds. Cast Range 150
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/snapfire_scatterblast.png%20)
Scatterblast
Cooldown increased from 10 to 13/12/11/10
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/sniper.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Sniper
Base damage increased by 4
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/sniper_headshot.png%20)
Headshot
Damage reduced from 30/60/90/120 to 20/50/80/110
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/sniper_assassinate.png%20)
Assassinate
Scepter cast time reduced from 1 to 0.5 seconds
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/spectre.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Spectre
Base health regen increased from 1.5 to 2.5
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/spectre_shadow_step.png%20)
Shadow Step
Scepter ability cooldown reduced from 70 to 35
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/spirit_breaker.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Spirit Breaker
Reworked Scepter. Increases Charge of Darkness movement speed by 100 and reduces cooldown by 5.
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/storm_spirit.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Storm Spirit
Base attack speed increased from 100 to 110
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/sven.png)
Base movement speed increased by 5
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/techies.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Techies
Talents
Level 25 Talent increased from +25 Mines Movement Speed to +75
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/templar_assassin.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Templar Assassin
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/templar_assassin_trap_teleport.png%20)
Psionic Projection
Scepter ability cast time reduced from 2 to 1 second
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/terrorblade.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Terrorblade
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/terrorblade_metamorphosis.png%20)
Metamorphosis
Scepter is now a standalone ability you gain while in Metamorphosis. Cooldown 90.
Talents
Level 10 Talent increased from +20 Movement Speed to +25
Level 10 Talent increased from +15% Evasion to +20%
Level 15 Talent increased from +250 Health to +300
Level 15 Talent increased from +25 Attack Speed to +30
Level 20 Talent increased from -8s Reflection Cooldown to -10s
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/tidehunter.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Tidehunter
Base strength increased by 3
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/tinker.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Tinker
Talents
Level 10 Talent changed from +125 Cast Range to +150
Level 15 Talent changed from +2s March of the Machines Duration to +3s
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/tiny.png)
Attack backswing reduced from 1 to 0.7
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/treant.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Treant Protector
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/treant_natures_guise.png%20)
Nature's Guise
Regen amplification increased from 25% to 40%
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/tusk.png)
Base movement speed increased by 5
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/tusk_ice_shards.png%20)
Ice Shards
Damage increased from 60/120/180/240 to 70/140/210/280
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/undying.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Undying
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/undying_tombstone.png%20)
Tombstone
Zombies damage increased from 36 to 46
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/ursa.png)
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/ursa_fury_swipes.png%20)
Fury Swipes
Damage increased from 7/14/21/28 to 10/20/30/40
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/ursa_overpower.png%20)
Overpower
Attack count reduced from 4/5/6/7 to 3/4/5/6
Cooldown reduced from 16/14/12/10 to 16/13/10/7
Manacost reduced from 75 to 55/60/65/70
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/ursa_enrage.png%20)
Enrage
No longer has a Fury Swipes multiplier
Duration increased from 4 to 4/4.5/5
Cooldown reduced from 70/50/30 to 50/40/30
Now grants +50% Status Resistance
Talents
Level 25 Talent changed from Enrage +80% Status Resistance to +3 Overpower Attacks
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/vengefulspirit.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Vengeful Spirit
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/vengefulspirit_magic_missile.png%20)
Magic Missile
Cast range increased from 500 to 550
Damage rescaled from 100/175/250/325 to 90/180/270/360
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/viper.png)
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/viper_viper_strike.png%20)
Viper Strike
Damage increased from 60/100/145 to 80/120/160
Talents
Level 10 Talent increased from +8% Spell Lifesteal to +10%
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/visage.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Visage
Base attack speed increased from 100 to 110
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/visage_soul_assumption.png%20)
Soul Assumption
Collection radius increased from 1375 to 1500
Cast range increased from 900 to 1000
Talents
Level 25 Talent changed from -2s Gravekeeper's Cloak to +6 Gravekeeper's Cloak Stacks
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/void_spirit.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Void Spirit
Added Scepter. Resonant Pulse is now a charge-based ability with 2 charges and it now silences enemies for 2 seconds.
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/warlock.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Warlock
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/warlock_shadow_word.png%20)
Shadow Word
Cast point improved from 0.5 to 0.4
Talents
Level 10 Talent increased from +150 Cast Range to +175
Level 20 Talent increased from 300 Shadow Word AoE to 375
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/weaver.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_agility.png)Weaver
Base intelligence increased from 13 to 16
Intelligence gain increased from 1.8 to 2.0
Base mana regen increased from 0.4 to 0.75
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/weaver_shukuchi.png%20)
Shukuchi
Movement bonus increased from +225 to +220/240/260/280
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/windrunner.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_universal.png)Windranger
Intelligence gain increased from 3 to 3.6
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/winter_wyvern.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Winter Wyvern
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/winter_wyvern_cold_embrace.png%20)
Cold Embrace
Is now considered a heal instead of regen
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/witch_doctor.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_intelligence.png)Witch Doctor
Paralzying Casks manacost reduced from 110/120/130/140 to 80/100/120/140
Abilities
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/abilities/witch_doctor_death_ward.png%20)
Death Ward
Scepter no longer has a bounce limit
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/skeleton_king.png)
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/hero_strength.png)Wraith King
Vampiric Aura lifesteal reduced from 6/12/18/24% to 5/10/15/20%
Vampiric Aura lifesteal and damage on your hero is now 1.5x
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/heroes/zuus.png)
Base movement speed increased from 295 to 300
Attack point improved from 0.45 to 0.35
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/valve_logo.png)![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/dota_footer_logo.png)
Dota and the Dota logo are trademarks and/or registered trademarks of Valve Corporation. 2025 Valve Corporation, all rights reserved.
