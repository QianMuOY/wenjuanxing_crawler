# -*- coding: utf-8-*-
import random
import Sojump
from Sojump import Wenjuanxing, text_library, answer_14
import schedule as schedule

url = 'https://www.wjx.cn/vm/O6xfX8f.aspx'
wenjuanxing = Wenjuanxing(url)

def run():
    # 计数器
    wenjuanxing.counter()
    # 伪装selenium
    wenjuanxing.weizhuang_selenium()
    # 问卷题目
    wenjuanxing.danxuan(1)
    wenjuanxing.fixed_danxuan(2, 2)
    wenjuanxing.excluded_danxuan(3, 3, flag=2)
    wenjuanxing.fixed_danxuan(4, 4, flag=2)
    wenjuanxing.fixed_danxuan(5, 2, flag=2)
    # r = wenjuanxing.danxuan(6, flag=2)
    # if r == 1:
    #     wenjuanxing.text('7', 2, 1)
    #     wenjuanxing.text('7', 4, 1)
    #     wenjuanxing.text('7', 6, 0)
    wenjuanxing.fixed_danxuan(6, 2, flag=2)
    wenjuanxing.fixed_danxuan(8, 1, flag=2)
    wenjuanxing.fixed_kuangxuan(2)
    wenjuanxing.excluded_danxuan(10, 4, 5, flag=2)
    wenjuanxing.excluded_danxuan(11, 4, 5, flag=2)
    wenjuanxing.fixed_danxuan(12, 1, flag=2)
    wenjuanxing.excluded_duoxuan(13, 6, 7, flag=2)
    wenjuanxing.fixed_matrix(14, 8, answer_14)
    r = wenjuanxing.excluded_danxuan(15, 4, 5, flag=2)
    # print(r)
    if r == 1:
        try:
            wenjuanxing.excluded_danxuan(16, 5, 6, 7, flag=2)
        except Exception as r:
            print("error in", r)
            print("可能为16题的错误显示")
    else:
        # wenjuanxing.click_submit()
        # wenjuanxing.excluded_danxuan(16, 6, 7, flag=2)
        try:
            wenjuanxing.excluded_danxuan(16, 5, 6, 7, flag=2)
        except Exception as r:
            print(r, '16题未显示')
        rr = 0
        try:
            wenjuanxing.click_submit()
            wenjuanxing.fixed_danxuan(17, 2, flag=2)
            rr = wenjuanxing.danxuan(18, flag=2)
            wenjuanxing.fixed_danxuan(19, 2, flag=2)
        except Exception as r:
            print("error in", r)
            print("可能为17、18、19题的错误显示")
        # wenjuanxing.click_submit()
        # wenjuanxing.danxuan(19, flag=2)
        if rr == 2:
            try:
                wenjuanxing.restrictive_danxuan(20, 1, 3, flag=2)
            except Exception as r:
                print(r)
                print("20题显示错误")

    wenjuanxing.fixed_danxuan(21, 2, flag=2)
    # wenjuanxing.excluded_duoxuan(22, 3, 5, 6, flag=2)
    wenjuanxing.fixed_s_matrix(23, 3, 4, 5)
    r = wenjuanxing.fixed_danxuan(24, 2, flag=2)
    if r == 1:
        wenjuanxing.excluded_duoxuan(26, 9, 10, flag=2)
    else:
        wenjuanxing.fixed_danxuan(25, 1, flag=2)
    wenjuanxing.excluded_danxuan(27, 1, 3, flag=2)
    r = wenjuanxing.excluded_danxuan(28, 1, 4, 5, flag=2)
    if r == 4 or r == 5:
        wenjuanxing.excluded_duoxuan(29, 4, 5, flag=2)
    wenjuanxing.fixed_danxuan(30, 3, flag=2)
    wenjuanxing.excluded_duoxuan(31, 3, 4, 5,  6, 7, flag=2)
    wenjuanxing.excluded_duoxuan(32, 2, 3, 4, 5, 6, flag=2)
    # time.sleep(3)
    # 提交问卷
    wenjuanxing.submit()

if __name__ == '__main__':
    # 每隔2秒运行
    schedule.every(2).seconds.do(run)
    # 判断条件
    while Sojump.count < 50:
        schedule.run_pending()

