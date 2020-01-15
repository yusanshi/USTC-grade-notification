# USTC Grade Notification

## 简介

Python 小脚本，用于[中科大教务系统](https://jw.ustc.edu.cn)成绩更新后邮件通知自己。

## 运行

### Linux

1. `git clone https://github.com/yusanshi/USTC_grade_notification.git && cd USTC_grade_notification`；
2. 在 `config.py` 中填入配置信息；
3. `pip3 install bs4 lxml`；
4. `python3 send_mail.py` 测试邮件，`python3 login.py` 测试登录；
5. 先直接 `python3 main.py` 运行，若没问题，`nohup python3 main.py >/dev/null 2>&1 &` 使其后台运行。可在 `log.txt` 下查看运行日志。若想结束程序运行，`ps -fe | grep main.py` 查看进程号，`kill -9 进程号`结束即可。亦可使用 Tmux，Screen 等工具。

### Windows

1. 点击上方“Clone or download”后，点击“Download ZIP”下载并解压；
2. 在 `config.py` 中填入配置信息；
3. `pip install bs4 lxml`；
4. `python send_mail.py` 测试邮件，`python login.py` 测试登录；
5. `python main.py` 运行脚本，可在 `log.txt` 下查看运行日志。

## 注意事项

- 请勿将 `PERIOD` 设置过小，以免增大教务系统压力；
- 配置邮件的 SMTP 服务参数时，部分邮箱（如 163 邮箱）需要填写授权码而不是登录密码，请自行查阅所用邮箱的参数；
- 本程序在 `config.py` 中明文存储教务系统的用户名和密码，本程序不会上传这些信息，如不放心请自行浏览代码。若您同意使用本程序，表示您已知悉可能产生的教务系统用户和密码泄露的风险（如您的服务器被黑，使别人看到您的配置信息）。
