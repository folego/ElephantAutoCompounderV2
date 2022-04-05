###### V2
###### Utilize the strategies mentioned on the sheet created by from Kelly Snook
###### https://docs.google.com/spreadsheets/d/1f-z7ISxKwffoNm8FEZBen1Xz8kzqlAdi4npkfVv8NU4/edit?usp=sharing
######
# Strategies mentioned: 
# 1 - Alternate Roll/Claim daily (Roll one day and the next day Claim)
# 2 - Roll/Claim once weekly (Roll everyday for 1 week and claim after 7 days without rolling)
# 3 - Roll 180 days, Roll/claim (Roll for 180 days straight and then alternate between roll and claim daily)
# 4 - Roll 1 year, Roll/claim (Roll for 365 days straight and then alternate between roll and claim daily)
# 5 - Roll 5, Claim 2 (Roll 5 days and claim 2 days)
# 6 - Roll S,T,T,S. Claim M,W,F (Roll on Sunday, Tuesday, Thursday and Saturday. Claim on Monday, Wednesday and Friday)
# 7 - Roll 21 days, claim 7 days (Roll for 21 days, wait 7 days and then claim)
# 8 - Roll 4 days, Claim 3 (Roll for 4 days, wait 3 days and then claim)
######
###### Future Features and notes:
###### Send an alert via Telegram or store in a variable?! to track all the rewards claimed.
###### Show info every x minutes (configurable) - How much money you are making per day, max payout 205%, etc.
###### Alert about gas fee. Check how much the user has in the wallet and estimate how much will last.
######
###### Ref Telegram: https://www.geeksforgeeks.org/create-a-telegram-bot-using-python/

import time
# from tkinter import W
import config as cfg
import util as u
import business

# Start Screen
print(f' _____ _     _____ ____  _     ____  _      _____    ____  _____  ____  _      ____  _____ ____  _____')
print(f'/  __// \   /  __//  __\/ \ /|/  _ \/ \  /|/__ __\  / ___\/__ __\/  _ \/ \__/|/  __\/  __//  _ \/  __/')
print(f'|  \  | |   |  \  |  \/|| |_||| / \|| |\ ||  / \    |    \  / \  | / \|| |\/|||  \/||  \  | | \||  \  ')
print(f'|  /_ | |_/\|  /_ |  __/| | ||| |-||| | \||  | |    \___ |  | |  | |-||| |  |||  __/|  /_ | |_/||  /_ ')
print(f'\____\\\____/\____\\\_/   \_/ \|\_/ \|\_/  \|  \_/    \____/  \_/  \_/ \|\_/  \|\_/   \____\\\____/\____\\')
print(f'                                                                                                      ')
print(f' ____  ____  _      ____  ____  _     _      ____    _____  ____  ____  _       _     ____            ')
print(f'/   _\/  _ \/ \__/|/  __\/  _ \/ \ /\/ \  /|/  _ \  /__ __\/  _ \/  _ \/ \     / \ |\/_   \           ')
print(f'|  /  | / \|| |\/|||  \/|| / \|| | ||| |\ ||| | \|    / \  | / \|| / \|| |     | | // /   /           ')
print(f'|  \__| \_/|| |  |||  __/| \_/|| \_/|| | \||| |_/|    | |  | \_/|| \_/|| |_/\  | \// /   /_           ')
print(f'\____/\____/\_/  \|\_/   \____/\____/\_/  \|\____/    \_/  \____/\____/\____/  \__/  \____/           ')
print(f'')
print(f'Reference: https://elephant.money/trunk.html')
print(f'')
print(f'Source: https://github.com/folego/ElephantAutoCompounderV2')
print(f'')

# List the config
print(f'CURRENT CONFIGURATION:')
strategy = cfg.read_config_strategy()
print(f'* Strategy Selected: {strategy}')
transaction = cfg.read_config_transaction_time()
print(f'* Time the transaction will be executed: {transaction}')
interval = cfg.read_config_interval_info()
print(f'* Interval in minutes to show the stats: {round(interval / 60)} mins')
print(f'')
print(f'')
u.log('Starting...', False)
u.log('Total deposits: ' + str(business.get_user_deposits()) + ' TRUNKs', False)

while True:
    while True:
        try:
            # print('Current rewards: ' + str(business.get_user_rewards()) + ' TRUNKs', end='\r')
            u.log('Current rewards: ' + str(business.get_user_rewards()) + ' TRUNKs                                               ')
            business.execute_action_configurated()
            time.sleep(interval)
        except Exception as e:
            pass
            print("ERROR")
            print(e)
            print("Probably an error ocurred. Check your internet connection. Pausing the process for 15 seconds.")
            time.sleep(15)
        else:
            break



# V1
# General options
# minimum_to_roll = 2e18 # delete, not relevant anymore
# time_between_check = 60 # read from config file
# last_reward = 0 # delete, not relevant anymore
# actual_reward = 0 # delete, not relevant anymore

# while True:
#     while True:
#         try:
#             # print(f'Checking actual rewards')
#             actual_rewards = math.floor(get_user_rewards(wallet_public_addr))

#             # Calculating next roll
#             if last_reward == 0:
#                 last_reward = actual_rewards
#             else: 
#                 actual_reward = actual_rewards

#             if last_reward > 0 and actual_reward > 0:
#                 speed = actual_reward - last_reward
#                 # Calculate the current speed (rewards / sec)
#                 speed = speed / time_between_check
#                 remaining = minimum_to_roll - actual_rewards
#                 next_roll = remaining / speed
#                 print(f'Current rewards speed is: {round(speed/1e18*60*60,4)} (TRUNK/hour). Next roll will be available in {display_time(next_roll)}')
#                 last_reward = actual_reward
            
#             # TO DO: Calculate Trunk/month, Trunk/week, Trunk/day, trunk/hour
#             # TO DO: Improve the estimation using average data

#             print(f'Actual rewards: {round(actual_rewards/1e18,4)} TRUNK(s)')
#             if actual_rewards >= math.floor(minimum_to_roll):
#                 print(f'Rolling...')
#                 roll()
#                 print(f'Rolled! Waiting 60 seconds to start a new cycle')
#                 time.sleep(60) # Interval to check a new roll
#             else:
#                 print(f'Min rewards not achieved yet, trying again in {time_between_check} seconds')
#                 time.sleep(time_between_check) # Interval of each check

#         except Exception as e:
#             pass
#             print("ERROR")
#             print(e)
#             print("Entered in the except of the main loop. Probably an error ocurred. Pausing the process for 15 seconds.")
#             time.sleep(15)
#         else:
#             break



