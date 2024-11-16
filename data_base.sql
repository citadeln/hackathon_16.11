CREATE TABLE "objects_type"(   
  id SERIAL primary key,
  name VARCHAR(42)
);

CREATE TABLE objects(   
  id SERIAL primary key,
  name VARCHAR(42) not null default 0,
  type INTEGER not null default 0,
  constraint fk_objects_type foreign key (type) objects_type(id)
);

CREATE TABLE wells(   
  well INTEGER primary key,
  ngdu INTEGER not null default 0,
  cdng INTEGER not null default 0,
  kust INTEGER not null default 0,
  mest INTEGER not null default 0
);

СREATE TABLE well_day_histories(   
  well INTEGER not null,
  date_fact date not null default current_date primary key,
  debit FLOAT not null default 0,
  ee_consume FLOAT not null default 0,
  expenses FLOAT not null default 0,
  pump_operating FLOAT not null default 0,
  constraint fk_well_day_histories_well foreign key (well) references wells(well)
);

СREATE TABLE well_day_plans(   
  well INTEGER not null,
  date_plan date not null default current_date primary key,
  debit FLOAT not null default 0,
  ee_consume FLOAT not null default 0,
  expenses FLOAT not null default 0,
  pump_operating FLOAT not null default 0,
  constraint fk_well_day_histories_well foreign key (well) references wells(well)
);

-- insert into PROG_TEST_PEOPLE values (1, 'Anna', 166);
-- insert into PROG_TEST_PEOPLE values (2, 'Andrey', 211);
-- insert into PROG_TEST_PEOPLE values (3, 'Kate', 333);
-- insert into PROG_TEST_PEOPLE values (4, 'Denis', 131);

--SELECT *;
