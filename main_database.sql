use train;

show tables;

-- TABLE - 1 : login -> User Data
desc login;

select * from login;

-- TABLE - 2 : trains -> List of Trains
create table trains(

id int auto_increment primary key,
train_no varchar(5) not null,
train_name varchar(30) not null,
source_station varchar(30) not null,
destination_station varchar(30) not null,
total_distance int not null,
avg_speed float not null

);

desc trains;

select * from trains;

insert into trains(train_no, train_name, source_station, destination_station, total_distance, avg_speed)
values('18620', 'INTERCITY EXP', 'GODDA - GODA', 'RANCHI - RNC', 457, 56);

-- TABLE - 3 : route -> Route of a train
create table route(
train_no varchar(5) not null,
station_code varchar(10) not null,
sequence varchar(2) not null,
distance int not null
);

desc route;

-- TABLE - 4 : class_fare -> Fare of different class types like 1AC, 2AC, 3AC, SL, etc.
create table class_fare(
class_code varchar(5) not null,
rate_per_km int not null,
reservation_charge int not null,
gst_percent float not null
);