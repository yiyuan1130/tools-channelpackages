# -*- coding: utf-8 -*-

# 白包 apk 路径
BASE_APK_PATH = str()

# 各个渠道包输出文件夹路径
OUTPUT_SIGNED_FLODER = str()

# 白包名字
BASE_APK_NAME = str()

# 白包反编译出的文件夹
BASE_APK_COMPILE_FLODER = str()

# 项目中要修改的 Config.json 文件
CONFIG_PATH = str()

# apktool的yml文件
APKTOOL_YML_PATH = str()

# 修改后编译出的代签名的 apk 路径
NEW_UNSIGNED_APK_PATH = str()

# 记录所有渠道的 txt 路径
CHANNEL_FILE = './main/channel.txt'

# storepass 根据自己项目修改
STORE_PASS = 'store_pass'

# keypass 根据自己项目修改
KEY_PASS = 'key_pass'

# keystore 路径 根据自己项目修改
KEY_STORE_PATH = '/Users/liyiyuan/Projects/Doc/test.keystore'

# keystore 名字 更具自己项目修改
KEY_STORE_NAME = 'key_store_name'

# 不能删除的文件及文件夹列表
USED_LIST = ['README.md', '.gitignore', '.git', 'main', 'dex2jar-2.0']