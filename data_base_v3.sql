CREATE TABLE object_types (
    id        integer PRIMARY KEY,
    name      varchar(42) NOT NULL
);

CREATE TABLE objects (
    id        integer PRIMARY KEY,
    name      varchar(42) NOT NULL,
    type      integer NOT NULL
);

CREATE TABLE wells (
    well      integer PRIMARY KEY,
    ngdu      integer NOT NULL,
    cdng      integer NOT NULL,
    kust      integer NOT NULL,
    mest      integer NOT NULL,
    CONSTRAINT fk_well FOREIGN KEY(well) REFERENCES objects(id),
    CONSTRAINT fk_ngdu FOREIGN KEY(ngdu) REFERENCES objects(id),
    CONSTRAINT fk_cdng FOREIGN KEY(cdng) REFERENCES objects(id),
    CONSTRAINT fk_kust FOREIGN KEY(kust) REFERENCES objects(id),
    CONSTRAINT fk_mest FOREIGN KEY(mest) REFERENCES objects(id)
);

CREATE TABLE well_day_histories (
    well      integer NOT NULL,
    date_fact date NOT NULL,
    debit           numeric(2,0) NOT NULL,
    ee_consume      numeric(5,2) NOT NULL,
    expenses        numeric(4,3) NOT NULL,
    pump_operating  numeric(2,0) NOT NULL,
    PRIMARY KEY (well,date_fact),
    CONSTRAINT fk_well_h FOREIGN KEY(well) REFERENCES wells(well)
);

CREATE TABLE well_day_plans (
    well      integer NOT NULL,
    date_plan date NOT NULL,
    debit           numeric(2,0) NOT NULL,
    ee_consume      numeric(5,2) NOT NULL,
    expenses        numeric(4,3) NOT NULL,
    pump_operating  numeric(2,0) NOT NULL,
    PRIMARY KEY (well,date_plan),
    CONSTRAINT fk_well_p FOREIGN KEY(well) REFERENCES wells(well)
);

insert into object_types (id,name) values (1,'���� (������������������� ����������)');
insert into object_types (id,name) values (2,'���� (��� ������ ����� � ����)');
insert into object_types (id,name) values (3,'���� �������');
insert into object_types (id,name) values (4,'��������');
insert into object_types (id,name) values (5,'�������������');

