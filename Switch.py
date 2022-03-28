import os
import shutil
import easygui
path_config = "" #这里塞放原神客户端的配置文件的文件夹
free_config = "C:\\Program Files"
with open("config.ini",'r',encoding='utf-8') as myConfig:
    myConfigLine = myConfig.readlines()
    for i in myConfigLine:
        if("GenshinConfig" in i):
            cut = i.split(" ")
            path_config = cut[2]
        if("FreeConfig" in i):
            cut = i.split(" ")
            free_config

if(os.path.exists(free_config)):
    os.remove(free_config)
if(easygui.ccbox(msg='选择游玩服务器',title='Genshin impact Switch',choices=('官服','B服'))):
    with open(path_config, encoding='utf-8') as switch:
        line = switch.readlines()
        flag = 0
        for i in line:
            if (i == "channel=14\n"):
                i = "channel=1\n"
                line[flag] = i
            if (i == "cps=bilibili\n"):
                i = "cps=mihayou\n"
                line[flag] = i
            if (i == "sub_channel=0\n"):
                i = "sub_channel=1\n"
                line[flag] = i
            flag = flag + 1
        with open(free_config,'a',encoding='utf-8')as final_file:
            for z in line:
                final_file.write(z)
        shutil.copy(free_config,path_config)
        os.remove(free_config)
        easygui.msgbox("B服转官服完成")
else:
    with open(path_config, encoding='utf-8') as switch:
        line = switch.readlines()
        flag = 0
        for i in line:
            if (i == "channel=1\n"):
                i = "channel=14\n"
                line[flag] = i
            if (i == "cps=mihayou\n"):
                i = "cps=bilibili\n"
                line[flag] = i
            if (i == "sub_channel=1\n"):
                i = "sub_channel=0\n"
                line[flag] = i
            flag = flag + 1
        with open(free_config,'a',encoding='utf-8')as final_file:
            for z in line:
                final_file.write(z)
        shutil.copy(free_config,path_config)
        os.remove(free_config)
        easygui.msgbox("官服转B服完成")