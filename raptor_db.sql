-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-09-2016 a las 00:04:50
-- Versión del servidor: 10.1.13-MariaDB
-- Versión de PHP: 7.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `raptor`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `getCache` (IN `_url` VARCHAR(300))  NO SQL
SELECT result FROM cache WHERE url = _url$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getDownloaUser` (IN `_user` INT)  NO SQL
SELECT id_track, fecha FROM descargas_x_usuario WHERE id_usuario = _user$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getLastDownload` (IN `_iduser` INT)  NO SQL
SELECT id_track FROM descargas_x_usuario 
WHERE id_usuario = _iduser
ORDER BY id_track DESC LIMIT 1$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertDownload` (IN `_user` VARCHAR(30), IN `_track` VARCHAR(30))  NO SQL
INSERT INTO descargas_x_usuario (id_track,id_usuario,fecha) VALUES (_track,_user, CURDATE( ) )$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertFaq` (IN `_id_user` INT, IN `_comentario` VARCHAR(599))  NO SQL
INSERT INTO faq (id_user,comentario,fecha) VALUES (_id_user,_comentario,CURDATE())$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertUser` (IN `_android_user` VARCHAR(20))  BEGIN
IF NOT EXISTS ( SELECT * FROM usuario WHERE android_id = _android_user ) THEN
	INSERT INTO usuario (android_id, ultima_con) VALUES (_android_user, NOW());
ELSE
	UPDATE usuario SET ultima_con = NOW() WHERE android_id = _android_user;
END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `setCache` (IN `_url` VARCHAR(300), IN `_result` MEDIUMTEXT)  NO SQL
INSERT INTO cache(url, result) VALUES (_url,_result)$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cache`
--

CREATE TABLE `cache` (
  `url` varchar(170) COLLATE utf8_bin NOT NULL,
  `result` longtext COLLATE utf8_bin
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `descargas_x_usuario`
--

CREATE TABLE `descargas_x_usuario` (
  `id_usuario` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `id_track` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `faq`
--

CREATE TABLE `faq` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `comentario` varchar(600) COLLATE utf8_spanish_ci NOT NULL,
  `fecha` date NOT NULL,
  `estado` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `playlist`
--

CREATE TABLE `playlist` (
  `id_playlist` int(11) NOT NULL,
  `id_user` varchar(20) NOT NULL,
  `nombre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `track_playlist`
--

CREATE TABLE `track_playlist` (
  `id_playlist` int(11) NOT NULL,
  `track_json` varchar(4000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `android_id` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `ultima_con` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cache`
--
ALTER TABLE `cache`
  ADD PRIMARY KEY (`url`);

--
-- Indices de la tabla `faq`
--
ALTER TABLE `faq`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `playlist`
--
ALTER TABLE `playlist`
  ADD PRIMARY KEY (`id_playlist`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `faq`
--
ALTER TABLE `faq`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `playlist`
--
ALTER TABLE `playlist`
  MODIFY `id_playlist` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
