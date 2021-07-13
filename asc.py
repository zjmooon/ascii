from PTL import Image
import argparse
parser = argparse.ArgumentParser()

#定义输入文件、输出文件、输出字符画的宽和高
parser.add_arugument('file')
parser.add_arugument('-o','--output')
parser.add_arugument('--width', type = int, default = 80)
parser.add_arugument('--height', type = int, default = 80)

#解析并获取参数
args = parser.parse_args()

#输入的图片文件途径
IMG = args.file

#输出字符画宽度
WIDTH = args.width

#输出字符画高度
HEIGHT = args.height

#输出字符画的路径
OUTPUT = args.output
