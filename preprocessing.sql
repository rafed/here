UPDATE data SET holiday=1 WHERE weekday=6;
UPDATE data SET weekday=MOD((weekday-1), 7) WHERE time="23:30" or time="23:45";
UPDATE data set weekday=6 WHERE weekday=-1;
DELETE FROM data WHERE LENGTH(dst)=0;
UPDATE data SET src=REPLACE(src, "\'", " ");
UPDATE data SET dst=REPLACE(dst, "\'", " "); -- labh nai

quotation space diye replace

java -Xmx2000m -jar weka.jar