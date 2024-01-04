-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 03:47 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `student_info`
--

CREATE TABLE `student_info` (
  `Name` char(30) NOT NULL,
  `IC_Number` int(12) NOT NULL,
  `Email` char(30) NOT NULL,
  `Password` int(8) NOT NULL,
  `Age` int(2) NOT NULL,
  `Total_fee` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_info`
--

INSERT INTO `student_info` (`Name`, `IC_Number`, `Email`, `Password`, `Age`, `Total_fee`) VALUES
('aliah', 98767, 'aliah@gamil', 981234, 13, 0),
('thirah', 12345678, 'thirah1218@gmail', 12345678, 13, 0),
('aaa', 123456789, 'wasdfgh', 12345678, 13, 30),
('aaa', 123456789, 'wasdfgh', 12345678, 13, 30),
('ttt', 1234567, 'asdfghj', 12345678, 13, 30),
('thii', 12345678, 'asdfgh', 12345678, 13, 54),
('thirah', 2147483647, 'thirah1218@gmail.com', 12345678, 13, 54),
('ayuni', 2147483647, 'ayunighazali03@gmail.com', 12345678, 17, 30),
('aisyah', 390875622, 'aisyah@gmail.com', 65226789, 13, 30),
('hanis', 235678909, 'hanis@gmail.com', 12345678, 13, 54),
('jiq', 41215178, 'jiq@gmail.com', 72728, 13, 54),
('milin', 2147483647, 'milin@gmail.com', 972527, 13, 30),
('milin', 2147483647, 'milin@gmail.com', 972527, 13, 30),
('milin', 2147483647, 'milin@gmail.com', 972527, 13, 54),
('milin', 2147483647, 'milin@gmail.com', 972527, 13, 30);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
