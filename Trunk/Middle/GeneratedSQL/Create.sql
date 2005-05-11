/*
Start of generated SQL.

# Date         = Wed May 11 17:17:20 2005
# Python ver   = 2.3.3 (#51, Dec 18 2003, 20:22:39) [MSC v.1200 32 bit (Intel)]
# Op Sys       = nt
# Platform     = win32
# Cur dir      = C:\jgott\Privat\SFW\esm-src\Middle
# Num classes  = 11

Classes:
	BLZ
	Prices
	AccountsMI
	AccountsTR
	AccountsVE
	AccountsBK
	AccountsVV
	AccountsAK
	AccountsEK
	Transfers
	IDs
*/

drop database if exists esm;
create database esm;
use esm;

create table BLZ (
    bLZId                          int not null primary key auto_increment,
	BLZ                            varchar(8) not null,
	Bank                           varchar(26) not null,
	ChangedOn                      char(2) not null,
	ChangedAt                      datetime not null,
	ChangedBy                      varchar(32) not null
);


create table Prices (
    pricesId                       int not null primary key auto_increment,
	BKZ                            varchar(10) not null,
	Soll                           double precision not null,
	Haben                          double precision not null,
	Beschreibung                   varchar(64) not null,
	Ab                             date,
	AbSoll                         double precision,
	AbHaben                        double precision,
	Konto                          varchar(10) not null,
	changedOn                      char(2) not null,
	changedAt                      datetime not null,
	changedBy                      varchar(32) not null
);


create table AccountsMI (
    accountsMIId                   int not null primary key auto_increment,
	ID                             varchar(10) not null,
	MitgliedsNr                    varchar(8) not null,
	NeueMitgliedsNr                varchar(8),
	Vorname                        varchar(64) not null,
	Nachname                       varchar(64) not null,
	Titel                          varchar(32),
	Adresszusatz                   varchar(32),
	Strasse                        varchar(64) not null,
	Ort                            varchar(64) not null,
	Countrycode                    char(2) not null,
	PLZ                            varchar(10) not null,
	TelefonPrivat                  varchar(32),
	TelefonDienst                  varchar(32),
	Mobiltelefon                   varchar(32),
	FAX                            varchar(32),
	EMail                          varchar(128),
	Geburtsdatum                   date not null,
	Geschlecht                     char(1) not null,
	KontoNr1                       varchar(20),
	BLZ1                           varchar(10),
	Bank1                          varchar(32),
	Kontoinhaber1                  varchar(32),
	KontoNr2                       varchar(20),
	BLZ2                           varchar(10),
	Bank2                          varchar(32),
	Kontoinhaber2                  varchar(32),
	Beitragsart1                   varchar(32),
	BeitragsartAb1                 date,
	BeitragsartFreiAb1             date,
	BeitragsartErhebungAb1         date,
	Beitragsart2                   varchar(32),
	BeitragsartAb2                 date,
	BeitragsartFreiAb2             date,
	BeitragsartErhebungAb2         date,
	Beitragsart3                   varchar(32),
	BeitragsartAb3                 date,
	BeitragsartFreiAb3             date,
	BeitragsartErhebungAb3         date,
	Beitragsart4                   varchar(32),
	BeitragsartAb4                 date,
	BeitragsartFreiAb4             date,
	BeitragsartErhebungAb4         date,
	Beitragsart5                   varchar(32),
	BeitragsartAb5                 date,
	BeitragsartFreiAb5             date,
	BeitragsartErhebungAb5         date,
	Zahlungsart                    varchar(16) not null,
	LastschriftAb                  date,
	RechnungAb                     date,
	Eintrittsdatum                 date not null,
	Austrittsdatum                 date,
	Austrittsgrund                 varchar(32),
	ErsteingabeAm                  date not null,
	Mahnstufe                      char(1),
	LetzteMahnungAm                date,
	Kommentare                     text,
	Fehlercode                     varchar(16),
	changedOn                      char(2) not null,
	changedBy                      varchar(32) not null,
	changedAt                      datetime not null
);


create table AccountsTR (
    accountsTRId                   int not null primary key auto_increment,
	ID                             varchar(10) not null,
	MitgliedsNr                    varchar(10) not null,
	NeueMitgliedsNr                varchar(10),
	Seit                           date not null,
	Bis                            date,
	Vorname                        varchar(64) not null,
	Nachname                       varchar(64) not null,
	Titel                          varchar(32),
	Adresszusatz                   varchar(32),
	Strasse                        varchar(64) not null,
	Ort                            varchar(64) not null,
	Countrycode                    char(2) not null,
	PLZ                            varchar(10) not null,
	TelefonPrivat                  varchar(32),
	TelefonDienst                  varchar(32),
	Mobiltelefon                   varchar(32),
	FAX                            varchar(32),
	EMail                          varchar(128),
	Geburtsdatum                   date not null,
	Geschlecht                     char(1) not null,
	KontoNr1                       varchar(20),
	BLZ1                           varchar(10),
	Bank1                          varchar(32),
	Kontoinhaber1                  varchar(32),
	KontoNr2                       varchar(20),
	BLZ2                           varchar(10),
	Bank2                          varchar(32),
	Kontoinhaber2                  varchar(32),
	ErsteingabeAm                  date not null,
	Kommentare                     text,
	Lizenz1                        varchar(32),
	LizenzNr1                      varchar(16),
	LizenzBis1                     date,
	LizenzZuschuss1                double precision,
	Lizenz2                        varchar(32),
	LizenzNr2                      varchar(16),
	LizenzBis2                     date,
	LizenzZuschuss2                double precision,
	Lizenz3                        varchar(32),
	LizenzNr3                      varchar(16),
	LizenzBis3                     date,
	LizenzZuschuss3                double precision,
	Lizenz4                        varchar(32),
	LizenzNr4                      varchar(16),
	LizenzBis4                     date,
	LizenzZuschuss4                double precision,
	Lizenz5                        varchar(32),
	LizenzNr5                      date,
	LizenzBis5                     date,
	LizenzZuschuss5                double precision,
	Lizenz6                        varchar(32),
	LizenzNr6                      date,
	LizenzBis6                     date,
	LizenzZuschuss6                double precision,
	Fortbildungen                  text,
	Honorar1                       varchar(32),
	HonorarBetrag1                 double precision,
	Honorar2                       varchar(32),
	HonorarBetrag2                 double precision,
	Honorar3                       varchar(32),
	HonorarBetrag3                 double precision,
	Honorar4                       varchar(32),
	HonorarBetrag4                 double precision,
	Honorar5                       varchar(32),
	HonorarBetrag5                 double precision,
	Honorar6                       varchar(32),
	HonorarBetrag6                 double precision,
	Training1                      varchar(32),
	TrainingOrt1                   varchar(32),
	TrainingTermin1                varchar(20),
	Training2                      varchar(32),
	TrainingOrt2                   varchar(32),
	TrainingTermin2                varchar(20),
	Training3                      varchar(32),
	TrainingOrt3                   varchar(32),
	TrainingTermin3                varchar(20),
	Training4                      varchar(32),
	TrainingOrt4                   varchar(32),
	TrainingTermin4                varchar(20),
	Training5                      varchar(32),
	TrainingOrt5                   varchar(32),
	TrainingTermin5                varchar(20),
	Training6                      varchar(32),
	TrainingOrt6                   varchar(32),
	TrainingTermin6                varchar(20),
	Training7                      varchar(32),
	TrainingOrt7                   varchar(32),
	TrainingTermin7                varchar(20),
	Training8                      varchar(32),
	TrainingOrt8                   varchar(32),
	TrainingTermin8                varchar(20),
	Training9                      varchar(32),
	TrainingOrt9                   varchar(32),
	TrainingTermin9                varchar(20),
	Training10                     varchar(32),
	TrainingOrt10                  varchar(32),
	TrainingTermin10               varchar(20),
	Fehlercode                     varchar(16),
	changedOn                      char(2) not null,
	changedBy                      varchar(32) not null,
	changedAt                      datetime not null
);


create table AccountsVE (
    accountsVEId                   int not null primary key auto_increment,
	ID                             varchar(10) not null,
	VendorNr                       varchar(10) not null,
	Firma                          varchar(64) not null,
	Vorname                        varchar(64) not null,
	Nachname                       varchar(64) not null,
	Titel                          varchar(32),
	Adresszusatz                   varchar(32),
	Strasse                        varchar(64) not null,
	Ort                            varchar(64) not null,
	Countrycode                    char(2) not null,
	PLZ                            varchar(10) not null,
	TelefonPrivat                  varchar(32),
	TelefonDienst                  varchar(32),
	Mobiltelefon                   varchar(32),
	FAX                            varchar(32),
	EMail                          varchar(128),
	KontoNr1                       varchar(20),
	BLZ1                           varchar(10),
	Bank1                          varchar(32),
	Kontoinhaber1                  varchar(32),
	KontoNr2                       varchar(20),
	BLZ2                           varchar(10),
	Bank2                          varchar(32),
	Kontoinhaber2                  varchar(32),
	ErsteingabeAm                  date not null,
	Kommentare                     text,
	Fehlercode                     varchar(16),
	changedOn                      char(2) not null,
	changedBy                      varchar(32) not null,
	changedAt                      datetime not null
);


create table AccountsBK (
    accountsBKId                   int not null primary key auto_increment,
	ID                             varchar(10) not null,
	BankNr                         varchar(10) not null,
	Bank                           varchar(64) not null,
	KontoNr                        varchar(20) not null,
	BLZ                            varchar(20) not null,
	Adresszusatz                   varchar(32),
	Strasse                        varchar(64) not null,
	Ort                            varchar(64) not null,
	Countrycode                    char(2) not null,
	PLZ                            varchar(10) not null,
	TelefonService                 varchar(32),
	Ansprechpartner                varchar(64),
	TelefonAnsprechpartner         varchar(32),
	FAXAnsprechpartner             varchar(32),
	EMailAnsprechpartner           varchar(128),
	PINInternet                    varchar(10),
	PINTelefon                     varchar(10),
	Berechtigte                    text,
	Kommentare                     text,
	ErsteingabeAm                  date not null,
	Fehlercode                     varchar(16),
	changedOn                      char(2) not null,
	changedBy                      varchar(32) not null,
	changedAt                      datetime not null
);


create table AccountsVV (
    accountsVVId                   int not null primary key auto_increment,
	ID                             varchar(10) not null,
	Nr                             varchar(8) not null,
	Name                           varchar(64) not null,
	Kommentare                     text,
	ErsteingabeAm                  date not null,
	Fehlercode                     varchar(16),
	changedOn                      char(2) not null,
	changedBy                      varchar(32) not null,
	changedAt                      datetime not null
);


create table AccountsAK (
    accountsAKId                   int not null primary key auto_increment,
	ID                             varchar(10) not null,
	Nr                             varchar(8) not null,
	Name                           varchar(64) not null,
	Kommentare                     text,
	ErsteingabeAm                  date not null,
	Fehlercode                     varchar(16),
	changedOn                      char(2) not null,
	changedBy                      varchar(32) not null,
	changedAt                      datetime not null
);


create table AccountsEK (
    accountsEKId                   int not null primary key auto_increment,
	ID                             varchar(10) not null,
	Nr                             varchar(8) not null,
	Name                           varchar(64) not null,
	Kommentare                     text,
	ErsteingabeAm                  date not null,
	Fehlercode                     varchar(16),
	changedOn                      char(2) not null,
	changedBy                      varchar(32) not null,
	changedAt                      datetime not null
);


create table Transfers (
    transfersId                    int not null primary key auto_increment,
	TAID                           varchar(20) not null,
	TransferID                     varchar(20) not null,
	ImportWho                      varchar(32),
	ImportBeschreibung             varchar(100),
	Beschreibung                   varchar(100),
	Who                            varchar(32),
	Haben                          double precision,
	Soll                           double precision,
	Konto1                         varchar(10),
	Konto2                         varchar(10),
	changedBy                      varchar(32) not null,
	changedAt                      datetime not null,
	Jahr                           int not null,
	Datum                          datetime,
	BKZ                            varchar(10) not null,
	changedOn                      char(2) not null
);


create table IDs (
    iDsId                          int not null primary key auto_increment,
	Tablename                      varchar(64) not null,
	LastID                         int not null,
	Lastschriften                  varchar(64)
);


create table _MKClassIds (
	id int not null primary key,
	name varchar(100)
);
insert into _MKClassIds (id, name) values
	(1, 'BLZ'),
	(2, 'Prices'),
	(3, 'AccountsMI'),
	(4, 'AccountsTR'),
	(5, 'AccountsVE'),
	(6, 'AccountsBK'),
	(7, 'AccountsVV'),
	(8, 'AccountsAK'),
	(9, 'AccountsEK'),
	(10, 'Transfers'),
	(11, 'IDs');

show tables

/* end of generated SQL */
