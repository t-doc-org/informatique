create table contact (
  nom text not null,
  prenom text not null,
  email text not null,
  sexe char(1) not null,
  naissance date,
  statut text,
  lieu text,
  code_postal char(4),
  interets text
);

insert into contact values
  ('Dupont', 'Bob', 'dupont.bob@glog.com', 'M', '1990-09-10', 'divorcé', 'Villars-sur-Glâne', '1752', 'Tennis, Animaux'),
  ('Martin', 'Anne', 'amartin@fri.ch', 'F', '1995-06-02', 'célibataire', 'Lausanne', '1000', 'Escape game'),
  ('Dunant', 'Martine', 'martine.dunant@google.com', 'F', '1985-12-24', 'séparé', 'Val-d''Illiez', '1873', 'Lecture'),
  ('Schmidt', 'Léo', 'leo@cine.ch', 'M', '2000-01-01', 'célibataire', 'La Roche', '1634', 'Cinéma, Jeux de société'),

  ('Dupont', 'Jean', 'jean.dpt85@swissmail.ch', 'M', '1985-06-15', 'célibataire', 'Genève', '1201', 'Sports, Musique'),
  ('Dubois', 'Marie', 'm.dubois_lovesreading@romandie.com', 'F', '1992-03-22', 'séparé', 'Lausanne', '1000', 'Lecture, Voyage'),
  ('Martin', 'Luc', 'lmartin.rando@helvetia.org', 'M', '2001-11-02', 'célibataire', 'Neuchâtel', '2000', 'Cuisine, Randonnée'),
  ('Lefevre', 'Sophie', 's.lefevre.art@photochic.ch', 'F', '1989-08-30', 'divorcé', 'Fribourg', '1700', 'Photographie, Art'),
  ('Roux', 'Pierre', 'pieroux.musicfan@playmail.ch', 'M', '1995-12-10', 'célibataire', 'Yverdon-les-Bains', '1400', 'Cinéma, Musique'),

  ('Moreau', 'Laura', 'laura.moreau_travel@swissmail.ch', 'F', '1981-04-11', 'séparé', 'Vevey', '1800', 'Voyage, Cuisine'),
  ('Simon', 'David', 'dsimon.techgeek@romandie.com', 'M', '1990-09-18', 'célibataire', 'Nyon', '1260', 'Sports, Technologie'),
  ('Blanc', 'Emilie', 'emilie_blanc.art@postnet.ch', 'F', '1986-07-24', null, 'Montreux', '1820', 'Musique, Art'),
  ('Gauthier', 'Antoine', 'antoine.g.photo@helvetia.org', 'M', '1993-01-14', 'célibataire', 'Bulle', '1630', 'Randonnée, Photographie'),
  ('Garcia', 'Elena', 'elena.garcia_cooking@genmail.ch', 'F', '1982-05-05', 'séparé', 'Sion', '1950', 'Cuisine, Lecture'),

  ('Lambert', 'Lucas', 'lucas_lambert.moviebuff@swissmail.ch', 'M', '1988-10-23', 'célibataire', 'Morges', '1110', 'Cinéma, Sports'),
  ('Lemoine', 'Julie', 'julie_traveller@romandie.com', 'F', '1991-02-17', 'En couple', null, null, 'Voyage, Cinéma'),
  ('Duval', 'Alexandre', 'aduval_tech@postnet.ch', 'M', '1983-03-30', 'séparé', 'Payerne', '1530', 'Technologie, Cuisine'),
  ('Leroux', 'Claire', 'claire.leroux_artistic@swissmail.ch', 'F', '1996-06-29', 'célibataire', null, null, 'Lecture, Art'),
  ('Giraud', 'Thomas', 'thomas_giraud@playmail.ch', 'M', '1987-12-01', 'célibataire', 'La Chaux-de-Fonds', '2300', 'Sports, Musique'),

  ('Perrin', 'Manon', 'manon.perrin_photo@romandie.com', 'F', '1990-07-13', 'séparé', 'Carouge', '1227', 'Photographie, Voyage'),
  ('Renaud', 'Nicolas', 'n.renaud_films@genmail.ch', 'M', '1979-11-25', 'célibataire', 'Meyrin', '1217', 'Technologie, Cinéma'),
  ('Mercier', 'Isabelle', 'isabelle_cooking_music@swissmail.ch', 'F', '1984-05-18', 'divorcé', 'Chavannes-près-Renens', '1022', 'Cuisine, Musique'),
  ('Chevalier', 'Vincent', 'vincent.chevalier.sport@playmail.ch', 'M', '1995-04-07', 'célibataire', 'Renens', '1020', null),
  ('Barbier', 'Camille', 'camille.barbier_art@helvetia.org', 'F', '1987-10-19', 'séparé', 'Onex', '1213', 'Lecture, Art'),

  ('Rousseau', 'Adrien', 'adrien.r_travel@romandie.com', 'M', '1992-03-12', 'divorcé', 'Versoix', '1290', 'Photographie, Voyage'),
  ('Leclerc', 'Sarah', 'sarah_leclerc@helvetia.org', 'F', '1980-06-02', 'séparé', 'Thônex', '1226', 'Musique, Lecture'),
  ('Faure', 'Guillaume', 'guillaume_faure.tech@genmail.ch', 'M', '1986-11-15', 'célibataire', 'Vernier', '1214', 'Technologie, Sports'),
  ('Royer', 'Alice', 'alice_r.artistic@romandie.com', 'F', '1991-08-27', 'célibataire', 'Plan-les-Ouates', '1228', 'Art, Photographie'),
  ('Pichon', 'Benoit', 'benoit.pichon_music@swissmail.ch', 'M', '1985-09-06', 'séparé', 'Pregny-Chambésy', '1292','Voyage, Musique'),

  ('Noel', 'Julien', 'julien_noel_athlete@helvetia.org', 'M', '1993-12-24', 'célibataire', 'Vésenaz', '1222', 'Sports, Cinéma'),
  ('Aubry', 'Pauline', 'pauline.aubry_cooking@playmail.ch', 'F', '1988-04-09', 'séparé', 'Collonge-Bellerive', '1254', 'Cuisine, Lecture'),
  ('Jacquet', 'François', 'f.jacquet.versoix@swissmail.ch', 'M', '2004-09-19', 'célibataire', 'Versoix', '1290', 'Technologie, Voyage'),
  ('Marchand', 'Valérie', 'valerie_m.art@romandie.com', 'F', '1990-02-25', null, 'Carouge', '1227', 'Musique, Art'),
  ('Muller', 'Philippe', 'philippe.muller_photo@genmail.ch', 'M', '1984-10-11', 'séparé', 'Nyon', '1260', null),

  ('Lemoine', 'Nathalie', 'nathalie.lemoine_trek@helvetia.org', 'F', '2001-05-30', 'séparé', 'Sion', '1950', 'Voyage, Randonnée'),
  ('Collin', 'Laurent', 'laurent.collin.movies@postnet.ch', 'M', '1995-07-14', 'célibataire', 'Sierre', '3960', 'Technologie, Cinéma'),
  ('Brunet', 'Camille', 'camille.brunet_food@swissmail.ch', 'F', '1987-08-07', 'célibataire', 'Fribourg', '1700', 'Lecture, Cuisine'),
  ('Girard', 'Mathieu', 'mathieu_g.music@playmail.ch', 'M', '1982-12-30', 'célibataire', 'Monthey', '1870', 'Musique, Art'),
  ('Bourdon', 'Elodie', 'elodie_b.photo@romandie.com', 'F', '1990-06-18', 'séparé', 'Vevey', '1800', 'Photographie, Randonnée'),

  ('Renaud', 'Aurélien', 'aurelien_renaud_sport@swissmail.ch', 'M', '1989-01-13', 'célibataire', 'Lausanne', '1000', 'Voyage, Sports'),
  ('Germain', 'Laure', 'laure_g.art@genmail.ch', 'F', '1994-11-20', 'célibataire', 'Yverdon-les-Bains', '1400', null),
  ('Perrier', 'Quentin', 'quentin.perrier_music@romandie.com', 'M', '1993-03-01', 'séparé', 'Neuchâtel', '2000', 'Technologie, Musique'),
  ('Robin', 'Chloé', 'chloe.robin.cooking@postnet.ch', 'F', '1985-07-29', 'célibataire', 'Genève', '1201', 'Cuisine, Photographie'),
  ('Lemoine', 'Jérôme', 'jerome.lemoine.trek@swissmail.ch', 'M', '1986-02-22', 'séparé', 'Nyon', '1260', 'Randonnée, Voyage'),

  ('Renard', 'Catherine', 'catherine.renard_books@romandie.com', 'F', '1990-09-05', 'divorcé', 'La Chaux-de-Fonds', '2300', 'Art, Lecture'),
  ('Durand', 'Victor', 'victor_durand.movies@swissmail.ch', 'M', '1997-01-17', 'divorcé', 'Martigny', '1920', 'Sports, Cinéma'),
  ('Lemoine', 'Thomas', 'thomas.lemoine.tech@genmail.ch', 'M', '1984-11-03', 'célibataire', 'Fribourg', '1700', 'Musique, Technologie'),
  ('Bernard', 'Claire', 'claire.bernard.photo@romandie.com', 'F', '1992-04-16', 'séparé', null, null, 'Voyage, Photographie'),
  ('Petit', 'Julie', 'julie.petit.books@postnet.ch', 'F', '1983-08-26', null, 'Sion', '1950', 'Lecture, Randonnée');
