BOT_TOKEN = "7182602993:AAGgzrs1gom1CX5Z8BD01a1dQjp2--UbusU"
DEPOSIT_ADDRESS = "EQDMdep8oQp98sEslzw_BVf8Sg03V1ujLU1PDfnrY-dhdbpr"
API_KEY = "eef7e4bdd51ebe8a0eb9a0632854cda46552f5eeaa4f7fcb63feab41a685f945"
RUN_IN_MAINNET = True  # Switch True/False to change mainnet to testnet

if RUN_IN_MAINNET:
    API_BASE_URL = "https://toncenter.com"
else:
    API_BASE_URL = "https://testnet.toncenter.com"
