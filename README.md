# 战国群雄（Heros-of-Warring-States）
## 剧本信息

这是一个关于春秋战国骑马与砍杀的Mod

## 剧本工具使用说明 

​	剧本工具可以快速，大量生成（阵营，国王，领主，兵种，部队模板等信息）,通过最少的配置,完成复杂多样的剧本修改。

### 第一步：设置标签

​	为了能够让该系统修改你的剧本，你需要配置本系统能够修改的位置，为了能够让系统修改你的剧本，必须要告诉系统，修改的开始位置和结束位置，使用以下标签来标注修改的位置

- 阵营标签：【#faction start】和【#faction end】
- 国王标签：【#king start】和【#king end】
- 文化标签：【#culture start】和【#culture end】
- 领主标签：【#lord start】和【#lord end】
- 兵种标签：【#troop start】和【#troop end】
- 部队模板标签：【#party templates start】和【#party templates end】

```python
#修改文化标签的例子
#culture start
("culture_1",  "culture_1", 0, 0.9, [], []),
("culture_2",  "culture_2", 0, 0.9, [], []),
("culture_3",  "culture_3", 0, 0.9, [], []),
("culture_4",  "culture_4", 0, 0.9, [], []),
("culture_5",  "culture_5", 0, 0.9, [], []),
#culture end

#当使用开始和结束标签标注以后，标签之间的内容会在系统运行时全部【删除】，之后【重新生成】,所以不要将你重要的信息写在在两个标签之间。当你将这些标签加入到剧本的任何位置，这些位置里面的内容全部都会被本工具所管理，这些数据会由本工具根据配置文件自动生成。
```

**注：标签要独占一行，标签前面不能有任何字符，包含空格，也就是#必须是这一行第一个字符。**

### 第二步：指定MOD路径

在config.py文件中

```python
#剧本路径（指定要修改的剧本位置）
modpath = r"C:\Users\Administrator\Desktop\mb_module_system_1010_0\ModuleSystem"
```

### 第三步：配置阵营相关信息

在config.py文件中

```python
# 国家相关的数据信息
# 该配置文件的具体含义请参看config.py文件
factions=[
    {
        "fac_id":"kingdom_1",
        "fac_name":"Kingdom of Swadia",
        "color":"0xDD8844",
        "king":swadian_kings[0],
        "lords":swadian_lords,
        "lord_items":swadian_lords[random.randint(0,len(swadian_lords)-1)]["items"],
        "lord_max_num":20,
        "troops":swadian_troops,
    },
    {
        "fac_id":"kingdom_2",
        "fac_name":"Kingdom of Vaegirs",
        "color":"0x33DD33",
        "king":vaegir_kings[0],
        "lords":vaegir_lords,
        "lord_items":vaegir_lords[random.randint(0,len(vaegir_lords)-1)]["items"],
        "lord_max_num":20,
        "troops":vaegir_troops,
    },
    {
        "fac_id":"kingdom_3",
        "fac_name":"Khergit Khanate",
        "color":"0xCC99FF",
        "king":khergit_kings[0],
        "lords":khergit_lords,
        "lord_items":khergit_lords[random.randint(0,len(khergit_lords)-1)]["items"],
        "lord_max_num":20,
        "troops":khergit_troops,
    },
    {
        "fac_id":"kingdom_4",
        "fac_name": "Kingdom of Nords",
        "color": "0xDDDD33",
        "king":nord_kings[0],
        "lords": nord_lords,
        "lord_items": nord_lords[random.randint(0, len(nord_lords) - 1)]["items"],
        "lord_max_num": 20,
        "troops": nord_troops,
    },
    {
        "fac_id":"kingdom_5",
        "fac_name": "Kingdom of Rhodoks",
        "color": "0x33DDDD",
        "king":rhodok_kings[0],
        "lords": rhodok_lords,
        "lord_items": rhodok_lords[random.randint(0, len(rhodok_lords) - 1)]["items"],
        "lord_max_num": 20,
        "troops": rhodok_troops,
    },
]
#以上内容，也可以写得像下面一样简单，同样也会生成5个国家，以及5个国家对应的国王，文化，领主，兵种，和队伍模板，只是里面的数据会按照一些简单的规则生成（如：国名和人名等），有一些信息会随机生成（装备，武器熟练度，颜色，容貌等）。
factions=[{},{},{},{},{},]
#当然如果你只希望其中一部分自动生成，那只需要添加你不想要自动生成的属性就可以了，如：
factions=[
    {
        "fac_name":"Kingdom of Swadia",
        "color":"0xDD8844",
    },
    {
        "lords":vaegir_lords,
        "color":"0x33DD33",
    },
    {
        "fac_id":"kingdom_3",
        "color":"0xCC99FF",
    },
    {
        "king":nord_kings[0],
    },
    {
        "lord_max_num": 20,
        "color": "0x33DDDD",
    },
]

```

### 第四步：运行工具

​	运行run.py文件就可以了。再查看你的剧本，是不是已经被修改了

### 第五步：出现错误

 - **未修改文件**：没有配置第一步
 - **文件没有找到**:没有有配置第二步，或者配置文件路径有问题
 - **写入文件时出错**：说明文件正在使用，或者文件是只读等等错误