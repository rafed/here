-- please do this, data is getting huge :3 19 min 49.53 sec
ALTER TABLE data DROP cn, DROP ff, DROP shp, DROP le, DROP sp, DROP su, DROP rainfall;
DELETE FROM data WHERE LENGTH(dst)=0;

-- fix dates
UPDATE data SET weekday=MOD((weekday-1), 7) WHERE time="23:30" or time="23:45";
UPDATE data set weekday=6 WHERE weekday=-1;

-- weekday checker
select distinct date,time,weekday,daylight from data where date="20-10-2018";

-- fix day night ### NO MORE
UPDATE data SET daylight=0 WHERE daylight='D';
UPDATE data SET daylight=1 WHERE daylight='N';

-- delete night data
select distinct time from data where str_to_date(time, '%H:%i') >= str_to_date('2:00','%H:%i') and str_to_date(time, '%H:%i') <= str_to_date('6:00','%H:%i');

DELETE FROM data WHERE str_to_date(time, '%H:%i') >= str_to_date('2:00','%H:%i') and str_to_date(time, '%H:%i') <= str_to_date('6:00','%H:%i');

-- fix holiday
UPDATE data SET holiday=1 WHERE weekday=6;
UPDATE data SET holiday=1 WHERE date="19-10-2018";


-- not needed now since turning strings to numerals
UPDATE data SET src=REPLACE(src, "\'", " ");
UPDATE data SET dst=REPLACE(dst, "\'", " "); -- labh nai

-- for dumping data
select time,src,dst,weekday,temperature,daylight,humidity,windspeed,rainDesc,holiday,area,jf from data into outfile '/tmp/traffic_full_preprocessed.csv' fields terminated by ',' lines terminated by '\n';

-- useful stuff
mysqldump -uhere -phere here data > traffic.sql
java -Xmx2000m -jar weka.jar


ff,shp,le,sp,su,rainfall baad de


########################################################
currently rows 55,654,951
per day around 700,000
146010 delete where windspeed=*
holiday update (19-10-2018, 07-11-2018, 21-11-2018, 23-11-2018)


*
Rain
Drizzle
Light rain

Date range: 07-10-2018  26-12-2018

Ubuntu 14.04.5 LTS
Linux 4.15.0-20-generic x86_64

CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                24
On-line CPU(s) list:   0-23
Thread(s) per core:    2
Core(s) per socket:    6
Socket(s):             2
NUMA node(s):          2
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 63
Stepping:              2
CPU MHz:               1200.068
BogoMIPS:              4799.91
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              15360K
NUMA node0 CPU(s):     0,2,4,6,8,10,12,14,16,18,20,22
NUMA node1 CPU(s):     1,3,5,7,9,11,13,15,17,19,21,23
