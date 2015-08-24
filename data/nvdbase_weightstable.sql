-- MySQL dump 10.13  Distrib 5.6.23, for Win64 (x86_64)
--
-- Host: localhost    Database: nvdbase
-- ------------------------------------------------------
-- Server version	5.6.25-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `weightstable`
--

DROP TABLE IF EXISTS `weightstable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weightstable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `xnone` double DEFAULT NULL,
  `xpartial` double DEFAULT NULL,
  `xcomplete` double DEFAULT NULL,
  `ynone` double DEFAULT NULL,
  `ypartial` double DEFAULT NULL,
  `ycomplete` double DEFAULT NULL,
  `znone` double DEFAULT NULL,
  `zpartial` double DEFAULT NULL,
  `zcomplete` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weightstable`
--

LOCK TABLES `weightstable` WRITE;
/*!40000 ALTER TABLE `weightstable` DISABLE KEYS */;
INSERT INTO `weightstable` VALUES (1,'WIVSS1',0,1.9,3.8,0,1,2,0,0.6,1.2),(2,'WIVSS2',0,1.8,3.6,0,1.1,2.2,0,0.6,1.2),(3,'WIVSS3',0,1.8,3.6,0,1,2,0,0.7,1.4),(4,'WIVSS4',0,1.7,3.4,0,1.1,2.2,0,0.7,1.4),(5,'WIVSS5',0,1.6,3.2,0,1.2,2.4,0,0.7,1.4),(6,'WIVSS6',0,1.5,3,0,1.3,2.6,0,0.7,1.4),(7,'WIVSS7',0,1.7,3.4,0,1,2,0,0.8,1.6),(8,'WIVSS8',0,1.5,3,0,1.2,2.4,0,0.8,1.6),(9,'WIVSS9',0,1.4,2.8,0,1.3,2.6,0,0.8,1.6),(10,'WIVSS10',0,1.6,3.2,0,1,2,0,0.9,1.8),(11,'WIVSS11',0,1.5,3,0,1.1,2.2,0,0.9,1.8),(12,'WIVSS12',0,1.4,2.8,0,1.2,2.4,0,0.9,1.8),(13,'WIVSS13',0,1.4,2.8,0,1.1,2.2,0,1,2),(14,'WIVSS14',0,1.3,2.6,0,1.2,2.4,0,1,2);
/*!40000 ALTER TABLE `weightstable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-24 21:54:06
