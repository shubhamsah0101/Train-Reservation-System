use train;

show tables;

create table train(

train_no varchar(5) not null primary key,
train_name varchar(50) not null,
fare varchar(3) not null

);

create table train_stations(

id integer primary key auto_increment,
train_no varchar(5) not null,
station varchar(50) not null,
arrival time not null,
departure time not null,
sequence integer not null

);

desc train;

desc train_stations;

insert into train values('13319', 'Dhanbad–Ranchi Express', '120');

insert into train_stations(train_no, station, arrival, departure, sequence) 
values('13319', 'RNC - Ranchi', '12:55', '12:55', 20);

select * from login;

select * from train;

select * from train_stations;

update train_stations set distance = '72' where id = 5;

alter table train_stations add distance varchar(4);

alter table train drop column fare;