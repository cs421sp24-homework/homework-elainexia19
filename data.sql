/*
 Navicat Premium Data Transfer

 Source Server         : qyay
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : 34.27.57.204:3306
 Source Schema         : data

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 17/02/2024 21:48:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for events
-- ----------------------------
DROP TABLE IF EXISTS `events`;
CREATE TABLE `events`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `organizer_id` int NOT NULL,
  `date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `code` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id`(`id` ASC) USING BTREE,
  INDEX `organizer_id`(`organizer_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of events
-- ----------------------------
INSERT INTO `events` VALUES (1, 'test_event', NULL, 1, '2024-02-17', '10:00:00', '23:00:00', '101010');
INSERT INTO `events` VALUES (10, 'event1', 'some description', 2, '2024-02-03', '22:21:00', '23:21:00', '809100');
INSERT INTO `events` VALUES (11, 'event2', 'test event', 2, '2024-02-04', '17:50:00', '19:50:00', '600151');
INSERT INTO `events` VALUES (12, 'event1', 'very long description very long description very long description very long description very long description very long description', 1, '2024-02-03', '23:11:00', '23:16:00', '901192');
INSERT INTO `events` VALUES (13, 'test', 'test', 5, '2024-02-06', '15:41:00', '17:41:00', '308183');
INSERT INTO `events` VALUES (14, 'test', 'test', 5, '2024-02-06', '15:41:00', '17:41:00', '206164');
INSERT INTO `events` VALUES (19, 'curr event', 'event that is currently live', 1, '2024-02-17', '15:24:00', '23:59:00', '1f0e3d');
INSERT INTO `events` VALUES (20, 'future event', 'event that is not live yet', 1, '2024-02-20', '15:25:00', '19:25:00', '98f137');

-- ----------------------------
-- Table structure for organizer
-- ----------------------------
DROP TABLE IF EXISTS `organizer`;
CREATE TABLE `organizer`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of organizer
-- ----------------------------
INSERT INTO `organizer` VALUES (1, 'john', 'qq1111', NULL);
INSERT INTO `organizer` VALUES (2, 'amy', 'ww2222', NULL);
INSERT INTO `organizer` VALUES (3, 'hello', 'hello333', 'hello@gmail.com');
INSERT INTO `organizer` VALUES (5, 'red', 'q1234', '');
INSERT INTO `organizer` VALUES (12, 'sam', 'ee3333', NULL);
INSERT INTO `organizer` VALUES (13, 'user', 'qq1234', NULL);
INSERT INTO `organizer` VALUES (14, 'user1', 'qq1234', NULL);

-- ----------------------------
-- Table structure for questions
-- ----------------------------
DROP TABLE IF EXISTS `questions`;
CREATE TABLE `questions`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `question` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `event_id` int NOT NULL,
  `votes` int NULL DEFAULT NULL,
  `answered` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 55 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of questions
-- ----------------------------
INSERT INTO `questions` VALUES (2, 'another test question', 1, 6, 1);
INSERT INTO `questions` VALUES (3, 'how are you?', 1, 9, 1);
INSERT INTO `questions` VALUES (4, 'fine thank you, and you?', 1, 3, 0);
INSERT INTO `questions` VALUES (6, 'very long question very long question very long question very long question very long question very long question very long question very long question very long question very long question', 1, 1, 0);
INSERT INTO `questions` VALUES (7, 'some other questions', 1, 0, 0);
INSERT INTO `questions` VALUES (23, 'post question', 1, 0, 0);
INSERT INTO `questions` VALUES (24, 'post question 2', 1, 0, 0);
INSERT INTO `questions` VALUES (25, 'post first question', 3, 0, 0);
INSERT INTO `questions` VALUES (26, 'post question', 13, 0, 0);
INSERT INTO `questions` VALUES (27, 'post question 2', 13, 0, 0);
INSERT INTO `questions` VALUES (44, 'test question', 1, 0, 0);
INSERT INTO `questions` VALUES (45, 'post question 3', 1, 0, 0);
INSERT INTO `questions` VALUES (46, 'post first question', 19, 1, 0);
INSERT INTO `questions` VALUES (47, 'post question 2', 19, 2, 0);
INSERT INTO `questions` VALUES (48, 'post a longer question, how you doing?', 19, 1, 0);
INSERT INTO `questions` VALUES (49, 'new question', 1, 0, 0);
INSERT INTO `questions` VALUES (50, 'i love cats and dogs', 1, 0, 0);
INSERT INTO `questions` VALUES (51, 'post an even longer question, how has your day been going?', 19, 3, 1);
INSERT INTO `questions` VALUES (52, 'post question 3', 19, 0, 0);
INSERT INTO `questions` VALUES (53, 'post question 4', 19, 0, 0);
INSERT INTO `questions` VALUES (54, 'another useless place holder', 1, 0, 0);

-- ----------------------------
-- View structure for event_organizer
-- ----------------------------
DROP VIEW IF EXISTS `event_organizer`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `event_organizer` AS select `events`.`id` AS `id`,`events`.`name` AS `name`,`events`.`description` AS `description`,`events`.`organizer_id` AS `organizer_id`,`events`.`date` AS `date`,`events`.`start_time` AS `start_time`,`events`.`end_time` AS `end_time`,`events`.`code` AS `code`,`organizer`.`username` AS `username`,`organizer`.`email` AS `email` from (`events` join `organizer`) where (`events`.`organizer_id` = `organizer`.`id`);

-- ----------------------------
-- View structure for event_questions
-- ----------------------------
DROP VIEW IF EXISTS `event_questions`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `event_questions` AS select `events`.`code` AS `code`,`questions`.`id` AS `id`,`questions`.`question` AS `question`,`questions`.`event_id` AS `event_id`,`questions`.`votes` AS `votes`,`questions`.`answered` AS `answered` from (`questions` join `events`) where (`events`.`id` = `questions`.`event_id`);

SET FOREIGN_KEY_CHECKS = 1;
