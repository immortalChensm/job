/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 50719
Source Host           : localhost:3306
Source Database       : python

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2018-04-15 23:57:08
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for zl_job
-- ----------------------------
DROP TABLE IF EXISTS `zl_job`;
CREATE TABLE `zl_job` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `position` varchar(100) DEFAULT NULL,
  `salary` varchar(100) DEFAULT NULL,
  `work_location` varchar(255) DEFAULT NULL,
  `work_attribute` varchar(100) DEFAULT NULL,
  `experience_year` varchar(100) DEFAULT NULL,
  `education` varchar(100) DEFAULT NULL,
  `job_num` varchar(100) DEFAULT NULL,
  `job_type` varchar(100) DEFAULT NULL,
  `job_details` text,
  `company_details` text,
  `company_name` varchar(255) DEFAULT '',
  `company_attribute` varchar(100) DEFAULT NULL,
  `company_scale` varchar(100) DEFAULT NULL,
  `company_position` varchar(100) DEFAULT NULL,
  `company_address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12075 DEFAULT CHARSET=utf8;
