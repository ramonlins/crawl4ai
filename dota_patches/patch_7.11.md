# Dota 2 Patch 7.11
# Source: https://www.dota2.com/patches/7.11

Gameplay Update
7.11
General Updates
This version is focused on changing how the gold and buyback formulas work
  

Buyback cost changed from 100 + ( Level * Level * 1.5) + (Time * 0.25) to 100 + Networth / 13
Buyback no longer reduces gold earned after respawning
  

AoE gold for the losing team no longer scales with the overall team networth difference, just the individual networth of the dying hero. Previously, a core on your team doing really well meant that a support on your team dying gave an increasing amount of gold to the enemy.
  

General:Default:-The comeback component is now just (DyingHeroNetWorth * 0.026 + 70) / # of killers 
This takes the place of the components below that considers NetWorth   
  
For example in the 1 killer case, it replaces (NetWorthEarlyFactor * 90 + NetWorthFactor * 0.03375)  
  
Like the previous formula, it is only given to the losing team
  

The gold multiplier based on the dying hero's net worth rank changed from 1.2/1.1/1.0/0.9/0.8 to 1.2/1.05/0.9/0.75/0.6
  

General:Default:For reference, the previous AoE gold formula is listed below:
  

General:Default:Terms:
General:Default:--
General:Default:NetWorthDifference = ( EnemyTeamNetWorth / AlliedTeamNetWorth ) - 1 [With a min of zero and a max of 1]
General:Default:NetWorthFactor = NetWorthDifference * VictimNetWorth
General:Default:NetWorthEarlyFactor (for when Enemy has more NW) = ( EnemyTeamNetWorth - AlliedTeamNetWorth ) / 4000 [Has a max of 1]
General:Default:NetWorthPoorFactor = 1.3 - 0.1 * NetWorthRank (dying's hero's networth rank)
General:Default:NetWorthRankingFactor (hero's rank amongst allies involved in the kill): For 1/2/3/4/5 from poorest to richest are: { 1 } / { 1.3, 0.7 } / { 1.3, 1.0, 0.7 } / { 1.3, 1.1, 0.9, 0.7 } / { 1.3, 1.15, 1.0, 0.85, 0.7}
  

General:Default:Formula:
General:Default:--
General:Default:1 Killer: NetWorthPoorFactor * NetWorthRankingFactor * ( 126 + 4.5 * VictimLevel + NetWorthEarlyFactor * 90 + NetWorthFactor * 0.03375 )
General:Default:2 Killer: NetWorthPoorFactor * NetWorthRankingFactor * ( 63 + 3.6 * VictimLevel + NetWorthEarlyFactor * 67.5 + NetWorthFactor * 0.03375 )
General:Default:3 Killer: NetWorthPoorFactor * NetWorthRankingFactor * ( 31.5 + 2.7 * VictimLevel + NetWorthEarlyFactor * 45 + NetWorthFactor * 0.03375 )
General:Default:4 Killer: NetWorthPoorFactor * NetWorthRankingFactor * ( 22.5 + 1.8 * VictimLevel + NetWorthEarlyFactor * 31.5 + NetWorthFactor * 0.027 )
General:Default:5 Killer: NetWorthPoorFactor * NetWorthRankingFactor * ( 18 + 0.9 * VictimLevel + NetWorthEarlyFactor * 22.5 + NetWorthFactor * 0.02025 )
Neutral Creep Updates
Item Updates
Neutral Item Updates
Hero Updates
![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/valve_logo.png)![](https://cdn.steamstatic.com/apps/dota2/images/dota_react/dota_footer_logo.png)
Dota and the Dota logo are trademarks and/or registered trademarks of Valve Corporation. 2025 Valve Corporation, all rights reserved.
