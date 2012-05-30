-- MySQL dump 10.13  Distrib 5.1.61, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: db_uv
-- ------------------------------------------------------
-- Server version	5.1.61

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
-- Table structure for table `tbl_content_action`
--

CREATE DATABASE IF NOT EXISTS uv_core;

USE uv_core;

DROP TABLE IF EXISTS `tbl_content_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_content_action` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `content_id` int(10) NOT NULL,
  `source` int(10) NOT NULL,
  `destination` int(10) NOT NULL,
  `action_type` tinyint(4) NOT NULL COMMENT '1-Like, 2-Comment, 3-Reply, 4-Forward, 5-Share',
  `created_ts` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`),
  KEY `follower_feed_fk_2` (`source`,`destination`),
  KEY `message_id_index` (`content_id`),
  KEY `created_ts_index` (`created_ts`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tbl_subscription`
--

DROP TABLE IF EXISTS `tbl_subscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_subscription` (
  `msisdn` int(10) unsigned NOT NULL,
  `device_id` varchar(45) DEFAULT NULL,
  `service_id` int(11) unsigned DEFAULT NULL,
  `subs_status` tinyint(4) NOT NULL COMMENT '1-Pending, 2-Subscribed ,3-Unsubscribed, 4-Expired, 5-Cancelled',
  `start_ts` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `expire_ts` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `renewal_ts` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `cancelled_ts` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `channel` tinyint(4) NOT NULL COMMENT '1-IVR, 2-SMS, 3-USSD, 4-WEB, 5-OBD',
  `created_ts` datetime NOT NULL,
  `updated_ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`msisdn`),
  UNIQUE KEY `tbl_subscription_uk_1` (`msisdn`,`service_id`),
  KEY `tbl_subscription_fk_2` (`service_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tbl_user_profile`
--

DROP TABLE IF EXISTS `tbl_user_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user_profile` (
  `msisdn` varchar(45) NOT NULL DEFAULT '0',
  `user_name` varchar(100) NOT NULL,
  `email_id` varchar(200) DEFAULT NULL,
  `display_name` varchar(40) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `location` char(2) NOT NULL DEFAULT 'SG' COMMENT 'ISO2 country codes',
  `channel` tinyint(4) NOT NULL COMMENT 'facebook-21, twitter-22, bubbly.net-23, iphone-24, android-25',
  `device_id` varchar(45) DEFAULT NULL COMMENT 'applicable for bubbly apps installed in devices',
  `user_desc` varchar(512) DEFAULT NULL,
  `profile_url` varchar(120) DEFAULT NULL COMMENT 'profile url',
  `intro_audio_url` varchar(120) DEFAULT NULL COMMENT 'introduction audio url',
  `image_url` varchar(120) DEFAULT NULL COMMENT 'profile avatar image',
  `created_ts` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1-New, 2-Active, 3-Disabled, 4-Deleted',
  `blogger_type` tinyint(4) NOT NULL DEFAULT '2' COMMENT '1-premium, 2-community',
  `follower_count` int(11) DEFAULT '0',
  `following_count` int(11) DEFAULT '0',
  `current_location` varchar(160) DEFAULT NULL,
  `facebook_token` varchar(260) DEFAULT NULL,
  `twitter_token` varchar(260) DEFAULT NULL,
  `twitter_token_secret` varchar(260) DEFAULT NULL,
  `facebook_id` varchar(100) DEFAULT NULL COMMENT 'facebook account id',
  `twitter_id` int(11) DEFAULT '-1',
  `facebook_username` varchar(160) DEFAULT NULL,
  `facebook_screenname` varchar(160) DEFAULT NULL,
  `twitter_username` varchar(160) DEFAULT NULL,
  `twitter_screenname` varchar(160) DEFAULT NULL,
  `telco_follower_count` int(11) unsigned NOT NULL DEFAULT '0',
  `operator_id` varchar(45) NOT NULL,
  `lang_notify` varchar(40) DEFAULT NULL,
  `notify_email_addr` varchar(100) DEFAULT NULL,
  `notify_new_msg` tinyint(1) NOT NULL DEFAULT '1',
  `lang` varchar(40) DEFAULT NULL,
  `fwd_to` varchar(20) DEFAULT NULL,
  `fwd_email_addr` varchar(100) DEFAULT NULL,
  `fwd_phone_no` varchar(20) DEFAULT NULL,
  `notify_pref` varchar(30) DEFAULT NULL,
  `new_inbox_size` int(10) NOT NULL DEFAULT '10',
  `heard_inbox_size` int(10) NOT NULL DEFAULT '10',
  `save_inbox_size` int(10) NOT NULL DEFAULT '10',
  `def_inbox_ttl` int(10) DEFAULT NULL,
  `def_save_ttl` int(10) DEFAULT NULL,
  `privacy` text,
  `block_list` text,
  PRIMARY KEY (`msisdn`),
  UNIQUE KEY `msi_loc` (`msisdn`,`location`),
  UNIQUE KEY `up_uk_3` (`email_id`),
  KEY `FK_user_profile_country_1` (`location`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tbl_service_charge`
--

DROP TABLE IF EXISTS `tbl_service_charge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_service_charge` (
  `service_id` int(10) DEFAULT NULL,
  `plan_id` int(10) DEFAULT NULL,
  `channel` varchar(4) DEFAULT NULL COMMENT '1-IVR, 2-SMS, 3-USSD, 4-WEB, 5-OBD',
  `duration` int(10) DEFAULT NULL,
  `price` int(10) DEFAULT NULL,
  `start_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `end_date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `status` tinyint(4) DEFAULT NULL COMMENT '0-disable,1-enable',
  `action` tinyint(4) DEFAULT NULL COMMENT '1-Sub, 2-Renewal',
  `remarks` varchar(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tbl_services`
--

DROP TABLE IF EXISTS `tbl_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_services` (
  `service_id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT NULL,
  `service_group` varchar(10) DEFAULT NULL,
  `desc` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

--
-- Table structure for table `tbl_number_normalizer`
--

DROP TABLE IF EXISTS `tbl_number_normalizer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_number_normalizer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `in_pattern` varchar(40) NOT NULL,
  `out_pattern` varchar(40) NOT NULL,
  `telco_id` varchar(20) NOT NULL,
  `channel` varchar(20) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-05-27 19:59:04
