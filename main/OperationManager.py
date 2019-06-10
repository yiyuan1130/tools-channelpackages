# -*- coding: utf-8 -*-

import os
import shutil
import Config

def check_output_floder():
	if os.path.exists(Config.OUTPUT_SIGNED_FLODER):
		pass
	else:
		os.makedirs(Config.OUTPUT_SIGNED_FLODER)

def get_channel_list():
	channel_list = []
	with open(Config.CHANNEL_FILE, 'r') as file:
		for line in file.readlines():
			channel = line.strip()
			channel_list.append(channel)
	return channel_list

def remove_useless():
	file_or_floder_list = os.listdir('./')
	for file_or_floder in file_or_floder_list:
		if file_or_floder in Config.USED_LIST:
			continue
		else:
			if os.path.isdir(file_or_floder):
				shutil.rmtree(file_or_floder)
			elif os.path.isfile(file_or_floder):
				os.remove(file_or_floder)

def remove_compile_floder():
	shutil.rmtree(Config.BASE_APK_COMPILE_FLODER)

def copy_base_apk():
	shutil.copyfile(Config.BASE_APK_PATH, Config.BASE_APK_NAME)