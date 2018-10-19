-- please do this, data is getting huge :3 19 min 49.53 sec
ALTER TABLE data DROP shp;
DELETE FROM data WHERE LENGTH(dst)=0;

-- fix dates
UPDATE data SET weekday=MOD((weekday-1), 7) WHERE time="23:30" or time="23:45";
UPDATE data set weekday=6 WHERE weekday=-1;

-- fix day night
UPDATE data SET daylight=0 WHERE daylight='D';
UPDATE data SET daylight=1 WHERE daylight='N';

-- delete night data
select distinct time from data where str_to_date(time, '%H:%i') >= str_to_date('2:00','%H:%i') and str_to_date(time, '%H:%i') <= str_to_date('6:00','%H:%i');
DELETE FROM data WHERE str_to_date(time, '%H:%i') >= str_to_date('2:00','%H:%i') and str_to_date(time, '%H:%i') <= str_to_date('6:00','%H:%i');

-- fix holiday
UPDATE data SET holiday=1 WHERE weekday=6;

-- not needed now since turning strings to numerals
UPDATE data SET src=REPLACE(src, "\'", " ");
UPDATE data SET dst=REPLACE(dst, "\'", " "); -- labh nai

-- for dumping data
select src,dst,cn,weekday,temperature,daylight,humidity,windspeed,time,holiday,area,jf from data into outfile '/tmp/final.csv' fields terminated by ',' lines terminated by '\n';

-- useful stuff
mysqldump -uhere -phere here data > traffic.sql
java -Xmx2000m -jar weka.jar


ff,shp,le,sp,su,rainfall baad de
