#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
from PIL import Image
from pylab import *

'''
    ginput(*args, **kwargs) 函数就可以实现交互式标注(首先绘制一幅图像，然后等待用户在绘图窗口的图像区域点击次数。程序将这些点击的坐标 [x, y] 自动保存在 x 列表里)

'''

if __name__ == '__main__':
    im = array(Image.open("./img/test.jpg"))

    imshow(im)

    x = ginput(3)

    print 'you clicked:', x

    show()