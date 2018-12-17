/*
Navicat MySQL Data Transfer

Source Server         : windows
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : comic

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-12-17 11:27:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for comic
-- ----------------------------
DROP TABLE IF EXISTS `comic`;
CREATE TABLE `comic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `intr` varchar(500) NOT NULL,
  `cover` varchar(100) NOT NULL,
  `comic_url` varchar(100) DEFAULT NULL,
  `comic_type` varchar(20) NOT NULL,
  `comic_type2` varchar(20) NOT NULL,
  `collection` int(11) NOT NULL,
  `recommend` int(11) NOT NULL,
  `praise` bigint(20) DEFAULT NULL,
  `roast` bigint(20) NOT NULL,
  `last_update_chapter` varchar(50) NOT NULL,
  `last_update_time` datetime NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  `add_time` datetime NOT NULL,
  `isDelete` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_key` (`name`,`author`)
) ENGINE=InnoDB AUTO_INCREMENT=1837 DEFAULT CHARSET=utf8;
