cpu=$(mpstat |grep -i all| awk '{sum=$3+$4+$5+$6+$7+$8+$9+$10+$11} END {print sum }')
echo $cpu
memory=$(free|grep Mem|awk '{print $3}')
echo $memory
disk=$(df --total|grep -i total|awk '{print $3 }')
echo $disk
d=$( date | awk '{print $4 }')
day=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-sql-container)
mysql -ualaa -p123 -h $day -e "use test1;INSERT INTO dataa (time, cpu,ram,disk) VALUES (CURRENT_TIMESTAMP(),$cpu,$memory,$disk);"

