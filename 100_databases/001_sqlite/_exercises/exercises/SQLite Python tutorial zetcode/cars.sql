BEGIN TRANSACTION;
CREATE TABLE cars(id INT, name TEXT, price INT);
INSERT INTO "cars" VALUES(1,'Audi',52643);
INSERT INTO "cars" VALUES(2,'Mercedes',57642);
INSERT INTO "cars" VALUES(5,'Bentley',350000);
INSERT INTO "cars" VALUES(6,'Hummer',41400);
COMMIT;