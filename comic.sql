SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `comic`;
CREATE TABLE `comic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comic_id` int(11) NOT NULL,
  `author` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `intr` varchar(500) DEFAULT NULL,
  `last_short_title` varchar(100) DEFAULT NULL,
  `cover` varchar(100) NOT NULL,
  `comic_url` varchar(100) DEFAULT NULL,
  `comic_type` varchar(20) DEFAULT NULL,
  `styles` varchar(200) DEFAULT NULL,
  
  `isDelete` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
-- ,UNIQUE KEY `unique_key` (`comic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `comic_chapter`;

CREATE TABLE `comic_chapter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comic_id` int(11) NOT NULL,
  `chapter_id` int(11) NOT NULL,
  `short_title` varchar(100) DEFAULT NULL,
  `urls` LONGTEXT DEFAULT NULL,
  `paths` LONGTEXT DEFAULT NULL,
  `title` varchar(400) DEFAULT NULL,
  `pub_time` datetime DEFAULT NULL,
  `isDelete` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

