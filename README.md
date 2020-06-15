WIFICRACK
======

很简单的WIFI弱口令检测工具,无参数直接交互运行
* python only
* Windows下适用Python3测试通过

安装和依赖
-------------

	1、pywifi: pip install pywifi
	2、无线网卡
	3、Windows与Python3.7+

    
使用
-------------

```
python run.py
Please input your target SSID KEYWORD(Leave it empty to ATTACK all) 输入需要攻击的WIFI名称(不需要完整填写,部分即可),如果留空则攻击全部可探测到的热点
To be ignored SSID KEYWORD(Can be part of your own WIFI name) 当选择攻击全部热点时，可以选择性的跳过部分包含特定关键词的WIFI名称
```

 * 交互方式爆破


```powershell

PS C:\Users> python .\run.py                                                            
Please input your target SSID KEYWORD(Leave it empty to ATTACK all):    1104
To be ignored SSID KEYWORD(Can be part of your own WIFI name):
Attacking SSID @PHICOMM_1104
Trying 123456789 for SSID @PHICOMM_1104...
Trying 1234567890 for SSID @PHICOMM_1104...
...
```
