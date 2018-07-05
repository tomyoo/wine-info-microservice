# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.21)
# Database: compendium
# Generation Time: 2018-07-03 18:27:04 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE=''NO_AUTO_VALUE_ON_ZERO'' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table brands
# ------------------------------------------------------------

LOCK TABLES `brands` WRITE;
/*!40000 ALTER TABLE `brands` DISABLE KEYS */;

INSERT INTO `brands` (`id`, `name`)
VALUES
	(1,''Test Brand'');

/*!40000 ALTER TABLE `brands` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table classifications
# ------------------------------------------------------------

LOCK TABLES `classifications` WRITE;
/*!40000 ALTER TABLE `classifications` DISABLE KEYS */;

INSERT INTO `classifications` (`id`, `name`, `type`)
VALUES
	(1,''Test Red Classification'',''red''),
	(2,''Test White Classification'',''white'');

/*!40000 ALTER TABLE `classifications` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table grapes
# ------------------------------------------------------------

LOCK TABLES `grapes` WRITE;
/*!40000 ALTER TABLE `grapes` DISABLE KEYS */;

INSERT INTO `grapes` (`id`, `name`)
VALUES
	(1,''Test Grape 1''),
	(2,''Test Grape 2''),
	(3,''Test Grape 3'');

/*!40000 ALTER TABLE `grapes` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table pairings
# ------------------------------------------------------------

LOCK TABLES `pairings` WRITE;
/*!40000 ALTER TABLE `pairings` DISABLE KEYS */;

INSERT INTO `pairings` (`id`, `name`)
VALUES
	(1,''Test Pairing 1''),
	(2,''Test Pairing 2''),
	(3,''Test Pairing 3'');

/*!40000 ALTER TABLE `pairings` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table regions
# ------------------------------------------------------------

LOCK TABLES `regions` WRITE;
/*!40000 ALTER TABLE `regions` DISABLE KEYS */;

INSERT INTO `regions` (`id`, `name`, `parent_id`)
VALUES
	(1,''Test Parent'',NULL),
	(2,''Test Child'',2);

/*!40000 ALTER TABLE `regions` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table tastes
# ------------------------------------------------------------

LOCK TABLES `tastes` WRITE;
/*!40000 ALTER TABLE `tastes` DISABLE KEYS */;

INSERT INTO `tastes` (`id`, `name`)
VALUES
	(1,''Test Taste 1''),
	(2,''Test Taste 2''),
	(3,''Test Taste 3'');

/*!40000 ALTER TABLE `tastes` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table traits
# ------------------------------------------------------------

LOCK TABLES `traits` WRITE;
/*!40000 ALTER TABLE `traits` DISABLE KEYS */;

INSERT INTO `traits` (`id`, `name`)
VALUES
	(1,''Test Trait 1''),
	(2,''Test Trait 2''),
	(3,''Test Trait 3'');

/*!40000 ALTER TABLE `traits` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table varieties
# ------------------------------------------------------------

LOCK TABLES `varieties` WRITE;
/*!40000 ALTER TABLE `varieties` DISABLE KEYS */;

INSERT INTO `varieties` (`id`, `name`, `type`)
VALUES
	(1,''Test Red Variety'',''red''),
	(2,''Test White Variety'',''white'');

/*!40000 ALTER TABLE `varieties` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table vintages
# ------------------------------------------------------------

LOCK TABLES `vintages` WRITE;
/*!40000 ALTER TABLE `vintages` DISABLE KEYS */;

INSERT INTO `vintages` (`id`, `year`, `abv`, `tasting_note`, `short_tasting_note`, `body`, `fruit`, `earth`, `tannin`, `oak`, `acidity`, `region_id`, `wine_id`)
VALUES
	(1,2018,12.5,''Viral asymmetrical kinfolk, gluten-free single-origin coffee squid marfa drinking vinegar selvage mlkshk jianbing adaptogen chia. Sriracha pabst biodiesel photo booth fixie hot chicken selfies lomo. Godard lumbersexual cray kombucha aesthetic you probably haven\''t heard of them man bun bushwick selvage offal. Ramps pop-up etsy neutra trust fund aesthetic mustache taxidermy. Intelligentsia next level tofu microdosing unicorn, kickstarter raw denim flexitarian snackwave literally helvetica.'',''Viral asymmetrical kinfolk, gluten-free single-origin coffee squid marfa drinking vinegar selvage mlkshk jianbing adaptogen chia.'',1,2,3,4,5,4,2,1),
	(2,2018,12.5,''YOLO street art wolf jianbing sustainable hot chicken woke hammock retro. Blue bottle fam copper mug, four dollar toast distillery helvetica cornhole. Try-hard wolf polaroid, listicle +1 XOXO before they sold out gentrify actually irony food truck. Offal cronut photo booth ugh austin four loko copper mug truffaut fingerstache letterpress fixie yr meh actually. Selfies heirloom franzen taxidermy.'',''YOLO street art wolf jianbing sustainable hot chicken woke hammock retro. Blue bottle fam copper mug, four dollar toast distillery helvetica cornhole.'',4,5,4,3,2,1,2,2);

/*!40000 ALTER TABLE `vintages` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table vintages_grapes
# ------------------------------------------------------------

LOCK TABLES `vintages_grapes` WRITE;
/*!40000 ALTER TABLE `vintages_grapes` DISABLE KEYS */;

INSERT INTO `vintages_grapes` (`grape_id`, `vintage_id`)
VALUES
	(1,1),
	(2,1),
	(3,2),
	(2,2);

/*!40000 ALTER TABLE `vintages_grapes` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table vintages_pairings
# ------------------------------------------------------------

LOCK TABLES `vintages_pairings` WRITE;
/*!40000 ALTER TABLE `vintages_pairings` DISABLE KEYS */;

INSERT INTO `vintages_pairings` (`vintage_id`, `pairing_id`)
VALUES
	(1,1),
	(1,2),
	(1,3),
	(2,1),
	(2,2),
	(2,3);

/*!40000 ALTER TABLE `vintages_pairings` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table vintages_tastes
# ------------------------------------------------------------

LOCK TABLES `vintages_tastes` WRITE;
/*!40000 ALTER TABLE `vintages_tastes` DISABLE KEYS */;

INSERT INTO `vintages_tastes` (`vintage_id`, `taste_id`)
VALUES
	(1,1),
	(1,2),
	(1,3),
	(2,1),
	(2,2),
	(2,3);

/*!40000 ALTER TABLE `vintages_tastes` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table vintages_traits
# ------------------------------------------------------------

LOCK TABLES `vintages_traits` WRITE;
/*!40000 ALTER TABLE `vintages_traits` DISABLE KEYS */;

INSERT INTO `vintages_traits` (`trait_id`, `vintage_id`)
VALUES
	(3,1),
	(2,1),
	(1,1),
	(1,2),
	(2,2),
	(3,2);

/*!40000 ALTER TABLE `vintages_traits` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table wines
# ------------------------------------------------------------

LOCK TABLES `wines` WRITE;
/*!40000 ALTER TABLE `wines` DISABLE KEYS */;

INSERT INTO `wines` (`id`, `name`, `brand_id`, `variety_id`, `classification_id`)
VALUES
	(1,''Test Red Wine'',1,1,1),
	(2,''Test White Wine'',1,2,2);

/*!40000 ALTER TABLE `wines` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
