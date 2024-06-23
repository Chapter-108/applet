from wxauto import *
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')

while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())
    if time_now == "17:45:00":
        wx = WeChat()
        msg = '??'.encode('utf-8').decode('utf-8')
        wx.SendMsg('ÎÞµÐ´òÀ×', msg)
        time.sleep(1)
