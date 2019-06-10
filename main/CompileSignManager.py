# -*- coding: utf-8 -*-

import subprocess
import Config
import platform

def decompile_base_apk():
	subprocess.call('apktool d ./{0}'.format(Config.BASE_APK_NAME), shell=True)

def dex2jar():
	os_name = platform.system()
	if os_name == 'Windows':
		subprocess.call('./dex2jar-2.0/d2j-dex2jar.bat ./{0}'.format(Config.BASE_APK_NAME), shell=True)
	elif os_name == 'Darwin':
		subprocess.call('sh ./dex2jar-2.0/d2j-dex2jar.sh ./{0}'.format(Config.BASE_APK_NAME), shell=True)
	
def compile_base_apk():
	subprocess.call('apktool b ./{0}'.format(Config.BASE_APK_COMPILE_FLODER), shell=True)

def resign_new_apk(target_channel):
	output_path = '{0}/resigned-{1}'.format(Config.OUTPUT_SIGNED_FLODER, Config.BASE_APK_NAME.replace('blank', target_channel))
	subprocess.call('jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keypass {0} -storepass {1} -keystore {2} -signedjar {3} {4} {5}'.format(Config.KEY_PASS, Config.STORE_PASS, Config.KEY_STORE_PATH, output_path, Config.NEW_UNSIGNED_APK_PATH, Config.KEY_STORE_NAME), shell=True)