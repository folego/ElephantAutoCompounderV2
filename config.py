import os

# error and format handling

def read_config_strategy():
    strategy = os.environ['STRATEGY']
    return int(strategy)

def read_config_transaction_time():
    time = os.environ['DAILY_TIME_TO_TRANSACTION']
    return int(time) # convert to 12 AM/PM

def read_config_interval_info():
    interval = os.environ['INTERVAL_INFO']
    return int(interval) * 60