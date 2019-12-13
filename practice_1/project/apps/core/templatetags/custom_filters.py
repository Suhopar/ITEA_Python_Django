import random
from django import template

register = template.Library()


# @register.filter
# def phone_format(value):
#     return f'+{value[:2]} ({value[2:5]}) {value[5:8]} {value[8:10]} {value[10:]}'


@register.filter
def semicolon(value):
    return value + ';'


@register.filter
def text_emoji(value):
    emoji_list = ['(─‿‿─)', '(ง ͠° ͟ل͜ ͡°)ง', 'ಠ╭╮ಠ', '(づ￣ ³￣)づ', 'ಠ‿↼',
                  '( ⚆ _ ⚆ )', '(>_<)', '(¬_¬)', '(⁎˃ᆺ˂)', '(͡ ͡° ͜ つ ͡͡°)']
    # return value+'  Random emoji: '+emoji_list[random.randint(0, 9)]
    return value+'  '+emoji_list[random.randint(0, 9)]

