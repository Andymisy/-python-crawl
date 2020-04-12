from fontTools.ttLib import TTFont
#解析的字体文件
font_1 = TTFont(r'D:\chorm download\font\douyin.ttf')
font_1.saveXML(r'D:\chorm download\font\font_1.xml')