### apk 反编译重签名出多渠道包

### 使用说明
1. 打出一个白包，命名为：项目名-blank-版本号.apk，例如：testgame-blank-v1.2.0.apk
2. 查看channel.text中渠道名字列表，按需求增删
3. 打开termianl，进入tools-channelpackage目录
4. 执行shell命令：python ./main/ChannelSign.py [第一步的白包路径] [重签名后所有的apk要保存到的路径]
   例如：python ./main/ChannelSign.py /Users/liyiyuan/Desktop/testgame-blank-v1.1.0.apk /Users/liyiyuan/Projects/APKs/testgame

### 可能出现的问题及解决方式
1. apktool 不存在：
	下载 [apktool](https://ibotpeaches.github.io/Apktool/install/), 根据平台不同按照教程安装apktool
2. 执行 sh ./dex2jar-2.0/d2j-dex2jar.sh 无权限问题：
	需要给相应文件添加可执行权限：chomd +x [无权限的文件]
3. keystore 相关有问题：
	修改Config.py中 KEY_STORE_PATH，KEY_STORE_NAME 等字段

### 注意
1. 不可删除的目录或文件：README.md, .gitignore, .git, main, dex2jar-2.0
2. 禁止修改.gitignore
3. 根据签名方式不同，修改ComplieSignManager.py中resign_new_apk函数的签名方式

### main中各文件说明
1. channel.txt 存放所有渠道的列表
2. Config.py 一些路径名字等配置
3. OperationManager.py 文件操作
4. CompileSignManager.py 反编译、签名等操作
5. AlterManager.py 修改项目内容操作
6. ChannelSign.py 本工具的主入口 

### 编辑时间
李宜源 2019.06.10