ROP TABLE IF EXISTS video;
DROP TABLE IF EXISTS canali;

CREATE TABLE canali (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  numero_iscritti INTEGER DEFAULT 0,
);

CREATE TABLE video (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  canale_id INTEGER NOT NULL,
  titolo TEXT NOT NULL,
  durata INTEGER NOT NULL, -- durata in secondi
  immagine TEXT, -- URL o nome file dell'anteprima
  FOREIGN KEY (canale_id) REFERENCES canali (id)
);

CREATE TABLE categoria (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL UNIQUE
);

-- Insert di esempio per i Canali
INSERT INTO canali (nome, numero_iscritti) VALUES
('TechWorld', 150000),
('CookingWithAmy', 250000),
('TravelVlogs', 100000);

-- Insert di esempio per i Video
INSERT INTO video (canale_id, titolo, durata, immagine) VALUES
(1, 'Top 10 Programming Languages in 2024', 600, 'techworld_top10.png'),
(1, 'How to Build a PC from Scratch', 1200, 'techworld_buildpc.png'),
(2, '5 Easy Pasta Recipes', 900, 'cookingwithamy_pasta.png'),
(2, 'Baking the Perfect Chocolate Cake', 1100, 'cookingwithamy_cake.png'),
(3, 'Exploring the Beaches of Thailand', 800, 'travelvlogs_thailand.png'),
(3, 'A Week in Paris: Top Attractions', 950, 'travelvlogs_paris.png');

-- Insert di esempio per le Categorie
INSERT INTO categoria (nome) VALUES
('Tecnologia'),
('Cucina'),
('Viaggi');
