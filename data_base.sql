CREATE TABLE wells(   
  well INTEGER primary key,
  ngdu INTEGER not null default 0,
  cdng INTEGER not null default 0,
  kust INTEGER not null default 0,
  mest INTEGER not null default 0,
);

CREATE TABLE wells(   
  well INTEGER primary key,
  ngdu INTEGER not null default 0,
  cdng INTEGER not null default 0,
  kust INTEGER not null default 0,
  mest INTEGER not null default 0,
);

CREATE TABLE PROG_TEST_ACCNT(  
  ACCNT_CODE bigint not null default 10,
  ACCNT_ACNT varchar(30) not null,
  ACCNT_PPL_CODE bigint primary key,
  ACCNT_CRNC varchar(3) not null,
  ACCNT_NAME varchar(2000) not null,
  --constraint uk_PROG_TEST_ACCNT unique (ACCNT_CODE, ACCNT_ACNT, ACCNT_CRNC, ACCNT_NAME),
  constraint fk_PROG_TEST_ACCNT_BLNC_ACCNT_CODE foreign key (ACCNT_CODE) references PROG_TEST_BLNC(BLNC_ACCNT_CODE)
);

create table PROG_TEST_DOCS(
  DOC_PPL_CODE bigint primary key,
  DOC_NUM varchar(30) not null,
  DOC_SERIES varchar(30) not null,
  DOC_TYPE varchar(30) not null,
  DOC_DATE date not null
);

insert into PROG_TEST_DOCS values (1, '1f', 'rrr', 'd', '2021-08-01');
insert into PROG_TEST_DOCS values (2, '2f', 'rrr', 'g', '2024-03-01');
insert into PROG_TEST_DOCS values (3, '2f', 'ttt', '0', '2023-01-02');
insert into PROG_TEST_DOCS values (5, '3f', 'hhh', 'r','2022-01-03');


create table PROG_TEST_ADDRESS(
  ADDR_PPL_CODE bigint primary key,
  ADDR_CITY varchar(200) not null,
  ADDR_STREET varchar(200) not null,
  ADDR_HOUSE varchar(200) not null,
  ADDR_FLAT varchar(20) not null
);

create table PROG_TEST_PEOPLE( 
  PPL_CODE bigint not null,
  PPL_NAME varchar(2000) not null,
  PPL_PPL_CODE bigint primary key,
  --constraint uk_PROG_TEST_PEOPLE unique (PPL_CODE, PPL_NAME, PPL_PPL_CODE),
  constraint fk_PPL_PPL_CODE_DOCS foreign key (PPL_CODE) references PROG_TEST_DOCS(DOC_PPL_CODE),
  constraint fk_PPL_PPL_CODE_ADDRESS foreign key (PPL_CODE) references PROG_TEST_ADDRESS(ADDR_PPL_CODE),
  constraint fk_PPL_PPL_CODE_ACCNT foreign key (PPL_PPL_CODE) references PROG_TEST_ACCNT(ACCNT_PPL_CODE)
);


insert into PROG_TEST_PEOPLE values (1, 'Anna', 166);
insert into PROG_TEST_PEOPLE values (2, 'Andrey', 211);
insert into PROG_TEST_PEOPLE values (3, 'Kate', 333);
insert into PROG_TEST_PEOPLE values (4, 'Denis', 131);

--SELECT * FROM PROG_TEST_DOCS;
