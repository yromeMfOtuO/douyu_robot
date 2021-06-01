cd ../
zip -r douyu_robot.zip douyu_robot
scp ~/Desktop/git_repository/gitee/douyu_robot.zip root@<ip>:/usr/local/script

unzip douyu_robot.zip
cd douyu_robot
pyinstaller -F douyu_robot.py -p /usr/local/lib/python3.6/site-packages

crontab -e

11 23 * * * cd /usr/local/script/;./douyu > /usr/local/script/douyu.log