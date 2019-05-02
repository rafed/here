create database if not exists here;

GRANT ALL PRIVILEGES ON here.* TO 'here'@'localhost' IDENTIFIED BY 'here';

drop table data;

create table data (
	date varchar(20),
	time varchar(20),
	weekday int,
	src varchar(300),
	dst varchar(300),
	-- le varchar(10),
	-- cn varchar(10),
	-- sp varchar(10),
	su varchar(10),
	ff varchar(10),
	-- shp varchar(2000),
	temperature double,
	daylight varchar(5),
	humidity varchar(10),
	-- rainfall varchar(10),
	raindesc varchar(50),
	windspeed varchar(10),
	holiday int,
	area int,
	jf varchar(10)
)
