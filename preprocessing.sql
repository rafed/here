-- please do this, data is getting huge :3 19 min 49.53 sec
ALTER TABLE data DROP shp;
DELETE FROM data WHERE LENGTH(dst)=0;

-- fix dates
UPDATE data SET weekday=MOD((weekday-1), 7) WHERE time="23:30" or time="23:45";
UPDATE data set weekday=6 WHERE weekday=-1;

-- not needed now since turning strings to numerals
UPDATE data SET src=REPLACE(src, "\'", " ");
UPDATE data SET dst=REPLACE(dst, "\'", " "); -- labh nai

-- for dumping data
select src,dst,cn,temperature,daylight,humidity,windspeed,time,holiday,jf from data into outfile '/tmp/lol.csv' fields terminated by ',' lines terminated by '\n';

-- dump table
mysqldump -uhere -phere here data > traffic.sql

java -Xmx2000m -jar weka.jar
