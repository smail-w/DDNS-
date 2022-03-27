url=$1
wget https://raw.githubusercontent.com/smail-w/DDNS-auto-update/main/ip.py
wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh" && chmod +x tcp.sh
website="  python3 /root/ip.py ${url}"
echo $website
cat >> /etc/crontab << END
* * * * *  root  $website
END
service cron restart
systemctl enable cron