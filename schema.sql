create database if not exists here;

GRANT ALL PRIVILEGES ON here.* TO 'here'@'localhost' IDENTIFIED BY 'here';

drop table data;

create table data (
	date varchar(10),
	time varchar(5),
	weekday int,
	li varchar(20),
	src varchar(100),
	dst varchar(100),
	-- le varchar(10),
	-- cn varchar(10),
	-- sp varchar(10),
	su varchar(6),
	ff varchar(6),
	-- shp varchar(2000),
	temperature double,
	daylight varchar(3),
	humidity varchar(5),
	-- rainfall varchar(10),
	raindesc varchar(40),
	rainfall varchar(6),
	windspeed varchar(5),
	holiday int,
	area int,
	jf varchar(10)
)
