drop table if exists AccountsBK;

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
