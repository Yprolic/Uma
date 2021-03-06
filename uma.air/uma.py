# -*- encoding=utf8 -*-
__author__ = "prolic"

from airtest.core.api import *

from datetime import datetime

auto_setup(__file__)


SLEEP_TIME = 0.5
USERNAME = "Prolic"
PASSWD = "Prolic123"
SAVE_PATH = "C:\\Users\\prolic\\Desktop\\save_IMG\\"
PACKAGE_NAME = "jp.co.cygames.umamusume"
close = Template(r"tpl1614961930538.png", record_pos=(-0.005, 0.268), resolution=(1441, 3120))
cancel = Template(r"tpl1614962464239.png", record_pos=(-0.212, 0.266), resolution=(1441, 3120))
skip = Template(r"tpl1614963132062.png", record_pos=(0.41, 0.987), resolution=(1441, 3120))
home_menu = Template(r"tpl1614961829797.png", record_pos=(0.422, 1.011), resolution=(1441, 3120))

game_menu = Template(r"tpl1614965649845.png", record_pos=(0.411, -0.99), resolution=(1441, 3120))
# skip = (1308, 2982)
def delete_account():
    home_menu_pos = wait(home_menu,  intervalfunc = lambda : touch((817, 1932)))
    touch(home_menu_pos)
    delete_account_btn = Template(r"tpl1614961887277.png", record_pos=(0.002, 0.544), resolution=(1441, 3120))
    touch(delete_account_btn)
    accept_btn = Template(r"tpl1614962382614.png", record_pos=(0.221, 0.746), resolution=(1441, 3120))
    accept_pos = wait(accept_btn, intervalfunc = lambda : touch((817, 1932)))

def new_account():
    accept_btn = Template(r"tpl1614962382614.png", record_pos=(0.221, 0.746), resolution=(1441, 3120))
    accept_pos = wait(accept_btn, intervalfunc = lambda : touch((755, 1440)))
    cancel_pos = wait(cancel, intervalfunc = lambda : touch(accept_pos))
    touch(cancel_pos)
    sleep(1)
    touch(Template(r"tpl1614962514209.png", record_pos=(-0.222, 0.268), resolution=(1441, 3120)))
    sleep(SLEEP_TIME)
    touch(Template(r"tpl1614962524413.png", record_pos=(0.213, 0.258), resolution=(1441, 3120)))
    sleep(SLEEP_TIME)
    edit_name(USERNAME)
    close_pos = wait(close, timeout = 60, intervalfunc = lambda : touch(skip, 10))
    touch(close_pos, 2)
    go_home()

def edit_name(name):
    touch((755, 1440))
    sleep(SLEEP_TIME)
    text(name,search=True)
    touch((800, 1940), 5)
    sleep(SLEEP_TIME)
    touch((800, 1940), 5)
    
def get_gift():
    gift_btn = Template(r"tpl1614964386722.png", record_pos=(0.405, 0.574), resolution=(1441, 3120))
    
    get_all_pos = wait(Template(r"tpl1614964409220.png", record_pos=(0.219, 0.753), resolution=(1441, 3120)), intervalfunc = lambda : touch(gift_btn))
    touch(get_all_pos)
    
    touch(close)
    go_home()

def gacha(count):
    touch((1290,3000),10)
    sleep(2)
    touch((1360,2104))
#     touch(Template(r"tpl1614964669081.png", record_pos=(0.433, 0.389), resolution=(1441, 3120)), times=2, duration=0.02)
    sleep(SLEEP_TIME)
    gacha10_btn = Template(r"tpl1614964691268.png", record_pos=(0.298, 0.734), resolution=(1441, 3120))
    touch(gacha10_btn)
    touch((1360,1927),10)
    again_btn = Template(r"tpl1614964818138.png", record_pos=(0.213, 0.77), resolution=(1441, 3120))
    for i in range(count - 1):
        again_pos = wait(again_btn, intervalfunc = lambda : touch((1330,3030)))
        touch(again_pos)
        sleep(SLEEP_TIME)
        touch(Template(r"tpl1614964951949.png", record_pos=(0.208, 0.264), resolution=(1441, 3120)))
        sleep(2)
    touch(wait(Template(r"tpl1614966998949.png", record_pos=(-0.223, 0.777), resolution=(1441, 3120)), intervalfunc = lambda : touch((1330,3030))))
    sleep(SLEEP_TIME)


def go_home():
    for i in range(5):
        touch((730,3000),10)
        sleep(0.2)
    
def save_ssr(account_id):
    support_btn = Template(r"tpl1614965234773.png", record_pos=(0.203, 0.491), resolution=(1441, 3120))
    support_pos = wait(support_btn, intervalfunc = lambda : touch((160,3000),10))
    touch(support_pos)
    touch(Template(r"tpl1614965253553.png", record_pos=(-0.204, 0.666), resolution=(1441, 3120)))
    touch(Template(r"tpl1614965279014.png", record_pos=(0.19, 0.666), resolution=(1441, 3120)))
    touch(Template(r"tpl1614965298276.png", record_pos=(0.211, -0.7), resolution=(1441, 3120)))
    touch(Template(r"tpl1614965314215.png", record_pos=(0.274, -0.511), resolution=(1441, 3120)))
    touch(Template(r"tpl1614965321459.png", record_pos=(0.213, 0.752), resolution=(1441, 3120)))
    sleep(2)
    snapshot(SAVE_PATH + str(account_id) + ".png")
    go_home()
def save_account(account_id):
    
    touch(game_menu)
    sleep(SLEEP_TIME)
    touch((1000,1950),10)
    touch((1200,1750),2)
    touch(Template(r"tpl1614965857489.png", record_pos=(0.218, 0.27), resolution=(1441, 3120)))
    set_passwd(PASSWD)
    sleep(2)
    snapshot(SAVE_PATH + str(account_id) + "_id.png")
    go_home()

def set_passwd(passwd):
    touch((740,1370))
    text(passwd,search=True)
    touch((740,1000))
    sleep(SLEEP_TIME)
    touch((740,1620))
    text(passwd,search=True)
    touch((740,1000))
    sleep(SLEEP_TIME)
    touch((350,1900))
    touch((1000,2100))
    
def logout():
    touch(game_menu)
    touch(Template(r"tpl1614966480991.png", record_pos=(0.223, 0.561), resolution=(1441, 3120)))
    wait(home_menu)


start_app(PACKAGE_NAME)

while True:
    try:
        sleep(2)
        account_id = datetime.now().strftime("%m%d%H%M")
        delete_account()
        new_account()
        get_gift()
        gacha(5)
        save_ssr(account_id)
        save_account(account_id)
        logout()
    except:
        stop_app(PACKAGE_NAME)
        start_app(PACKAGE_NAME)

