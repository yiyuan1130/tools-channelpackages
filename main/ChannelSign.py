# -*- coding: utf-8 -*-

import sys
import os
import datetime
import Config
import AlterManager
import OperationManager
import CompileSignManager

def prepare_config():
	Config.BASE_APK_PATH = sys.argv[1]
	Config.OUTPUT_SIGNED_FLODER = sys.argv[2]
	Config.BASE_APK_NAME = os.path.basename(Config.BASE_APK_PATH)
	Config.BASE_APK_COMPILE_FLODER = Config.BASE_APK_NAME.replace('.apk', '')
	Config.NEW_UNSIGNED_APK_PATH = './{0}/dist/{1}'.format(Config.BASE_APK_COMPILE_FLODER, Config.BASE_APK_NAME)
	Config.CONFIG_PATH = './{0}/assets/Configs/config.json'.format(Config.BASE_APK_COMPILE_FLODER)

if __name__ == '__main__':
	start_time = datetime.datetime.now()

	prepare_config()
	OperationManager.remove_useless()
	OperationManager.check_output_floder()
	channel_list = OperationManager.get_channel_list()
	for target_channel in channel_list:
		OperationManager.remove_useless()
		OperationManager.copy_base_apk()
		CompileSignManager.decompile_base_apk()
		# CompileSignManager.dex2jar() # 不需要改jar里面的脚本，所以省略
		AlterManager.change_config(target_channel)
		AlterManager.change_apktool_yml()
		CompileSignManager.compile_base_apk()
		CompileSignManager.resign_new_apk(target_channel)
	OperationManager.remove_useless()

	end_time = datetime.datetime.now()
	print('==================================================================')
	print('多渠道包编译重签名完毕，共 {0} 个，总用时：{1}'.format(len(channel_list), end_time - start_time))