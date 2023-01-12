# -*- coding:utf-8 -*-
# encoding:utf-8
import kivy
import os
from kivy.resources import resource_add_path, resource_find

resource_add_path(os.path.abspath('res/fonts/'))
from kivy.core.text import LabelBase

LabelBase.register('Roboto', 'PingFangSC-Thin.otf')
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button


class ButtonApp(App):
    def build(self):
        btn = Button(text="这是一个按钮",  # 文本
                     font_size="20sp",  # 字体大小
                     background_color=(255, 255, 255, 1),  # 背景颜色
                     color=(102, 204, 255, 1),  # 字体颜色
                     # size =(500, 500),                    # 绝对大小，当size_hint=(None,None)时生效
                     size_hint=(0.3, 0.3),  # 相对大小，相对于窗口的比例大小
                     pos=(500, 500),  # 绝对坐标
                     )
        return btn


print("测试")
root = ButtonApp()
root.run()
