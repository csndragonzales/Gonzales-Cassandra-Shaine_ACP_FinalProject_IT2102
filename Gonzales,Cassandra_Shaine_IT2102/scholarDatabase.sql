-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2024 at 05:58 AM
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
-- Database: `scholar_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `StudentID` int(11) NOT NULL,
  `Full_name` varchar(100) DEFAULT NULL,
  `Birthday` date DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`StudentID`, `Full_name`, `Birthday`, `Address`, `Email`, `userid`) VALUES
(1, 'Gonzales,Cassandra Shaine A.', '2005-07-27', 'Conde Labac', 'cassandra@gmail.com', NULL),
(2, 'Masagpag, Ayesha Marie M.', '2005-05-24', 'Sta Rita', 'ayeshamarie@gmail.com', NULL),
(3, 'Rendon, Zaira Mae A.', '2004-09-17', 'Alangilan', 'zairamae@gmail.com', NULL),
(4, 'Alon. Ma. Annita C.', '2009-10-12', 'Sto. Nino', 'anitta@gmail.com', NULL),
(5, 'Disacula, Ma. Lhiana A.', '2010-03-19', 'Sta Rita', 'malhiana@gmail.com', NULL),
(6, 'Rena, Ainjeal M.', '2003-07-15', 'San Pascual', 'ainjeal@gmail.com', NULL),
(7, 'Mendoza, Angel Rymndza S.', '2005-11-25', 'Alangilan', 'angelrymn@gmail.com', NULL),
(8, 'Cordova, Joyce Ellaine D,', '2002-10-28', 'Sto. Domingo', 'joycellaine@gmail.com', NULL),
(9, 'Carag, Jiro Nino Angelo A.', '2011-10-01', 'Malalim', 'jirocarag@gmail.com', NULL),
(10, 'Erlano, Alexis Nicole M.', '2008-04-10', 'Bauan', 'alexis@gmail.com', NULL),
(26, 'Green, Rachel Karen M.', '2005-05-05', 'Alangilan', 'rachel@gmail.com', NULL),
(28, 'Asi, Jan Daniel P.', '2007-03-16', 'Conde Labac', 'daniel@gmail.com', NULL),
(34, 'Gonzales, Cassandra Shaine', '2005-07-27', 'Conde Labac', 'shaine@gmail.com', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`StudentID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `StudentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
