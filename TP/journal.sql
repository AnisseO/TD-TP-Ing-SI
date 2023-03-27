DROP TABLE IF EXISTS Article;
CREATE TABLE Article (
    id_article integer,
    titre char (100),
    nom_rubrique char(15),
    primary key (id_article)
);

DROP TABLE IF EXISTS Journaliste;
CREATE TABLE Journaliste (
    id_journalist integer,
    prenom char (20),
    nom char (30),
    primary key (id_journalist)
);

DROP TABLE IF EXISTS Rubrique;
CREATE TABLE Rubrique (
    id integer,
    nom char (30),
    primary key (id)
);


DROP TABLE IF EXISTS Auteur;
CREATE TABLE Auteur(
    id_article integer,
    id_journaliste integer,
    primary key (id_journaliste, id_article),
    foreign key (id_journaliste) references Journaliste (id_journalist) ON DELETE CASCADE,
    foreign key (id_article) references Article (id_article) ON DELETE CASCADE
);