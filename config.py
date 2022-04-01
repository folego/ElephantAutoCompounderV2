import os

# TO DO: error and format handling

def read_config_strategy():
    strategy = os.environ['STRATEGY']
    return int(strategy)

def read_config_transaction_time():
    time = os.environ['DAILY_TIME_TO_EXECUTE_TRANSACTION']
    return int(time)

def read_config_interval_info():
    interval = os.environ['INTERVAL_INFO']
    return int(interval) * 60