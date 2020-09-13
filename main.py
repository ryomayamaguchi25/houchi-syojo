import getParameter as gp
import time


def main():
    print('main')

    # ボタンの場所などを確認
    gp.getParameter()

    # ウィンドウのアクティブ化
    gp.clickLeft()

    for i in range(500):
        print('---------------------------')

        # C級育成
        gp.clickLeft()

        gp.getSS()

        gp.getText()


main()
