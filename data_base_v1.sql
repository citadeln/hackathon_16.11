CREATE TABLE wells (   
  well INTEGER PRIMARY KEY,
  ngdu INTEGER NOT NULL DEFAULT 0,
  cdng INTEGER NOT NULL DEFAULT 0,
  kust INTEGER NOT NULL DEFAULT 0,
  mest INTEGER NOT NULL DEFAULT 0,
  CONSTRAINT fk_objects_ngdu FOREIGN KEY (ngdu) REFERENCES "objects"(type),
  CONSTRAINT fk_objects_cdng FOREIGN KEY (cdng) REFERENCES "objects"(type),
  CONSTRAINT fk_objects_kust FOREIGN KEY (kust) REFERENCES "objects"(type),
  CONSTRAINT fk_objects_mest FOREIGN KEY (mest) REFERENCES "objects"(type)
);

CREATE TABLE objects (   
  id SERIAL PRIMARY KEY,
  name VARCHAR(42),
  type INTEGER NOT NULL DEFAULT 0,
  CONSTRAINT fk_objects_type FOREIGN KEY (type) REFERENCES "objects_type"(id)
);

CREATE TABLE "objects_type" (   
  id SERIAL PRIMARY KEY,
  name VARCHAR(42)
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

INSERT INTO wells (well, ngdu, cdng, kust, mest) 
VALUES (1111, 0, 0, 0, 0);
