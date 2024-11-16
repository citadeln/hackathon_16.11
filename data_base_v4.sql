CREATE TABLE "objects_type" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(42) NOT NULL
);

CREATE TABLE objects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(42) NOT NULL,
    type INTEGER NOT NULL DEFAULT 0
);
    --CONSTRAINT fk_objects_type FOREIGN KEY (type) REFERENCES "objects_type"(id)

CREATE TABLE wells (
    well INTEGER PRIMARY KEY,
    ngdu INTEGER NOT NULL DEFAULT 0,
    cdng INTEGER NOT NULL DEFAULT 0,
    kust INTEGER NOT NULL DEFAULT 0,
    mest INTEGER NOT NULL DEFAULT 0,
    CONSTRAINT fk_objects_well FOREIGN KEY (well) REFERENCES objects(id),
    CONSTRAINT fk_objects_ngdu FOREIGN KEY (ngdu) REFERENCES objects(id),
    CONSTRAINT fk_objects_cdng FOREIGN KEY (cdng) REFERENCES objects(id),
    CONSTRAINT fk_objects_kust FOREIGN KEY (kust) REFERENCES objects(id),
    CONSTRAINT fk_objects_mest FOREIGN KEY (mest) REFERENCES objects(id)
);

CREATE TABLE well_day_histories (
    well INTEGER NOT NULL,
    date_fact DATE NOT NULL DEFAULT current_date,
    debit FLOAT NOT NULL DEFAULT 0,
    ee_consume FLOAT NOT NULL DEFAULT 0,
    expenses FLOAT NOT NULL DEFAULT 0,
    pump_operating FLOAT NOT NULL DEFAULT 0,
    PRIMARY KEY (well, date_fact),
    CONSTRAINT fk_well_day_histories_well FOREIGN KEY (well) REFERENCES wells(well)
);

CREATE TABLE well_day_plans (
    well INTEGER NOT NULL,
    date_plan DATE NOT NULL DEFAULT current_date,
    debit FLOAT NOT NULL DEFAULT 0,
    ee_consume FLOAT NOT NULL DEFAULT 0,
    expenses FLOAT NOT NULL DEFAULT 0,
    pump_operating FLOAT NOT NULL DEFAULT 0,
    PRIMARY KEY (well, date_plan),
    CONSTRAINT fk_well_day_plans_well FOREIGN KEY (well) REFERENCES wells(well)
);

INSERT INTO objects_type (id, name) VALUES (1, 'скважина(Ресурсный источник)');
INSERT INTO objects_type (id, name) VALUES (2, 'НГДУ (нефтегазодобывающее управление)');
INSERT INTO objects_type (id, name) VALUES (3, 'ЦДНГ (цех добычи нефти и газа)');
INSERT INTO objects_type (id, name) VALUES (4, 'Куст (кустовая площадка)');
INSERT INTO objects_type (id, name) VALUES (5, 'Месторождение');
