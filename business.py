import time
import datetime
import config as cfg
import util as u
import service

def execute_action_configurated():
    if not check_action_already_performed_today():
        #print("check_action_already_performed_today", check_action_already_performed_today())
        if cfg.read_config_strategy() == 1: #strategy = 1 - IMPROVE, considering days even and odds
            print("strategy = 1")
            if not check_for_low_rewards():
                #print("check_for_low_rewards", check_for_low_rewards())
                if (u.get_current_day() % 2) == 0: #even
                    print("roll")
                    service.roll()
                else:
                    print("withdraw")
                    service.withdraw()
                update_action_performed()

def update_action_performed():
    print("update_action_performed")
    file = open('data.txt', "w")
    file.write(datetime.datetime.now().strftime("%Y%m%d") + " Y")

def action_already_performed_today():
    print("action_already_performed_today")
    data = open('data.txt', "r").readline()
    current_date = data[0:8]
    action_was_performed = data[9:10]
    # print('current_date', current_date)
    # print('now', datetime.datetime.now().strftime("%Y%m%d"))
    # print('action_was_performed', action_was_performed)
    if current_date == datetime.datetime.now().strftime("%Y%m%d"):
        # print(f'The current data is the same in the file')
        if action_was_performed == "Y":
            #print(f'The action was already performed today')
            return True
    else:
        return False

def check_action_already_performed_today():
    print("check_action_already_performed_today")
    # print(f'Current hour is:', u.get_current_time_of_the_day())
    # print(f'Current hour configurated is:', cfg.read_config_transaction_time())
    if u.get_current_time_of_the_day() >= cfg.read_config_transaction_time():
        if action_already_performed_today():
            print('The action scheduled for today was already performed.')
            return True
        else:
            print('The action WAS NOT PERFORMED today')
            return False
        # print(f'Current hour is equal or bigger than configurated')
    else:
        print('Current hour is lower than configurated')
        return True

def check_for_low_rewards():
    print("check_for_low_rewards")
    rewards = service.get_user_rewards()
    print("check_for_low_rewards", rewards)
    if rewards > 2: return False 
    else: return True

