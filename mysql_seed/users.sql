create table users (
    id int not null auto_increment,
    name varchar(255) not null,
    email varchar(255) not null,
    password varchar(255) not null,
    primary key (id)
) engine=InnoDB auto_increment=1 default charset=utf8mb4;

insert into users (name, email, password) values ('andre', 'teste@gmail.com', '123456');
insert into users (name, email, password) values ('andre 2', 'teste2@gmail.com', '1234567');
insert into users (name, email, password) values ('andre 3', 'teste3@gmail.com', '12345678');