create database webpage;
use webpage;

create table users(username varchar(20) primary key, password varchar(30));

insert into users(username,password) 
values("dummy","dummy"),("hack3r","no_flag"),("h4ck_s3cur3","flag{y0u_ar3_st1ll_a_noob31e}");
