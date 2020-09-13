# import screenShot as ss
import pyautogui
import cv2
import pyocr
import pyocr.builders
from PIL import Image
import sys
import time


preParamImg = 'tempImg/preParamImg.png'
paramImg = 'tempImg/paramImg.png'
preStatusTop = 0
preStatusBottom = 0
statusTop = 0
statusBottom = 0
preTop = 0
height = 0

btnLeft = 0
btnRight = 0


def test():
    preStatusTop = pyautogui.screenshot(region=(275, 1373, 276, 40))
    preStatusTop.save('test.png')
    pyautogui.click(250, 400)
    pyautogui.click(250, 400)

    pyautogui.click(250, 400)


def getParameter():

    global preStatusTop
    global preStatusBottom
    global statusTop
    global statusBottom
    global preTop
    global height
    global btnLeft
    global btnRight

    preStatusTop = pyautogui.locateOnScreen(
        'refImg/preStatusTop.png', region=(0, 0, 1000, 1500), confidence=0.8)

    preStatusBottom = pyautogui.locateOnScreen(
        'refImg/preStatusBottom.png', region=(0, 0, 1500, 1500), confidence=0.8)

    statusTop = pyautogui.locateOnScreen(
        'refImg/statusTop.png', region=(0, 0, 1000, 1500), confidence=0.8)

    statusBottom = pyautogui.locateOnScreen(
        'refImg/statusBottom.png', region=(0, 0, 1500, 1500), confidence=0.8)

    preTop = preStatusTop.top + preStatusTop.height
    height = statusBottom.top - preTop

    btnLeft = pyautogui.locateOnScreen(
        'refImg/btnLeft.png', region=(0, 0, 1500, 3000), confidence=0.8)

    btnRight = pyautogui.locateOnScreen(
        'refImg/btnRight.png', region=(0, 0, 1500, 3000), confidence=0.8)


def clickLeft():
    btnLeftX, btnLeftY = pyautogui.center(btnLeft)
    pyautogui.click(btnLeftX / 2, btnLeftY / 2)  # retinaDesiplayは/2
    time.sleep(1)


def clickRight():
    btnRightX, btnRightY = pyautogui.center(btnRight)
    pyautogui.click(btnRightX/2, btnRightY/2)  # retinaDesiplayは/2
    time.sleep(1)


def getSS():
    preSc = pyautogui.screenshot(
        region=(preStatusTop.left, preTop, preStatusTop.width, height))
    sc = pyautogui.screenshot(
        region=(statusTop.left, preTop, statusTop.width, height))

    preSc.save(preParamImg)
    sc.save(paramImg)
    # time.sleep(1)


def getText():
    tools = pyocr.get_available_tools()
    tool = tools[0]
    langs = tool.get_available_languages()
    param = tool.image_to_string(
        Image.open(paramImg),
        lang='eng',
        builder=pyocr.builders.DigitBuilder()
    ).split()
    preParam = tool.image_to_string(
        Image.open(preParamImg),
        lang='eng',
        builder=pyocr.builders.DigitBuilder()
    ).split()

    while (len(param) != 4):
        time.sleep(0.3)
        print('成長後のステが取れなかったのでもう一度')
        getSS()
        param = tool.image_to_string(
            Image.open(paramImg),
            lang='eng',
            builder=pyocr.builders.DigitBuilder()
        ).split()

    print(preParam)
    print(param)

    strength = int(param[0]) - int(preParam[0])
    agile = int(param[1]) - int(preParam[1])
    inte = int(param[2]) - int(preParam[2])
    physical = int(param[3]) - int(preParam[3])
    total = strength * 4 + physical * 3 + agile + inte

    print(total)
    if (total >= 0):
        print(total)
        print('保存')
        clickRight()

        # 結果が表示される。邪魔なので3秒待つ。
        time.sleep(3)

    else:
        print(total)
        print('閉じる')
        clickLeft()


def gray():
    # original
    img = cv2.imread(paramImgPath)
    # gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # threshold
    th = 180
    img = cv2.threshold(
        img, th, 255, cv2.THRESH_BINARY
    )[1]

    # img = cv2.bitwise_not(img)

    cv2.imwrite(paramImgPath, img)


# test()
# getParameter()
# getSS()
# gray()

# getText()
