#!/usr/bin/python
# -*- coding: utf-8 -*-
from telegram.ext import CommandHandler
from telegram import InputMediaPhoto
import requests
import yaml

owner = "-98881019"
count = "1"
offset = 0


def module_init(gd):
    global channel, token, database
    channel = gd.config["channel"]
    token = gd.config["vk_token"]
    commands = gd.config["commands"]
    database = gd.config["database"]
    for command in commands:
        gd.dp.add_handler(CommandHandler(command, sonyan_post))
    jobQueue = gd.updater.job_queue
    jobQueue.run_repeating(callback=sonyan_post, interval=60, first=0, context="@"+channel, name='RepeatingJob')



def sonyan_post(bot, update):
    with open(database, "r") as datefile:
        date_old = yaml.load(datefile)["date"]
    date = check_post(owner, offset, count, token)
    if date > date_old:
        print("New post!")
        post_link, images = dlpic(owner, offset, count, token)
    else:
        return
    bot.send_media_group(chat_id="@"+channel, media=images)
    data = {"date" : date}
    with open(database, "w") as datefile:
        yaml.dump(data, datefile)


def check_post(owner, offset, count, token):
    wallposts = requests.get("https://api.vk.com/method/wall.get?"+
                            "owner_id="+owner+
                             "&offset="+str(offset)+
                             "&count="+count+
                             "&filter="+owner+
                             "&access_token="+token+
                             "&v=5.60")
    serverjson = wallposts.json()
    date = serverjson["response"]["items"][0]["date"]
    return date


def dlpic(owner, offset, count, token):
    wallposts = requests.get("https://api.vk.com/method/wall.get?"+
                             "owner_id="+owner+
                             "&offset="+str(offset)+
                             "&count="+count+
                             "&filter="+owner+
                             "&access_token="+token+
                             "&v=5.60")
    serverjson = wallposts.json()
    vk_id = serverjson["response"]["items"][0]["id"]
    post_link = "https://vk.com/wall-98881019_"+str(vk_id)
    try:
        attachments = serverjson["response"]["items"][0]["attachments"]
    except:
        return None, None, None, None
    media_list = []
    for i in serverjson["response"]["items"][0]["attachments"]:
        if "photo" not in i:
            continue
        photo = i["photo"]
        link = photo[max((x for x in photo if x.startswith("photo_")), key=lambda x: int(x.split("_")[1]))]
        media = InputMediaPhoto(media=link)
        media_list.append(media)
    return post_link, media_list
