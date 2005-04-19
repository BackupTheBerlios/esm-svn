use esm;
drop table if exists AccountsVV;

create table AccountsVV (
    accountsVVId                   int not null primary key auto_increment,
	ID                             varchar(10) not null,
	Nr                             varchar(10) not null,
	Name                           varchar(64) not null,
	Kommentare                     text,
	ErsteingabeAm                  date not null,
	Fehlercode                     varchar(16),
	changedOn                      char(2) not null,
	changedBy                      varchar(32) not null,
	changedAt                      datetime not null
);

