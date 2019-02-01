# coding=utf-8

import  random
from base_data import *


#剧本路径（指定要修改的剧本位置）
modpath = r"C:\Users\Administrator\Desktop\mb_module_system_1010_0\ModuleSystem"
# # 国家相关的数据信息
# # 主要的配置信息,默认规则请参看：factions_descript（在本文件最后）
factions=[
    {
        "fac_id":"kingdom_1",
        "fac_name":"Kingdom of Swadia",
        "color":"0xDD8844",
        "king":swadian_kings,
        "pretender":swadian_pretender,
        "lords":swadian_lords,
        "lord_items":swadian_lords[random.randint(0,len(swadian_lords)-1)]["items"],
        "lord_max_num":20,
        "troops":swadian_troops,
        "upgradeKingdom":swadian_upgrade,
    },
    {
        "fac_id":"kingdom_2",
        "fac_name":"Kingdom of Vaegirs",
        "color":"0x33DD33",
        "king":vaegir_kings,
        "pretender":vaegir_pretender,
        "lords":vaegir_lords,
        "lord_items":vaegir_lords[random.randint(0,len(vaegir_lords)-1)]["items"],
        "lord_max_num":20,
        "troops":vaegir_troops,
        "upgradeKingdom":vaegir_upgrade,
    },
    {
        "fac_id":"kingdom_3",
        "fac_name":"Khergit Khanate",
        "color":"0xCC99FF",
        "king":khergit_kings,
        "pretender":khergit_pretender,
        "lords":khergit_lords,
        "lord_items":khergit_lords[random.randint(0,len(khergit_lords)-1)]["items"],
        "lord_max_num":20,
        "troops":khergit_troops,
        "upgradeKingdom":khergit_upgrade,
        "wifes":ladies_wifes,
        "daughters":ladies_daughters
    },
    {
        "fac_id": "kingdom_4",
        "fac_name": "Kingdom of Nords",
        "color": "0xDDDD33",
        "king": nord_kings,
        "pretender":nord_pretender,
        "lords": nord_lords,
        "lord_items": nord_lords[random.randint(0, len(nord_lords) - 1)]["items"],
        "lord_max_num": 20,
        "troops": nord_troops,
        "upgradeKingdom": nord_upgrade,
    },
    {
        "fac_id": "kingdom_5",
        "fac_name": "Kingdom of Rhodoks",
        "color": "0x33DDDD",
        "king": rhodok_kings,
        "pretender":rhodok_pretender,
        "lords": rhodok_lords,
        "lord_items": rhodok_lords[random.randint(0, len(rhodok_lords) - 1)]["items"],
        "lord_max_num": 20,
        "troops": rhodok_troops,
        "upgradeKingdom": rhodok_upgrade,
    },
    {
        "fac_id": "kingdom_6",
        "fac_name": "Kingdom of test",
        "color": "0x33FFDD",
        "king": rhodok_kings,
        "pretender":rhodok_pretender,
        "lords": rhodok_lords,
        "lord_items": rhodok_lords[random.randint(0, len(rhodok_lords) - 1)]["items"],
        "lord_max_num": 20,
        "troops": rhodok_troops,
        "autoTroops":["infantry1","archer3","crossbowman"],
        "upgradeKingdom": rhodok_upgrade,
    }
]

## 如果用户没有提供，就使用以下默认值（不了解代码，不要修改此内容）
default_faction={
    #为系统自动生成提供默认值
    "king":[
        swadian_kings[0],
        vaegir_kings[0],
        nord_kings[0],
        rhodok_kings[0],
        khergit_kings[0]
    ],
    "pretender":[
        swadian_pretender[0],
        vaegir_pretender[0],
        nord_pretender[0],
        rhodok_pretender[0],
        khergit_pretender[0]
    ],
    #为系统自动生成提供默认值
    "lords":swadian_lords,
    # 为系统自动生成提供默认值
    "wifes":ladies_wifes,
    # 为系统自动生成提供默认值
    "daughters": ladies_daughters,
    # 用户可以在这里自定义英雄
    "heros":[],
    # 每一个国家领主最大数量
    "lord_max_num":20,
    #每一个国家妻子的最大个数
    "wife_max_num":0,
    #每一个国家女儿的最大个数
    "daughter_max_num":0,
    #
    "ladiesItems":ladies_daughters[random.randint(0,len(ladies_daughters)-1)]["items"],
    "default_lady":ladies_daughters[random.randint(0,len(ladies_daughters)-1)],
    "troops":swadian_troops,
    #兵种升级关系(国家兵种),由于国家兵种Id可能随机生成，所以使用编号
    "upgradeKingdom":[
        [1,2,3],
        [2,4],
        [4,5],
        [3,6],
        [6,7],
    ],
    #兵种升级关系（非国家兵种）
    "upgradeOther":[],
    "troop_max_num":14
}


#这个配置没有作用，只是起到解释作用
#各个参数说明信息
factions_descript=[
        {
        #阵营id（使用kingdom_编号）,如果不提供，格式：kingdom_编号
        "fac_id":"kingdom_%",
        #阵营名称（默认使用阵营id）,如果不提供，格式：kingdom_编号
        "fac_name":"kingdom_%",
        #阵营颜色(默认随机产生)，如果不提供，随机产生
        "color":"0xDD8844",
        ## 和领主属性一样的用法
        "king":{
                #领主id（自动生成的领主规则：阵营id_knight_序号）
                "id":"knight_1_1",
                #领主名字（自动生成时采用领主id）
                "lord_name":"Lord Klargus",
                #领主的标识信息
                "flag":"tf_hero",
                #领主拥有装备(不提供时使用lord_items)
                "items":[
                    "itm_saddle_horse",
                    "itm_courtly_outfit",
                    "itm_heraldic_mail_with_surcoat",
                    "itm_nomad_boots",
                    "itm_splinted_greaves",
                    "itm_great_helmet",
                    "itm_sword_medieval_c",
                    "itm_scale_gauntlets",
                    "itm_tab_shield_heater_cav_a"
                ],
                #领主属性
                "attr":"knight_attrib_1",
                #领主武器熟练度
                "wp":"wp(130)",
                #领主技能
                "skill":"knight_skills_1|knows_trainer_1|knows_trainer_3",
                #领主容貌
                "face":"0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000"
        },
        #领主信息（指定领主的详细信息，如果不指定，20个领主全部自动生成，自动生成的属性信息会先从指定的领主中随机找一个，
        # 如果20个领主一个都没有提供，就会参照default_faction中的lords属性）
        "lords":[
            {
                #领主id（自动生成的领主规则：阵营id_knight_序号）
                "id":"knight_1_1",
                #领主名字（自动生成时采用领主id）
                "lord_name":"Lord Klargus",
                #领主的标识信息
                "flag":"tf_hero",
                #领主拥有装备(不提供时使用lord_items)
                "items":[
                    "itm_saddle_horse",
                    "itm_courtly_outfit",
                    "itm_heraldic_mail_with_surcoat",
                    "itm_nomad_boots",
                    "itm_splinted_greaves",
                    "itm_great_helmet",
                    "itm_sword_medieval_c",
                    "itm_scale_gauntlets",
                    "itm_tab_shield_heater_cav_a"
                ],
                #领主属性
                "attr":"knight_attrib_1",
                #领主武器熟练度
                "wp":"wp(130)",
                #领主技能
                "skill":"knight_skills_1|knows_trainer_1|knows_trainer_3",
                #领主容貌
                "face":"0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000"
            }
        ],
        #为所有的领主统一设定装备(优先使用每一个领主自己装备,如果该领主没有提供,就使用该属性提供的装备)
        "lord_items":[],
        #领主最大个数（默认20个），自动生成领主的个数=lord_max_num-len(lords)
        "lord_max_num":20,
        #领主的妻子们
        "wifes":[],
        #领主的女儿们
        "daughters":[],
        #兵种信息（兵种的个数由troop_max_num属性来决定，在troops中配置的个数比troop_max_num多的兵种将会被忽略）
        "troops":[
            {
                #兵种id(如果不提供，格式：阵营编号_troop_编号)
                "id":"swadian_recruit",
                #兵种名称(如果不提供，格式：阵营编号_troop_编号)
                "troop_name":"Swadian Recruit",
                #兵种的标识（如果不提供，默认）
                "flag":"tf_mounted|tf_guarantee_boots|tf_guarantee_armor",
                #兵种装备（会使用factions_default中troops中与当前兵种对应的装备，用户指定的兵种过多，会导致该兵种没有装备）
                "items":[
                    "itm_scythe",
                    "itm_hatchet",
                    "itm_pickaxe",
                    "itm_club",
                    "itm_stones",
                    "itm_tab_shield_heater_a",
                    "itm_leather_cap",
                    "itm_felt_hat",
                    "itm_felt_hat",
                    "itm_shirt",
                    "itm_coarse_tunic",
                    "itm_leather_apron",
                    "itm_nomad_boots",
                    "itm_wrapping_boots"
                ],
                #兵种属性
                "attr":"def_attrib|level(4)",
                #兵种武器熟练度
                "wp":"wp(60)",
                #兵种技能
                "skill":"knows_common",
                #面容1
                "face1":"swadian_face_younger_1",
                #面容2
                "face2":"swadian_face_middle_2"
            }
        ],
        #通过兵种模板生成兵种信息(模板参照data_troop.py文件)
        "autoTroops":["infantry1",""],
        #该国家最多拥有兵种的个数
        "troop_max_num":14,
        #兵种升级关系(国家兵种),由于国家兵种Id可能随机生成，所以使用编号
        "upgradeKingdom":[
            #国家第一个兵种，可以升级成第二个和第三兵种
            [1,2,3],
            #国家第二个兵种，可以升级成第四个兵种
            [2,4],
            #国家第四个兵种，可以升级成第五个兵种
            [4,5],
            #国家第三个兵种，可以升级成第六个兵种
            [3,6],
            #国家第六个兵种，可以升级成第七个兵种
            [6,7],
        ],
        #兵种升级关系（非国家兵种）
        "upgradeOther":[
            ["farmer","watchman"],
            ["watchman","caravan_guard","mercenary_crossbowman"],
        ],
    }
]