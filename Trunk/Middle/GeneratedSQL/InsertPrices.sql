--
-- Table structure for table 'Prices'
--

DROP TABLE IF EXISTS Prices;
CREATE TABLE Prices (
  pricesId int(11) NOT NULL auto_increment,
  BKZ varchar(10) NOT NULL default '',
  Soll double NOT NULL default '0',
  Haben double NOT NULL default '0',
  Beschreibung varchar(64) NOT NULL default '',
  Ab date default NULL,
  AbSoll double default NULL,
  AbHaben double default NULL,
  Konto varchar(10) NOT NULL default '',
  changedOn char(2) NOT NULL default '',
  changedAt datetime NOT NULL default '0000-00-00 00:00:00',
  changedBy varchar(32) NOT NULL default '',
  PRIMARY KEY  (pricesId)
) TYPE=MyISAM;

--
-- Dumping data for table 'Prices'
--


INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (1,'10ps',5,0,'passives Mitglied Trainerbeitrag','2002-01-01',3,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (2,'10pa',10,0,'passives Mitglied','2002-01-01',6,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (3,'10Jg',8,0,'Jugendliche, Auszubildende Trainerbeitrag','2002-01-01',5,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (4,'10Ju',16,0,'Jugendliche, Auszubildende','2002-01-01',10,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (5,'10Fö',14,0,'Fördermitglied','2002-01-01',8,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (6,'10Fl',22,0,'Familie mit 2 Erwachsenen Trainerbeitrag','2002-01-01',12,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (7,'10Fi',44,0,'Familie mit 2 Erwachsenen','2002-01-01',24,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (8,'10Fm',15,0,'Familie mit 1 Erwachsenen Trainerbeitrag','2002-01-01',8.5,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (9,'10Fa',30,0,'Familie mit 1 Erwachsenen','2002-01-01',17,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (10,'10Ew',11,0,'Erwachsene Trainerbeitrag','2002-01-01',6.5,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (11,'10Er',22,0,'Erwachsene','2002-01-01',13,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (12,'11ps',10,0,'Aufnahmegebühr passives Mitglied Trainerbeitrag','2002-01-01',6,0,'EK3100Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (13,'11pa',20,0,'Aufnahmegebühr passives Mitglied','2002-01-01',12,0,'EK3100Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (14,'11Jg',16,0,'Aufnahmegebühr Jugendliche, Auszubildende Trainerbeitrag','2002-01-01',10,0,'EK3100Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (15,'11Ju',32,0,'Aufnahmegebühr Jugendliche, Auszubildende','2002-01-01',20,0,'EK3100Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (16,'11Fö',28,0,'Aufnahmegebühr Fördermitglied','2002-01-01',16,0,'EK3100Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (17,'11Fl',44,0,'Aufnahmegebühr Familie mit 2 Erwachsenen Trainerbeitrag','2002-01-01',24,0,'EK3100Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (18,'11Fi',88,0,'Aufnahmegebühr Familie mit 2 Erwachsenen','2002-01-01',48,0,'EK3100Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (19,'11Fm',30,0,'Aufnahmegebühr Familie mit 1 Erwachsenen Trainerbeitrag','2002-01-01',17,0,'EK3100Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (20,'11Fa',60,0,'Aufnahmegebühr Familie mit 1 Erwachsenen','2002-01-01',34,0,'EK3100Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (21,'11Ew',22,0,'Aufnahmegebühr Erwachsene Trainerbeitrag','2002-01-01',13,0,'EK3100Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (22,'11Er',44,0,'Aufnahmegebühr Erwachsene','2002-01-01',26,0,'EK3100Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (23,'11Sc',40,0,'Schwimmkursgebühr','2002-01-01',22,0,'EK3010Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (24,'GutBei',0,0,'Gutschrift Beitrag','2002-01-01',0,0,'EK3000Gut','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (25,'GutAuf',0,0,'Gutschrift Aufnahmegebühr','2002-01-01',0,0,'EK3100Gut','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (26,'GutKu',0,40,'Gutschrift Kursgebühr','2002-01-01',0,22,'EK3010Gut','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (27,'GutSto',0,15,'Gutschrift Stornierungsgebühr','2002-01-01',0,3.83,'AK2230Bank','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (28,'Storno',0,0,'Stornierung','2002-01-01',3.83,0,'BK1100','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (29,'EL',0,0,'Lastschrift','2002-01-01',0,0,'VV1400','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (30,'Ein',0,0,'Einzahlung','2002-01-01',0,0,'BK1100','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (31,'Aus',0,0,'Auszahlung','2002-01-01',0,0,'BK1100','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (32,'Mahn',10,0,'Mahnung','2002-01-01',6,0,'EK3200','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (33,'Verw',0,0,'Verwaltungsgebühr','2002-01-01',7,0,'EK3200','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (34,'GutMahn',0,10,'Gutschrift Mahngebühr','2002-01-01',0,6,'EK3200','JG','2002-03-04 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (35,'10Eh',0,0,'Ehrenmitglied','2002-01-01',0,0,'EK3000Ein','JG','2002-03-09 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (36,'11Eh',0,0,'Aufnahmegebühr Ehrenmitglied','2002-01-01',0,0,'EK3100Ein','JG','2002-03-09 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (37,'11AT',0,0,'Aufnahmegebühr Aushilfstrainer','2002-01-01',0,0,'EK3100Ein','JG','2002-03-09 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (38,'10AT',0,0,'Aushilfstrainer','2002-01-01',0,0,'EK3100Ein','JG','2002-03-09 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (39,'Spende',0,0,'Beitragsspende','2002-01-01',0,0,'EK3000Ein','JG','2002-03-09 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (40,'Raten',0,0,'Ratenzahlung','2002-01-01',0,0,'VV1410','JG','2002-03-09 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (41,'10Em',0,0,'Ehrenmitglied','2002-01-01',0,0,'EK3000Ein','JG','2000-08-06 21:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (43,'20Aus',0,0,'Auszahlung','2002-01-01',0,0,'BK1100','JG','2002-10-20 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (42,'20Ab',0,0,'Trainerabrechnung','2002-01-01',0,0,'AK2010Trai','JG','2002-10-20 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (44,'20Storno',0,0,'Stornierung der Auszahlung','2002-01-01',0,0,'BK1100','JG','2002-10-20 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (45,'20AbVw',0,0,'Abrechnung Verwaltung','2002-01-01',0,0,'AK2010Verw','JG','2002-10-23 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (46,'30Aus410',0,0,'Sportgeräte','2002-01-01',0,0,'AK410','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (47,'30Aus420',0,0,'Büroeinrichtung','2002-01-01',0,0,'AK420','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (48,'31Aus2200',0,0,'Büroverbrauchsmaterial','2002-01-01',0,0,'AK2200','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (49,'31Aus2210T',0,0,'Telefon','2002-01-01',0,0,'AK2210','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (50,'31Aus2210P',0,0,'Porto','2002-01-01',0,0,'AK2210','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (51,'31Aus2230B',0,0,'Bankgebühren','2002-01-01',0,0,'AK2230Bank','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (52,'31Aus2230I',0,0,'Internet-Gebühren','2002-01-01',0,0,'AK2230','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (53,'31Aus2230L',0,0,'Lagermiete','2002-01-01',0,0,'AK2230','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (54,'31Aus2230W',0,0,'Werbung','2002-01-01',0,0,'AK2230','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (55,'31Aus2230V',0,0,'Vereinszeitung','2002-01-01',0,0,'AK2230','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (56,'31Aus2300',0,0,'Abgaben Landessportverband','2002-01-01',0,0,'AK2300','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (57,'31Aus2310',0,0,'Abgaben Fachverband','2002-01-01',0,0,'AK2310','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (58,'31Aus2320',0,0,'sonstige Beiträge','2002-01-01',0,0,'AK2320','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (59,'31Aus2900A',0,0,'Ausbildung','2002-01-01',0,0,'AK2900','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (60,'31Aus2900K',0,0,'Sportkleidung','2002-01-01',0,0,'AK2900','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (61,'31Aus2900R',0,0,'Reisekosten','2002-01-01',0,0,'AK2900','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (62,'31Aus2900S',0,0,'Spielbetrieb','2002-01-01',0,0,'AK2900','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (63,'31Aus2900V',0,0,'Veranstaltungen','2002-01-01',0,0,'AK2900','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (64,'32Aus4630',0,0,'Bewirtung','2002-01-01',0,0,'AK4630','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (65,'40Ausz',0,0,'Auszahlung','2002-01-01',0,0,'BK1100','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (66,'40Storno',0,0,'Stornierung','2002-01-01',0,0,'BK1100','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (67,'40Einz',0,0,'Einzahlung','2002-01-01',0,0,'BK1100','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (68,'50Ein3210',0,0,'sonstige Spenden','2002-01-01',0,0,'EK3210','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (69,'51Ein3300',0,0,'Zuschüsse von Verbänden','2002-01-01',0,0,'EK3300','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (70,'50Ein3310P',0,0,'Zuschüsse aus Förderprogrammen','2002-01-01',0,0,'EK3310','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (71,'50Ein3310S',0,0,'Sachzuwendungen','2002-01-01',0,0,'EK3310','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (72,'50Ein3620',0,0,'Zinserträge','2002-01-01',0,0,'EK3620','JG','2002-11-03 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (73,'31Aus2011',0,0,'Vereinsmanagement','2002-01-01',0,0,'AK2011','JG','2002-11-13 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (74,'51KdtAus',0,0,'Kreditauszahlung','2002-01-01',0,0,'BK1100','JG','2002-11-23 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (75,'41KdtEin',0,0,'Kreditrückzahlung','2002-01-01',0,0,'BK1100','JG','2002-11-23 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (76,'41RatenEin',0,0,'Einzahlung für Ratenzahlung','2002-01-01',0,0,'BK1100','JG','2002-11-23 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (77,'41ZuschEin',0,0,'Einzahlung für Zuschuss','2002-01-01',0,0,'BK1100','JG','2002-11-23 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (78,'51KursAbr',0,0,'Abrechnung von Kurseinnahmen','2002-01-01',0,0,'EK3010Ein','JG','2002-11-23 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (79,'41KursEin',0,0,'Einzahlung von Kurseinnahmen','2002-01-01',0,0,'BK1100','JG','2002-11-23 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (80,'31Aus2900',0,0,'sonstige Ausgaben (ideell)','2002-01-01',0,0,'AK2900','JG','2002-11-23 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (81,'40SVH',0,0,'Saldovortrag','2002-01-01',0,0,'VV0000','JG','2002-11-23 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (82,'40Last1400',0,0,'Guthaben Lastschrifteinzug','2002-01-01',0,0,'VV1400','JG','2002-11-23 12:28:00','Jan Gottschick');
INSERT INTO Prices (pricesId, BKZ, Soll, Haben, Beschreibung, Ab, AbSoll, AbHaben, Konto, changedOn, changedAt, changedBy) VALUES (83,'31Aus2230',0,0,'sonstige Ausgaben','2002-01-01',0,0,'AK2230','JG','2002-11-03 12:28:00','Jan Gottschick');
