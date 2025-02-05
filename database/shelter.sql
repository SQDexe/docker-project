SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

CREATE DATABASE IF NOT EXISTS `shelter` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `shelter`;

CREATE TABLE `adoptions` (
  `id` int UNSIGNED NOT NULL,
  `date` date NOT NULL,
  `animal_id` int UNSIGNED NOT NULL,
  `signature` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `adoptions` (`id`, `date`, `animal_id`, `signature`) VALUES
(1, '2024-12-23', 1, 'Jane Doe'),
(2, '2021-07-15', 4, 'Joanna Kowalska');

CREATE TABLE `animals` (
  `id` int UNSIGNED NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `species` enum('dog','cat','lizard','bird','rodent') COLLATE utf8mb4_unicode_ci NOT NULL,
  `gender` enum('male','female') COLLATE utf8mb4_unicode_ci NOT NULL,
  `birth` year NOT NULL,
  `arrival` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `animals` (`id`, `name`, `species`, `gender`, `birth`, `arrival`) VALUES
(1, 'Bob', 'dog', 'male', '2021', '2023-03-14'),
(2, 'Polly', 'bird', 'female', '2015', '2021-08-11'),
(3, 'Teeths', 'rodent', 'male', '2023', '2024-09-26'),
(4, 'Kitkat', 'cat', 'male', '2018', '2019-01-24'),
(5, 'Grassy', 'lizard', 'female', '2022', '2025-01-03');

CREATE TABLE `donations` (
  `id` int UNSIGNED NOT NULL,
  `date` date NOT NULL,
  `amount` decimal(12,2) UNSIGNED NOT NULL,
  `signature` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `donations` (`id`, `date`, `amount`, `signature`) VALUES
(1, '2024-12-02', 1000.00, 'Jan Kowalski'),
(2, '2018-09-12', 12000.00, 'John Doe');

CREATE TABLE `workers` (
  `id` int UNSIGNED NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `surname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `password_hash` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `phone_number` varchar(9) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `workers` (`id`, `name`, `surname`, `username`, `password_hash`, `admin`, `phone_number`, `email`) VALUES
(1, '-', '-', 'admin', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 1, '000000000', 'admin@shelter.com'),
(2, 'Jan', 'Kowalski', 'jankow', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 0, '123456789', 'test@gmail.com'),
(3, 'Joe', 'Doe', 'test', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 0, '987654321', 'scraps@gmail.com');


ALTER TABLE `adoptions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `adoption` (`animal_id`);

ALTER TABLE `animals`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `donations`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `workers`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `adoptions`
  MODIFY `id` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `animals`
  MODIFY `id` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

ALTER TABLE `donations`
  MODIFY `id` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `workers`
  MODIFY `id` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;


ALTER TABLE `adoptions`
  ADD CONSTRAINT `adoption` FOREIGN KEY (`animal_id`) REFERENCES `animals` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;