import pyautogui

import pyocr
import pyocr.builders
from PIL import Image
import sys


def main():
    # screenShot()

    getText()


def screenShot():
    sc = pyautogui.screenshot(region=(100, 200, 800, 1400))
    sc.save('tempImg/test.png')


def getText():
    tools = pyocr.get_available_tools()
    tool = tools[0]
    langs = tool.get_available_languages()
    txt = tool.image_to_string(
        Image.open('tempImg/aa.png'),
        lang='eng',
        builder=pyocr.builders.TextBuilder()
    )
    print(txt)


main()
