# USTC Grade Notification

> 中科大教务系统成绩更新后邮件通知。

## 简介

Python 小脚本，用于[中科大教务系统](https://jw.ustc.edu.cn)成绩更新后邮件通知自己。

## 运行

### Linux（以 Ubuntu 为例）

1. `git clone https://github.com/yusanshi/USTC_grade_notification.git && cd USTC_grade_notification`；
2. 在`config.py`中填入配置信息；
3. `python3 send_mail.py`，测试是否能收到测试邮件；
4. `sudo apt install python3-pip && pip3 install bs4 lxml` 
5. 先直接`python3 main.py`运行，若没问题，`nohup python3 main.py >/dev/null 2>&1 &`使其后台运行。可在`log.txt`下查看运行日志。若想结束程序运行，`ps -fe | grep main.py`查看进程号，`kill -9 进程号`结束即可。

### Windows

1. 点击上方“Clone or download”后，点击“Download ZIP”下载并解压；
2. 在`config.py`中填入配置信息；
3. `python send_mail.py`，测试是否能收到测试邮件；
4. `pip install bs4 lxml`；
5. `python main.py`，可在`log.txt`下查看运行日志。

