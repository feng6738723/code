"""
1.声明一个电脑类：
属性：品牌、颜色、内存大小
方法：打游戏、写代码、看视频

a.创建电脑类的对象，然后通过对象点的方式获取、修改、添加和删除它的属性
b.通过attr相关方法去获取、修改、添加和删除它的属性
"""


class Computer(object):
    """电脑类"""

    __slots__ = ('brand', 'color', 'memory', 'name')

    # 构造方法（创建类的对象的时候会自动init方法去初始化对象的属性）
    def __init__(self, brand='', color='', memory=0):
        self.brand = brand
        self.color = color
        self.memory = memory

    def play_game(self):
        print('可以打游戏')

    def coding(self):
        print('可以写python程序')

    def watch_tv(self):
        print('可以看视频')


computer1 = Computer('联想', 'black', '500G')
print(computer1.brand)
computer1.brand = '戴尔'
computer1.name = 'yuting'
del computer1.name

print(getattr(computer1, 'brand'))
setattr(computer1, 'color', 'red')
print(getattr(computer1, 'color'))
setattr(computer1, 'name', 'zhangsan')
delattr(computer1, 'color')
# print(getattr(computer1, 'color'))












