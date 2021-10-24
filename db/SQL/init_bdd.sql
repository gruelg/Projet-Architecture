DROP DATABASE  IF EXISTS Curiculum;

create DATABASE Curiculum; 

create table Curiculum.resume(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    email VARCHAR(255),
    date_naissance VARCHAR(100),
    pays VARCHAR(255),
    ville VARCHAR(255),
    code_postal VARCHAR(5)
);

insert into Curiculum.resume(nom, prenom, email, date_naissance, pays, ville, code_postal) values ("","","","","","","");

