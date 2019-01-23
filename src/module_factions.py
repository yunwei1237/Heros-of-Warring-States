#-*-coding:utf-8-*-
from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),
  ##天子国
  ("culture_1",  "Zhou", 0, 0.9, [], []),
  ##大国
  ("culture_2",  "Qi", 0, 0.9, [], []),
  ("culture_3",  "Chu", 0, 0.9, [], []),
  ("culture_4",  "Yan", 0, 0.9, [], []),
  ("culture_5",  "Jin", 0, 0.9, [], []),
  ("culture_6",  "Han", 0, 0.9, [], []),
  ("culture_7",  "Zhao", 0, 0.9, [], []),
  ("culture_8",  "Wei", 0, 0.9, [], []),
  ("culture_9",  "Qin", 0, 0.9, [], []),
  ##中国
  ("culture_10",  "Wu", 0, 0.9, [], []),
  ("culture_11",  "Yue", 0, 0.9, [], []),
  ("culture_12",  "Ba", 0, 0.9, [], []),
  ("culture_13",  "Shu", 0, 0.9, [], []),
  ("culture_14",  "Song", 0, 0.9, [], []),
  ("culture_15",  "ZhongShan", 0, 0.9, [], []),
  ("culture_16",  "Lu", 0, 0.9, [], []),
  ## 小国
  ("culture_17",  "Zhen", 0, 0.9, [], []),
  ("culture_18",  "Wei", 0, 0.9, [], []),
  ("culture_19",  "Tan", 0, 0.9, [], []),
  ("culture_20",  "Ju", 0, 0.9, [], []),
  ("culture_21",  "Chen", 0, 0.9, [], []),
  ("culture_22",  "Xu", 0, 0.9, [], []),
  ("culture_23",  "Xu", 0, 0.9, [], []),
  ## 少数民族
  ("culture_24",  "XiongNu", 0, 0.9, [], []),
  ("culture_25",  "DongHu", 0, 0.9, [], []),
  ("culture_26",  "SuShen", 0, 0.9, [], []),
  ("culture_27",  "WuSun", 0, 0.9, [], []),
  ("culture_28",  "Qiang", 0, 0.9, [], []),
  ##　备用国家
#  ("culture_29",  "XiongNu", 0, 0.9, [], []),
#  ("culture_30",  "DongHu", 0, 0.9, [], []),
#  ("culture_31",  "SuShen", 0, 0.9, [], []),
#  ("culture_32",  "WuSun", 0, 0.9, [], []),
#  ("culture_33",  "Qiang", 0, 0.9, [], []),
#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
  ## 天子国：周国
  ### 大国：齐国、楚国、燕国、晋（韩国、赵国、魏国）、秦国。
  ### 中国：吴国、越国、巴国、蜀国、宋国、中山国、鲁国
  ### 小国：郑国、卫国、郯国、莒国、陈国、徐国、（滕国、邹国、费国）
  #少数民族：匈奴、东胡、肃慎、乌孙、羌
  ## 玩家国家
  ("player_faction","Player Faction",0, 0.9, [], []),
  ## 玩家支持的阵营
  ("player_supporters_faction","Player Faction",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], []),
  ## 周国   
  ("kingdom_1",  "Kingdom of Zhou", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x99FF00),
  ## 齐国
  ("kingdom_2",  "Kingdom of Qi",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFF0000),
  ## 楚国
  ("kingdom_3",  "Kingdom of Chu",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFFFF00),
  ## 燕国
  ("kingdom_4",  "Kingdom of Yan",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFFFFCC),
  ## 晋国
  ("kingdom_5",  "Kingdom of Jin",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x99CC66),
  ## 韩国
  ("kingdom_6",  "Kingdom of Han", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFF99CC),
  ## 赵国
  ("kingdom_7",  "Kingdom of Zhao", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x9966FF),
  ## 魏国
  ("kingdom_8",  "Kingdom of Wei",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x996600),
  ## 秦国
  ("kingdom_9",  "Kingdom of Qin", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x0000000),
  ## 吴国
  ("kingdom_10",  "Kingdom of Wu", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC3366),
  ## 越国
  ("kingdom_11",  "Kingdom of Yue",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC00CC),
  ## 巴国
  ("kingdom_12",  "Kingdom of Ba",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x990066),
  ## 蜀国
  ("kingdom_13",  "Kingdom of Shu", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x339999),
  ## 宋国
  ("kingdom_14",  "Khergit Song", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00CCFF),
  ## 中山国
  ("kingdom_15",  "Kingdom of ZhongShan",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x3366FF),
  ## 鲁国
  ("kingdom_16",  "Kingdom of Lu",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x330000),
  ## 郑国
  ("kingdom_17",  "Kingdom of Zhen",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x006600),
  ## 卫国
  ("kingdom_18",  "Kingdom of Wei",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x333333),
  ## 郯国
  ("kingdom_19",  "Kingdom of Tan",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x660066),
  ## 莒国
  ("kingdom_20",  "Kingdom of Ju",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x000033),
  ## 陈国
  ("kingdom_21",  "Kingdom of Chen",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x330000),
  ## 徐国
  ("kingdom_22",  "Kingdom of Xue",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCCCC66),
  ## 蔡国
  ("kingdom_23",  "Kingdom of Cai",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCCFF99),
  
  ## 少数民族
  ## 匈奴
  ("kingdom_24",  "Kingdom of XiongNu",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x666600),
  ## 东胡
  ("kingdom_25",  "Kingdom of DongHu",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x666600),
  ## 肃慎
  ("kingdom_26",  "Kingdom of SuShen",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x666600),
  ## 乌孙
  ("kingdom_27",  "Kingdom of WuSun",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x666600),
  ## 羌
  ("kingdom_28",  "Kingdom of Qiang",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x666600),
##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "robber_knights", 0, 0.1, [], []),

  ("khergits","Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("undeads","Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","Slavers", 0, 0.1, [], []),
  ("peasant_rebels","Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","Noble Refugees", 0, 0.5,[], []),
]
