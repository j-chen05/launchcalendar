"""
main driver for program
"""

from gcal import Gcal

cal_handler = Gcal()

cal_handler.authorize()
cal_handler.ten_events()
