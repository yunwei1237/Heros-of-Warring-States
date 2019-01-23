#-*-coding:utf-8-*-
from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17.0, 52.5),[(trp_player,1,0),(trp_swadian_knight,30,0)]),
("temp_party","temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0.0, 0.0),[]),
("camp_bandits","camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1.0, 1.0),[(trp_unarmed_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

("temp_party_2","temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0.0, 0.0),[]),
#Used for calculating casulties.
("temp_casualties","casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
("temp_casualties_2","casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
("temp_casualties_3","casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
("temp_wounded","enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
("temp_killed", "enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
("main_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
("encountered_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
("collective_friends_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
("player_casualties","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
("enemy_casualties","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
("ally_casualties","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),

("collective_enemy","collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
  #TODO: remove this and move all to collective ally
("collective_ally","collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),
("collective_friends","collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.0, 1.0),[]),

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  城镇
("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.7, 62.9),[]),
  
  ###天子国：周国
  ### 大国：齐国、楚国、燕国、晋（韩国、赵国、魏国）、秦国。
  ### 中国：吴国、越国、巴国、蜀国、宋国、中山国、鲁国
  ### 小国：郑国、卫国、郯国、莒国、陈国、徐国、蔡国（滕国、邹国、费国）
  
  ## 周国
  #  洛阳
("town_1","luoyang",  icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(26.7, -14.9),[], 135),
  ## 【齐国】
  #  临淄
("town_2","linzi", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-86.3, -85.0),[], 175),
  #  即墨
("town_3","jimo",   icon_town_snow|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-127.1, -61.8),[], 90),
  #  蓬莱
("town_4","penglai",   icon_town_steppe|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-137.1, -101.3),[], 310),
  ## 【楚国】
  # 郢（都）
("town_5","yingdu",   icon_town|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(41.9, 76.4),[], 240),
  # 寿春
("town_6","shouchun",   icon_town_snow|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-61.4, 34.5),[], 150),
  # 上庸
("town_7","shangyong", icon_town|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(90.3, 31.1),[], 25),
  ## 【燕国】
  # 蓟
("town_8","ji",icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-48.1, -158.3),[], 60),
  # 孤竹
("town_9","guzhu",  icon_town_steppe|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-87.9, -171.7),[], 135),
  ## 【晋国】(赵魏韩)
  #  邯郸
("town_10","handan",     icon_town|pf_town, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-16.0, -77.0),[], 290),
  #  安邑
("town_11","anyi",  icon_town|pf_town, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(7.4, -45.8),[], 90),
  #  阳翟
("town_12","yangdi",   icon_town|pf_town, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-15.2, -39.3),[], 155),
  ## 【秦国】
  #  咸阳
("town_13","xianyang",  icon_town|pf_town, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(119.7, -18.8),[], 170),
  #  义渠
("town_14","yiqu",     icon_town|pf_town, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(105.8, -67.6),[], 120),
  #  雍（都）
("town_15","yongdu",   icon_town|pf_town, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(156.0, -29.0),[], 80),
  ## 【吴国】
  #  姑苏
("town_16","gusu",     icon_town|pf_town, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-154.4, 48.1),[], 290),
  #  广陵
("town_17","guangling",  icon_town|pf_town, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-118.4, 26.1),[], 90),
  ## 【越国】
  #  会稽
("town_18","kuaiji",   icon_town|pf_town, no_menu, pt_none, fac_kingdom_11,0,ai_bhvr_hold,0,(-159.8, 87.3),[], 155),

  #  宣（城）
("town_19","xuan",  icon_town|pf_town, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-112.8, 72.0),[], 135),
  ## 【巴国】
  #  江州
("town_20","jiangzhou", icon_town|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(153.2, 80.0),[], 175),

  ## 【蜀国】
  #  成都
("town_21","chengdu",   icon_town_snow|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(211.4, 49.9),[], 90),
  ## 【宋国】
  #  商丘
("town_22","shangqu",   icon_town_steppe|pf_town, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-35.7, -14.1),[], 310),
  ## 【中山国】
  #  灵寿
("town_23","lingshou",   icon_town|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-0.6, -112.8),[], 240),
  ## 【鲁国】
  #  曲阜
("town_24","qufu",   icon_town_snow|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-63.2, -47.3),[], 150),
  #  薛(城)
("town_25","xue", icon_town|pf_town, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-74.0, -22.9),[], 25),
  ## 【郑国】
  #  新郑
("town_26","xinzheng",icon_town|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-6.7, -5.2),[], 60),
  ## 【卫国】
  #  朝歌
("town_27","chaoge",  icon_town_steppe|pf_town, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-11.8, -58.5),[], 135),
  ## 【郯国】
  #  郯（城）
("town_28","tan",     icon_town|pf_town, no_menu, pt_none, fac_kingdom_19,0,ai_bhvr_hold,0,(-93.6, -19.0),[], 290),
  ## 【莒国】
  #  莒父
("town_29","jufu",  icon_town|pf_town, no_menu, pt_none, fac_kingdom_20,0,ai_bhvr_hold,0,(-101.0, -44.6),[], 90),
  ## 【陈国】
  #  宛丘
("town_30","wanqiu",   icon_town|pf_town, no_menu, pt_none, fac_kingdom_21,0,ai_bhvr_hold,0,(-27.1, 7.7),[], 155),
  ## 【徐国】
  #  彭（城）
("town_31","peng",  icon_town|pf_town, no_menu, pt_none, fac_kingdom_22,0,ai_bhvr_hold,0,(-72.2, -7.9),[], 170),
  ## 【蔡国】
  #  上蔡
("town_32","shangcai",     icon_town|pf_town, no_menu, pt_none, fac_kingdom_23,0,ai_bhvr_hold,0,(-20.6, 18.9),[], 120),


## 备用
# ("town_33","yongdu",   icon_town|pf_town, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(156.0, -29.0),[], 80),
# ("town_34","gusu",     icon_town|pf_town, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-154.4, 48.1),[], 290),
# ("town_35","guangling",  icon_town|pf_town, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-118.4, 26.1),[], 90),
# ("town_36","kuaiji",   icon_town|pf_town, no_menu, pt_none, fac_kingdom_11,0,ai_bhvr_hold,0,(-159.8, 87.3),[], 155),

#   Aztaq_Castle       
#  Malabadi_Castle
#  城堡
  ## 周国
  #  3
  #  洛南,渑池,函谷（关）
("castle_1","luonan",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(42.4, -7.7),[],50),
("castle_2","yingchi",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(41.1, -21.1),[],75),
("castle_3","hangu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(27.8, -20.3),[],100),
  ## 【齐国】
  #  15
  #  北（城）,文（城）    ,夜（邑）,莱西（城）,纪（城）,淳于（城）,密（城）,琅琊（城）,安平,昌（城）,
  #  莱芜        ,葵丘（邑）,历下        ,阿（城）    ,夹谷
("castle_4","bei",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-144.6, -132.2),[],180),
("castle_5","wen",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-166.0, -92.9),[],90),
("castle_6","ye",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-126.8, -92.1),[],55),
("castle_7","laixi",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-133.1, -79.7),[],45),
("castle_8","ji",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-104.2, -79.4),[],30),
("castle_9","chunyu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-105.8, -66.1),[],100),
("castle_10","mi",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-110.3, -57.8),[],110),
("castle_11","langya",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-115.0, -48.7),[],75),
("castle_12","anping",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-93.0, -81.8),[],95),
("castle_13","chang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-83.4, -66.8),[],115),
("castle_14","laiwu",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-89.7, -64.5),[],90),
("castle_15","kuiqiu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-76.9, -82.4),[],235),
("castle_16","lixia",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-62.6, -64.8),[],45),
("castle_17","a",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-42.4, -62.9),[],15),
("castle_18","jiagu",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-78.8, -55.4),[],300),
  ## 【楚国】
  # 29
  # 蒙（城）,钟离（城）,巨阳 ,六（城）,舒（城）,桐（城）,息（城）,蓼（城）,黄（城）,松阳,
  # 城阳        ,西阳            ,柏举 ,鄂（城）,彭            ,艾            ,江夏        ,宛（城）,申（城）,邓（城）,
  # 唐（城）,随（城）    ,荆门 ,竟陵        ,秭归        ,巫            ,枝江        ,鼎（城）,武陵
("castle_19","meng",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-50.7, 9.4),[],280),
("castle_20","zhongli",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-89.4, 20.1),[],260),
("castle_21","juyang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-46.2, 17.8),[],260),
("castle_22","liu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-62.6, 55.0),[],260),
("castle_23","shu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-81.2, 58.4),[],80),
("castle_24","tong",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-74.4, 69.3),[],260),
("castle_25","xi",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-19.5, 29.1),[],260),
("castle_26","liao",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-32.0, 37.9),[],260),
("castle_27","huang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-23.7, 39.8),[],260),
("castle_28","songyang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-50.0, 80.2),[],260),
("castle_29","chengyang",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(3.9, 39.1),[],280),
("castle_30","xiyang",icon_castle_d|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-5.2, 50.8),[],260),
("castle_31","boju",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-11.7, 60.7),[],260),
("castle_32","e",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-28.1, 84.6),[],260),
("castle_33","peng",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-44.5, 84.6),[],80),
("castle_34","ai",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-33.7, 91.1),[],260),
("castle_35","jiangxia",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-18.9, 78.6),[],260),
("castle_36","wan",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(28.5, 4.7),[],260),
("castle_37","shen",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(20.8, 15.6),[],260),
("castle_38","deng",icon_castle_d|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(41.3, 33.1),[],260),
("castle_39","tang",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(25.9, 38.7),[],280),
("castle_40","sui",icon_castle_d|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(13.4, 44.2),[],260),
("castle_41","jingmen",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(34.3, 62.8),[],50),
("castle_42","jingling",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(14.9, 84.5),[],75),
("castle_43","zigui",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(88.7, 46.3),[],100),
("castle_44","wu",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(88.9, 60.7),[],180),
("castle_45","zhijiang",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(62.3, 64.2),[],90),
("castle_46","ding",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(54.0, 103.2),[],55),
("castle_47","wuling",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(46.9, 88.4),[],45),
  ## 【燕国】
  #  8
  #  海（城）,葫芦（城）,唐山（城）,无终,军粮（城）,涿鹿,高柳,容城
  #
("castle_48","hai",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-160.6, -166.2),[],30),
("castle_49","hulu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-120.8, -168.5),[],100),
("castle_50","tangshan",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-79.8, -156.4),[],110),
("castle_51","wuzhong",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-67.5, -161.8),[],75),
("castle_52","junliang",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-58.8, -125.6),[],95),
("castle_53","zhuolu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-15.5, -154.7),[],115),
("castle_54","gaoliu",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(10.7, -157.4),[],90),
("castle_55","rong",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-35.1, -137.7),[],50),
  ## 【晋国】(赵魏韩)
  #   23
  #   新（城）,朔（城）,代（城）,神池(城),娄烦,晋阳        ,平遥（城）,箕（城）,邢（城）,巨鹿,
  #   坝丘        ,晋（城）,霍（城）,蒲（城） ,平阳,翼（城）,曲沃            ,侯马        ,绛（城）,运（城）,
  #   虞（城）,苪（城）,虢（城）,
  #
("castle_56","xin",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(31.0, -136.5),[],75),
("castle_57","shuo",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(41.3, -126.8),[],100),
("castle_58","dai",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(30.3, -112.8),[],180),
("castle_59","shenchi",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(43.1, -114.9),[],90),
("castle_60","loufan",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(39.6, -104.4),[],55),
("castle_61","jinyang",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(30.1, -97.3),[],45),
("castle_62","pingyao",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(38.4, -79.6),[],30),
("castle_63","qi",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(1.0, -79.7),[],100),
("castle_64","xing",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-11.3, -95.0),[],110),
("castle_65","julu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-22.7, -104.1),[],75),
("castle_66","beiqiu",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-39.5, -80.8),[],95),
("castle_67","jin",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-3.9, -57.3),[],115),
("castle_68","huo",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(43.1, -66.2),[],90),
("castle_69","pu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(60.6, -65.5),[],235),
("castle_70","pingyang",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(55.5, -59.5),[],45),
("castle_71","yi",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(40.7, -55.2),[],15),
("castle_72","quwo",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(45.9, -50.0),[],300),
("castle_73","houma",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(50.0, -45.2),[],280),
("castle_74","jiang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(57.7, -40.8),[],260),
("castle_75","yun",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(57.7, -35.6),[],260),
("castle_76","yu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(51.8, -31.5),[],260),
("castle_77","rui",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(66.2, -27.2),[],80),
("castle_78","guo",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(56.6, -18.4),[],260),
  ## 【秦国】
  #   13
  #   定阳,烁阳,渭南（城）,卢氏,商（城）,泾阳,旬阳,狄道,豕原,棉诸,
  #   南郑,临垗,武都
  #
("castle_79","dingyang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(18.4, -35.4),[],260),
("castle_80","yueyang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(94.6, -27.0),[],260),
("castle_81","weinan",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(91.4, -16.1),[],260),
("castle_82","lushi",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(55.9, -11.7),[],260),
("castle_83","shang",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(74.3, -5.9),[],280),
("castle_84","jingyang",icon_castle_d|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(117.5, -26.6),[],260),
("castle_85","xunyang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(100.1, 20.0),[],260),
("castle_86","didao",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(201.1, -38.4),[],260),
("castle_87","shiyuan",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(215.0, -43.7),[],80),
("castle_88","mianzhu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(185.3, -32.7),[],260),
("castle_89","nanzheng",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(167.1, 7.4),[],260),
("castle_90","linzhao",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(226.3, -27.4),[],260),
("castle_91","wudu",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_9,0,ai_bhvr_hold,0,(212.7, -19.1),[],260),
  ## 【吴国】
  #  10
  #  盐（城）,善道,淮,棠（城）,邗（城）,延陵,太仓,槜李,湖（城）,鸠兹
  #
("castle_92","yan",icon_castle_d|pf_castle, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-137.4, 11.3),[],260),
("castle_93","shangdao",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-112.0, 7.2),[],280),
("castle_94","huai",icon_castle_d|pf_castle, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-107.4, 12.6),[],260),
("castle_95","tang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-117.6, 18.4),[],50),
("castle_96","han",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-129.9, 23.2),[],75),
("castle_97","yanling",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-138.9, 40.7),[],100),
("castle_98","taicang",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-160.3, 51.4),[],180),
("castle_99","zuili",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-160.5, 65.0),[],90),
("castle_100","hu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-140.6, 68.7),[],55),
("castle_101","jiuzi",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_10,0,ai_bhvr_hold,0,(-108.3, 55.9),[],45),
  ## 【越国】
  #  6
  #  无句,余杭,夫椒,余姚,甬东,姑蔑
  #
("castle_102","wuju",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_11,0,ai_bhvr_hold,0,(-65.6, 81.8),[],30),
("castle_103","yuhang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_11,0,ai_bhvr_hold,0,(-136.3, 77.4),[],100),
("castle_104","fujiao",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_11,0,ai_bhvr_hold,0,(-157.8, 81.7),[],110),
("castle_105","yuzhao",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_11,0,ai_bhvr_hold,0,(-170.9, 81.5),[],50),
("castle_106","yongdong",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_11,0,ai_bhvr_hold,0,(-182.0, 92.5),[],75),
("castle_107","gumie",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_11,0,ai_bhvr_hold,0,(-140.4, 97.0),[],100),
  ## 【巴国】
  #  6
  #  大竹,涪陵,黄平,修文,昭通,毕节
  #
("castle_108","dazhu",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_12,0,ai_bhvr_hold,0,(160.5, 64.6),[],180),
("castle_109","peiling",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_12,0,ai_bhvr_hold,0,(147.4, 89.5),[],90),
("castle_110","huangping",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_12,0,ai_bhvr_hold,0,(173.1, 77.4),[],55),
("castle_111","xiuwen",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_12,0,ai_bhvr_hold,0,(144.5, 103.1),[],45),
("castle_112","zhaotong",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_12,0,ai_bhvr_hold,0,(135.8, 60.7),[],30),
("castle_113","bijie",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_12,0,ai_bhvr_hold,0,(171.5, 101.5),[],100),
  ## 【蜀国】
  #  6
  #  梓潼,乐山,安雅,西昌,德昌,九龙
  #
("castle_114","zitong",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_13,0,ai_bhvr_hold,0,(202.7, 10.7),[],110),
("castle_115","leshan",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_13,0,ai_bhvr_hold,0,(193.3, 77.6),[],75),
("castle_116","anya",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_13,0,ai_bhvr_hold,0,(195.8, 64.1),[],95),
("castle_117","xichang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_13,0,ai_bhvr_hold,0,(224.0, 66.3),[],115),
("castle_118","dechang",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_13,0,ai_bhvr_hold,0,(221.1, 95.4),[],90),
("castle_119","jiulong",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_13,0,ai_bhvr_hold,0,(208.5, 82.3),[],235),
  ## 【宋国】
  #  7
  #  陶（城）,兰考,开封（城）,葵丘,夏（城）,萧（城）,永（城）
  #
("castle_120","tao",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_14,0,ai_bhvr_hold,0,(-28.1, -30.7),[],45),
("castle_121","lankao",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_14,0,ai_bhvr_hold,0,(-24.1, -24.0),[],15),
("castle_122","kaifeng",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_14,0,ai_bhvr_hold,0,(-17.7, -16.3),[],300),
("castle_123","kuiqiu",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_14,0,ai_bhvr_hold,0,(-31.3, -18.1),[],280),
("castle_124","xia",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_14,0,ai_bhvr_hold,0,(-42.8, -9.3),[],260),
("castle_125","xiao",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_14,0,ai_bhvr_hold,0,(-60.9, -15.6),[],260),
("castle_126","yong",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_14,0,ai_bhvr_hold,0,(-50.6, 1.3),[],260),
  ## 【中山国】
  #  3
  #  广灵,灵丘,肥
  #
("castle_127","guangling",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_15,0,ai_bhvr_hold,0,(11.2, -140.8),[],80),
("castle_128","lingqiu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_15,0,ai_bhvr_hold,0,(8.5, -131.9),[],260),
("castle_129","fei",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_15,0,ai_bhvr_hold,0,(11.5, -120.3),[],260),
  ## 【鲁国】
  #  17
  #  铸    ,曲池,长勺,堂阜        ,防（城）,费（城）,鄅,邾    ,邹（城）,滕（城）,
  #  宿    ,须句,夫钟,郓（城）,武（城）,邿            ,甲父
  #
("castle_130","zhu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-52.9, -59.2),[],260),
("castle_131","quchi",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-54.7, -54.1),[],260),
("castle_132","changshao",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-62.6, -52.8),[],260),
("castle_133","tangfu",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-84.8, -50.1),[],280),
("castle_134","fang",icon_castle_d|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-89.6, -49.4),[],260),
("castle_135","fei",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-82.9, -41.9),[],260),
("castle_136","yu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-86.2, -39.1),[],260),
("castle_137","zhu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-76.8, -36.9),[],80),
("castle_138","zou",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-65.2, -39.7),[],260),
("castle_139","teng",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-67.5, -34.2),[],260),
("castle_140","su",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-43.3, -56.8),[],260),
("castle_141","xuju",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-46.3, -52.8),[],260),
("castle_142","fuzhong",icon_castle_d|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-42.7, -50.2),[],260),
("castle_143","jun",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-33.3, -42.0),[],280),
("castle_144","wu",icon_castle_d|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-42.9, -36.4),[],260),
("castle_145","shi",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-54.6, -37.8),[],50),
("castle_146","jiafu",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_16,0,ai_bhvr_hold,0,(-38.0, -27.7),[],75),
  ## 【郑国】
  #  11
  #  共（城）,延津,制,虎牢（关）,京（城）,郑（城）,颖谷,长葛,鄢陵,许（城）,
  #  郾（城）
  #
("castle_147","gong",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_17,0,ai_bhvr_hold,0,(-0.0, -43.9),[],100),
("castle_148","yanjin",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_17,0,ai_bhvr_hold,0,(-14.0, -24.3),[],180),
("castle_149","zhi",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_17,0,ai_bhvr_hold,0,(12.0, -20.7),[],90),
("castle_150","hulao",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_17,0,ai_bhvr_hold,0,(0.1, -23.1),[],55),
("castle_151","jing",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_17,0,ai_bhvr_hold,0,(3.1, -12.7),[],45),
("castle_152","zheng",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_17,0,ai_bhvr_hold,0,(-10.3, -13.3),[],30),
("castle_153","yinggu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_17,0,ai_bhvr_hold,0,(15.5, -6.6),[],100),
("castle_154","changge",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_17,0,ai_bhvr_hold,0,(-4.7, 4.9),[],110),
("castle_155","yanling",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_17,0,ai_bhvr_hold,0,(-16.9, 11.1),[],75),
("castle_156","xu",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_17,0,ai_bhvr_hold,0,(-8.1, 12.6),[],95),
("castle_157","yan",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_17,0,ai_bhvr_hold,0,(-12.9, 18.7),[],115),
  ## 【卫国】
  #  2
  #  邶（城）,城濮
  #
("castle_158","bei",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_18,0,ai_bhvr_hold,0,(-7.7, -65.6),[],90),
("castle_159","chengpu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_18,0,ai_bhvr_hold,0,(-31.5, -57.7),[],50),
  ## 【郯国】
  #  3
  #  鄟（城）,鄣（城）
  #
("castle_160","zhuan",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_19,0,ai_bhvr_hold,0,(-91.0, -27.2),[],75),
("castle_161","zhang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_19,0,ai_bhvr_hold,0,(-109.2, -22.7),[],100),
  ## 【莒国】
  #  5
  #  郠,浮来,寿舒,向（城）,纪鄣
  #
("castle_162","geng",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_20,0,ai_bhvr_hold,0,(-93.4, -53.9),[],180),
("castle_163","fulai",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_20,0,ai_bhvr_hold,0,(-95.9, -44.8),[],90),
("castle_164","shoushu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_20,0,ai_bhvr_hold,0,(-105.5, -39.7),[],55),
("castle_165","xiang",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_20,0,ai_bhvr_hold,0,(-96.8, -34.3),[],45),
("castle_166","jizhang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_20,0,ai_bhvr_hold,0,(-107.0, -30.1),[],30),
  ## 【陈国】
  #  4
  #  太康（城）,鹿（城）,郸（城）,项（城）
  #
("castle_167","taikang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_21,0,ai_bhvr_hold,0,(-24.3, -1.3),[],100),
("castle_168","lu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_21,0,ai_bhvr_hold,0,(-39.7, 5.3),[],110),
("castle_169","dan",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_21,0,ai_bhvr_hold,0,(-39.4, 11.9),[],75),
("castle_170","xiang",icon_castle_b|pf_castle, no_menu, pt_none, fac_kingdom_21,0,ai_bhvr_hold,0,(-30.5, 16.4),[],95),
  ## 【徐国】
  #  4
  #  钟吾,吕（城）,泗上,娄林
  #
("castle_171","zhongwu",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_22,0,ai_bhvr_hold,0,(-82.7, -11.5),[],115),
("castle_172","lv",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_22,0,ai_bhvr_hold,0,(-86.7, -5.8),[],90),
("castle_173","sishang",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_22,0,ai_bhvr_hold,0,(-81.6, 5.4),[],235),
("castle_174","loulin",icon_castle_c|pf_castle, no_menu, pt_none, fac_kingdom_22,0,ai_bhvr_hold,0,(-99.9, 1.1),[],45),
  ## 【蔡国】
  #  3
  #  驻马（城）,平舆,新蔡
  #
("castle_175","zhuma",icon_castle_a|pf_castle, no_menu, pt_none, fac_kingdom_23,0,ai_bhvr_hold,0,(-14.4, 23.6),[],15),
("castle_176","pingyu",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_23,0,ai_bhvr_hold,0,(-27.7, 22.1),[],300),
("castle_177","xincai",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_kingdom_23,0,ai_bhvr_hold,0,(-24.4, 26.5),[],280),
## 以下城堡为以后做准备
#
#  ("castle_178","jiang",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.36, -29.92),[],260),
#  ("castle_179","yun",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1, 2),[],260),
#  ("castle_180","yu",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0, 2),[],260),
#  ("castle_181","rui",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.36, -32.92),[],80),
#  ("castle_182","guo",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.36, -33.92),[],260),
#  ("castle_183","dingyang",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 5.98),[],260),
#  ("castle_184","yueyang",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 6.98),[],260),
#  ("castle_185","weinan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 7.98),[],260),
#  ("castle_186","lushi",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 8.98),[],260),
#  ("castle_187","shang",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 9.98),[],280),
#  ("castle_188","jingyang",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 10.98),[],260),
#  ("castle_189","xunyang",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 11.98),[],260),
#  ("castle_190","didao",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 12.98),[],260),
#  ("castle_191","shiyuan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 13.98),[],80),
#  ("castle_192","mianzhu",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 14.98),[],260),
#  ("castle_193","nanzheng",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 15.98),[],260),
#  ("castle_194","linzhao",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 16.98),[],260),
#  ("castle_195","wudu",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.23, 17.98),[],260),
#  ("castle_196","yan",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.13, 37.74),[],260),
#  ("castle_197","shangdao",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.13, 38.74),[],280),
#  ("castle_198","huai",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.13, 39.74),[],260),
#  ("castle_199","tang",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.13, 40.74),[],50),
#  ("castle_200","han",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.13, 41.74),[],75),
#  ("castle_201","yanling",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.13, 42.74),[],100),
#  ("castle_202","taicang",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.13, 43.74),[],180),
#  ("castle_203","zuili",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.13, 44.74),[],90),
#  ("castle_204","hu",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.13, 45.74),[],55),
#  ("castle_205","jiuzi",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0, 1),[],45),
#     Rinimad
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
#  村庄
("village_1", "Yaragar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.9, -3.0),[], 100),
("village_2", "Burglen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.6, -12.7),[], 110),
("village_3", "Azgad",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.6, 11.0),[], 120),
("village_4", "Nomar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.4, 34.4),[], 130),
("village_5", "Kulum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.5, 76.6),[], 170),
("village_6", "Emirin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.8, -28.2),[], 100),
("village_7", "Amere",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.8, -30.7),[], 110),
("village_8", "Haen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.2, 75.0),[], 120),
("village_9", "Buvran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-109.3, -15.1),[], 130),
("village_10","Mechin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.5, 47.7),[], 170),

("village_11","Dusturil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.1, -35.3),[], 100),
("village_12","Emer",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.7, -119.9),[], 110),
("village_13","Nemeja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.7, -7.2),[], 120),
("village_14","Sumbuja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.5, 69.8),[], 130),
("village_15","Ryibelet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.6, 33.2),[], 170),
("village_16","Shapeshte",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139.2, 84.4),[], 170),
("village_17","Mazen",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.3, 51.3),[], 35),
("village_18","Ulburban",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(224.0, 38.0),[], 170),
("village_19","Hanun",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(167.2, 91.6),[], 170),
("village_20","Uslum",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.1, 19.4),[], 170),

("village_21","Bazeck",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(167.0, 61.8),[], 100),
("village_22","Shulus",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(224.2, -52.3),[], 110),
("village_23","Ilvia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.9, -140.6),[], 120),
("village_24","Ruldi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123.8, -179.7),[], 130),
("village_25","Dashbigha",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.3, -52.3),[], 170),
("village_26","Pagundur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.1, -89.5),[], 170),
("village_27","Glunmar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.7, -24.8),[], 170),
("village_28","Tash_Kulun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.8, -50.8),[], 170),
("village_29","Buillin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.9, 53.6),[], 170),

("village_30","Ruvar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.3, 77.3),[], 170),
("village_31","Ambean",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.0, 53.0),[], 100),
("village_32","Tosdhar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.5, -19.2),[], 110),
("village_33","Ruluns",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.8, 40.8),[], 120),
("village_34","Ehlerdah",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.4, -52.1),[], 130),
("village_35","Fearichen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.2, 97.4),[], 170),
("village_36","Jayek",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.2, 98.7),[], 170),
("village_37","Ada_Kulun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.6, -68.1),[], 170),
("village_38","Ibiran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.5, 19.1),[], 170),
("village_39","Reveran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.9, -10.1),[], 170),
("village_40","Saren",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.0, -38.1),[], 170),

("village_41","Dugan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.6, -36.6),[], 100),
("village_42","Dirigh_Aban",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.8, -64.5),[], 110),
("village_43","Zagush",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.4, -77.4),[], 120),
("village_44","Peshmi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.0, -58.5),[], 130),
("village_45","Bulugur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.3, -69.8),[], 170),
("village_46","Fedner",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159.1, -153.9),[], 170),
("village_47","Epeshe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.6, -0.9),[], 170),
("village_48","Veidar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.5, -43.7),[], 170),
("village_49","Tismirr",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.7, -23.6),[], 10),
("village_50","Karindi",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(218.2, 59.4),[], 170),

("village_51","Jelbegi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145.9, 22.1),[], 100),
("village_52","Amashke",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(67.8, -37.3),[], 110),
("village_53","Balanli",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.0, -38.2),[], 120),
("village_54","Chide",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(133.5, -27.0),[], 130),
("village_55","Tadsamesh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.9, 23.5),[], 170),
("village_56","Fenada",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.2, 99.0),[], 170),
("village_57","Ushkuru",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.7, 11.9),[], 170),
("village_58","Vezin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.5, 48.2),[], 170),
("village_59","Dumar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.7, -22.2),[], 170),
("village_60","Tahlberl",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.6, -1.9),[], 170),

("village_61","Aldelen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.8, 92.4),[], 100),
("village_62","Rebache",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.7, 67.1),[], 100),
("village_63","Rduna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.5, 21.5),[], 100),
("village_64","Serindiar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.8, -43.2),[], 100),
("village_65","Iyindah",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.6, -39.5),[], 100),
("village_66","Fisdnar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.6, 78.3),[], 100),
("village_67","Tebandra",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.9, 91.8),[], 100),
("village_68","Ibdeles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.9, -40.2),[], 100),
("village_69","Kwynn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.6, 85.3),[], 100),
("village_70","Dirigsene",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.4, -94.0),[], 100),

("village_71","Tshibtin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.0, -39.0),[], 20),
("village_72","Elberl",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.5, -41.1),[], 60),
("village_73","Chaeza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-156.0, -140.0),[], 55),
("village_74","Ayyike",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.9, 29.9),[], 15),
("village_75","Bhulaban",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(214.0, 104.5),[], 10),
("village_76","Kedelke",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.2, -75.5),[], 35),
("village_77","Rizi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.6, 73.3),[], 160),
("village_78","Sarimish",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.3, -51.7),[], 180),
("village_79","Istiniar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.0, 20.4),[], 0),
("village_80","Vayejeg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.0, 72.2),[], 40),

("village_81","Odasan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.9, 94.2),[], 20),
("village_82","Yalibe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.2, 44.0),[], 60),
("village_83","Gisim",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.8, 78.0),[], 55),
("village_84","Chelez",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.3, 38.7),[], 15),
("village_85","Ismirala",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(153.6, -66.0),[], 10),
("village_86","Slezkh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.3, 35.8),[], 35),
("village_87","Udiniad",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.3, 93.5),[], 160),
("village_88","Tulbuk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.0, -82.5),[], 180),
("village_89","Uhhun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.0, -62.1),[], 0),
("village_90","Jamiche",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.1, -157.1),[], 40),
  ##新建的村庄
("village_91", "Longquanyi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, 6.0),[], 100),
("village_92", "Wulitunxiang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.9, -27.9),[], 110),
("village_93", "Qingshan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.8, -13.8),[], 120),
("village_94", "Shigang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.2, 34.8),[], 130),
("village_95", "Xiadian",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.4, 96.2),[], 170),
("village_96", "Qinglong",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.4, -47.0),[], 100),
("village_97", "Majiaji",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.1, -58.9),[], 110),
("village_98", "Pujiaxiang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159.1, 59.9),[], 120),
("village_99", "Hegu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.3, 40.3),[], 130),
("village_100","Hongqiao",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.3, 32.8),[], 170),

("village_101","Wanghe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.7, -50.3),[], 100),
("village_102","Nanshui",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.3, -173.5),[], 110),
("village_103","Shili",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.9, -0.5),[], 120),
("village_104","Lianhuaqiao",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.8, 59.0),[], 130),
("village_105","Daling",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.8, 68.1),[], 170),
("village_106","Shihe",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.1, 65.3),[], 170),
("village_107","Qishan",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.5, 51.9),[], 35),
("village_108","Longmen",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(184.6, 72.3),[], 170),
("village_109","Xiqiao",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(199.0, 17.7),[], 170),
("village_110","Shuangmiao",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(192.9, 93.7),[], 170),

("village_111","Jiushu",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(192.0, -62.7),[], 100),
("village_112","Jingzhuang",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(183.8, -83.1),[], 110),
("village_113","Nanlou",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.5, -127.0),[], 120),
("village_114","Bali",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.1, -70.3),[], 130),
("village_115","Shuangqiao",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.2, -116.1),[], 170),
("village_116","Shiqiao",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.8, -37.3),[], 170),
("village_117","Gaoqiao",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-138.9, 21.0),[], 170),
("village_118","Jiujing",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.6, -51.1),[], 170),
("village_119","Longhe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.8, 79.8),[], 170),
("village_120","Jiulong",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.0, 76.0),[], 170),
  
("village_121","Gaoshan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.0, 53.0),[], 100),
("village_122","Shunhe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.6, -97.2),[], 110),
("village_123","Jingshan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.0, 42.0),[], 120),
("village_124","Sanmiaoling",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.3, -16.5),[], 130),
("village_125","Shihe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.8, 98.1),[], 170),
("village_126","Xitang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.8, 89.8),[], 170),
("village_127","Shanghe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.2, -85.5),[], 170),
("village_128","Nanyue",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, 25.8),[], 170),
("village_129","Caojiahe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.7, 8.9),[], 170),
("village_130","Liangang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.7, -56.5),[], 170),

("village_131","Shahe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.3, -73.0),[], 100),
("village_132","Xinlou",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.1, -74.4),[], 110),
("village_133","Sanhe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.1, -7.0),[], 120),
  
("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.5, -32.2),[]),
("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.1, -40.1),[]),
("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.8, -40.1),[]),
("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.3, -15.8),[]),
("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.8, -180.6),[]),

("training_ground","Training Ground0",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.5, -88.8),[]),

  # ("training_ground_1", "Training Field",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44,61),[], 100),
  # ("training_ground_2", "Training Field",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38, 81.7),[], 100),
  # ("training_ground_3", "Training Field",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.2, 16),[], 100),
  # ("training_ground_4", "Training Field",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.5 , -80.5),[], 100),
  # ("training_ground_5", "Training Field",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.75, -30.3),[], 100),
  
("training_ground_1", "Training Field1",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.0, 61.0),[], 100),
("training_ground_2", "Training Field2",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.1, 34.9),[], 100),
("training_ground_3", "Training Field3",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(121.7, -39.4),[], 100),
("training_ground_4", "Training Field4",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.7, -57.6),[], 100),
("training_ground_5", "Training Field5",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.1, -5.3),[], 100),


#  bridge_a
  # ("Bridge_1","1",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.56, 59.89),[], 90),
  # ("Bridge_2","2",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.14, 34.13),[], 64),
  # ("Bridge_3","3",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.92, 72.98),[], 10),
  # ("Bridge_4","4",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.94, 67.25),[], 90),
  # ("Bridge_5","5",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.16, 79.18),[], 135),
  # ("Bridge_6","6",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.60, 64.32),[], 120),
  # ("Bridge_7","7",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.47, 43.28),[], 75),
  # ("Bridge_8","8",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.46, 21.19),[], 55),
  # ("Bridge_9","9",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.13, 48.21),[], 60),
  # ("Bridge_10","10",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.05, 54.55),[], 35),
  # ("Bridge_11","11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.85, -41.40),[], 90),
  # ("Bridge_12","12",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.17, 79.57),[], 135),
  # ("Bridge_13","13",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.16, 81.16),[], 90),
  # ("Bridge_14","14",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.88, 78.80),[], 75),
  # ("Bridge_15","15",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.01, -29.60),[], 15),
  # ("looter_spawn_point"   ,"looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
("Bridge_1","1",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.1, -25.9),[], -10),
("Bridge_2","2",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.0, 76.9),[], -30),
("Bridge_3","3",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.7, -105.1),[], 75),
("Bridge_4","4",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.3, 81.6),[], -50),
("Bridge_5","5",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.1, 77.5),[], -45),
("Bridge_6","6",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(195.3, -79.6),[], -40),
("Bridge_7","7",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.8, 27.7),[], -20),
("Bridge_8","8",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.4, 40.0),[], 55),
("Bridge_9","9",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.3, -68.4),[], 55),
("Bridge_10","10",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.0, -61.2),[], 90),
("Bridge_11","11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.0, -81.0),[], 70),
  # ("Bridge_12","12",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.17, 79.57),[], 135),
  # ("Bridge_13","13",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.16, 81.16),[], 90),
  # ("Bridge_14","14",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.88, 78.80),[], 75),
  # ("Bridge_15","15",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.01, -29.60),[], 15),
("looter_spawn_point"   ,"looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26.0, 77.0),[(trp_looter,15,0)]),
("steppe_bandit_spawn_point"  ,"steppe_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(42.0, -73.3),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
("forest_bandit_spawn_point"  ,"forest_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-30.0, 5.5),[(trp_looter,15,0)]),
("mountain_bandit_spawn_point","mountain_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(46.4, 22.4),[(trp_looter,15,0)]),
("sea_raider_spawn_point_1"   ,"sea_raider_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-43.0, 96.0),[(trp_looter,15,0)]),
("sea_raider_spawn_point_2"   ,"sea_raider_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.0, 86.0),[(trp_looter,15,0)]),
 # add extra towns before this point 
("spawn_points_end"                  ,"last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(-1.4, 0.4),[(trp_looter,15,0)]),
]
