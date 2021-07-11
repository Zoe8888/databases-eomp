-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: LC_Academy
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Admin_SignIn`
--

DROP TABLE IF EXISTS `Admin_SignIn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Admin_SignIn` (
  `id` varchar(13) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(10) NOT NULL,
  PRIMARY KEY (`password`),
  KEY `id` (`id`),
  CONSTRAINT `Admin_SignIn_ibfk_1` FOREIGN KEY (`id`) REFERENCES `User_Info` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_SignIn`
--

LOCK TABLES `Admin_SignIn` WRITE;
/*!40000 ALTER TABLE `Admin_SignIn` DISABLE KEYS */;
INSERT INTO `Admin_SignIn` VALUES ('9903200072086','zoeerispe7@gmail.com','passw0rd');
/*!40000 ALTER TABLE `Admin_SignIn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NextOfKin`
--

DROP TABLE IF EXISTS `NextOfKin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NextOfKin` (
  `kinName` varchar(30) NOT NULL,
  `kinNumber` varchar(10) DEFAULT NULL,
  `id` varchar(13) NOT NULL,
  PRIMARY KEY (`kinName`),
  KEY `id` (`id`),
  CONSTRAINT `NextOfKin_ibfk_1` FOREIGN KEY (`id`) REFERENCES `User_Info` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NextOfKin`
--

LOCK TABLES `NextOfKin` WRITE;
/*!40000 ALTER TABLE `NextOfKin` DISABLE KEYS */;
INSERT INTO `NextOfKin` VALUES ('Chelsea Erispe','0612345790','9903200072086'),('Dillan Wasserfall','0824615793','9504265148082'),('Donnavon Erispe','0715946283','0012085583081'),('Janine Plandt','0842135799','9904240072086'),('Jesse Terblanche','0814523670','9811145170081');
/*!40000 ALTER TABLE `NextOfKin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SignIn`
--

DROP TABLE IF EXISTS `SignIn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SignIn` (
  `name` varchar(20) NOT NULL,
  `surname` varchar(20) NOT NULL,
  `id` varchar(13) NOT NULL,
  `date` date DEFAULT NULL,
  `time_in` time DEFAULT NULL,
  `time_out` time DEFAULT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SignIn`
--

LOCK TABLES `SignIn` WRITE;
/*!40000 ALTER TABLE `SignIn` DISABLE KEYS */;
INSERT INTO `SignIn` VALUES ('Zoe','Erispe','9903200072086','2021-07-07','08:16:18','10:48:35'),('Zoe','Erispe','9903200072086','2021-07-08','08:16:18','10:48:35'),('Zoe','Erispe','9903200072086','2021-07-08','08:16:18','10:48:35'),('Alex','Joshua','9904240072086','2021-07-09','13:17:14','13:18:19'),('Ronald','Terblanche','9811145170081','2021-07-09','11:57:24','14:51:16'),('Fioana','Erispe','0012085583081','2021-07-11','10:26:37','16:00:00'),('Nicole','Wasserfall','9504265148082',NULL,'08:15:18','17:48:35');
/*!40000 ALTER TABLE `SignIn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_Info`
--

DROP TABLE IF EXISTS `User_Info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_Info` (
  `name` varchar(20) NOT NULL,
  `surname` varchar(20) NOT NULL,
  `id` varchar(13) NOT NULL,
  `email` varchar(60) NOT NULL,
  `number` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_Info`
--

LOCK TABLES `User_Info` WRITE;
/*!40000 ALTER TABLE `User_Info` DISABLE KEYS */;
INSERT INTO `User_Info` VALUES ('Fioana','Erispe','0012085583081','fionae@live.co.za','0761239544'),('Nicole','Wasserfall','9504265148082','nicolewasserfall@gmail.com','0846213577'),('Ronald','Terblanche','9811145170081','ronaldterblanche@gmail.com','0875746122'),('Zoe','Erispe','9903200072086','zoeerispe7@gmail.com','0862135040'),('Alex','Joshua','9904240072086','alexjoshua@gmail.com','0754863320');
/*!40000 ALTER TABLE `User_Info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-11 17:46:47
