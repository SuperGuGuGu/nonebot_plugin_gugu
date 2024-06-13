# coding=utf-8
import os
import re
import sqlite3
import time
from nonebot.plugin import PluginMetadata


# 插件元信息，让nonebot读取到这个插件是干嘛的
__plugin_meta__ = PluginMetadata(
    name="gugu",
    description="gugu插件",
    usage="/帮助",
    type="application",
    homepage="https://github.com/SuperGuGuGu/nonebot_plugin_gugu",
)

print("ping")
