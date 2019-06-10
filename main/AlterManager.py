# -*- coding: utf-8 -*-

import json
import Config

def change_config(target_channel):
	# 要修改的两个变量
	channel = 'CHANNEL'

	# 读原有的json
	config_str = open(Config.CONFIG_PATH, 'r').read()
	config_dict = json.loads(config_str)
	config_dict[channel] = target_channel

	# 写入修改后的json
	with open(Config.CONFIG_PATH, 'w') as f:
		to_write_data = json.dumps(config_dict, indent=4)
		f.write(to_write_data)
