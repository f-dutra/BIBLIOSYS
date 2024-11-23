-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 23, 2024 at 02:52 AM
-- Server version: 11.5.2-MariaDB
-- PHP Version: 8.3.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `BIBLIOTECA`
--

-- --------------------------------------------------------

--
-- Table structure for table `alunos`
--

CREATE TABLE `alunos` (
  `id` int(11) DEFAULT NULL,
  `nome` varchar(60) DEFAULT NULL,
  `serie` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `emprestimo`
--

CREATE TABLE `emprestimo` (
  `id` int(11) DEFAULT NULL,
  `idAluno` int(11) DEFAULT NULL,
  `idLivro` int(11) DEFAULT NULL,
  `inicio` date DEFAULT NULL,
  `prazo` date DEFAULT NULL,
  `estado` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `livros`
--

CREATE TABLE `livros` (
  `id` int(11) DEFAULT NULL,
  `titulo` varchar(600) DEFAULT NULL,
  `genero` varchar(60) DEFAULT NULL,
  `autor` varchar(60) DEFAULT NULL,
  `acervo` varchar(20) DEFAULT NULL,
  `disponivel` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
