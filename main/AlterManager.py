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

def change_apktool_yml():
	yml_path = Config.APKTOOL_YML_PATH

	yml_file = open(yml_path, 'r')
	all_lines = yml_file.readlines()
	yml_file.close()
	new_lines = []
	need_record = True
	for i in range(0, len(all_lines)):
		currentline = all_lines[i]
		if 'compressionType' in currentline:
			currentline = 'compressionType: true'
		if 'isFrameworkApk' in currentline:
			need_record = True
		if need_record == True:
			new_lines.append(currentline.replace('\n', ''))
		if 'doNotCompress' in currentline:
			need_record = False

	new_yml_str = str()
	for line in new_lines:
		new_yml_str = new_yml_str + line + '\n'
	yml_file = open(yml_path, 'w')
	yml_file.write(new_yml_str)
	yml_file.close()