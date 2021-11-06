-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Czas generowania: 05 Lis 2021, 00:45
-- Wersja serwera: 10.4.21-MariaDB
-- Wersja PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `Gra`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `gracze`
--

CREATE TABLE `gracze` (
  `id_gracza` int(11) NOT NULL,
  `kraj` text COLLATE utf8_polish_ci NOT NULL,
  `data_dolaczenia` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `gracze`
--

INSERT INTO `gracze` (`kraj`, `liczba_graczy`) VALUES
('Polska', 11),
('Stany Zjednoczone', 8),
('Francja', 7),
('Niemcy', 6),
('Rosja', 6);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `gracze`
--
ALTER TABLE `gracze`
  ADD PRIMARY KEY (`id_gracza`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `gracze`
--
ALTER TABLE `gracze`
  MODIFY `id_gracza` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=201;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
