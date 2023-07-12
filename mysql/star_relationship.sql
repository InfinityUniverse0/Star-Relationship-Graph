/*
 Navicat Premium Data Transfer

 Source Server         : hyf
 Source Server Type    : MySQL
 Source Server Version : 80032
 Source Host           : localhost:3306
 Source Schema         : star_relationship

 Target Server Type    : MySQL
 Target Server Version : 80032
 File Encoding         : 65001

 Date: 12/07/2023 17:17:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 主演
-- ----------------------------
DROP TABLE IF EXISTS `主演`;
CREATE TABLE `主演`  (
  `person` bigint(0) UNSIGNED NOT NULL,
  `works` bigint(0) UNSIGNED NOT NULL,
  PRIMARY KEY (`person`, `works`) USING BTREE,
  INDEX `works`(`works`) USING BTREE,
  CONSTRAINT `主演_ibfk_1` FOREIGN KEY (`person`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `主演_ibfk_2` FOREIGN KEY (`works`) REFERENCES `影视作品` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 主演
-- ----------------------------
INSERT INTO `主演` VALUES (3, 1);
INSERT INTO `主演` VALUES (1, 2);
INSERT INTO `主演` VALUES (5, 3);
INSERT INTO `主演` VALUES (12, 4);
INSERT INTO `主演` VALUES (5, 5);
INSERT INTO `主演` VALUES (1, 6);
INSERT INTO `主演` VALUES (1, 7);
INSERT INTO `主演` VALUES (3, 7);
INSERT INTO `主演` VALUES (15, 8);

-- ----------------------------
-- Table structure for 亲属
-- ----------------------------
DROP TABLE IF EXISTS `亲属`;
CREATE TABLE `亲属`  (
  `person1` bigint(0) UNSIGNED NOT NULL,
  `person2` bigint(0) UNSIGNED NOT NULL,
  PRIMARY KEY (`person1`, `person2`) USING BTREE,
  INDEX `person2`(`person2`) USING BTREE,
  CONSTRAINT `亲属_ibfk_1` FOREIGN KEY (`person1`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `亲属_ibfk_2` FOREIGN KEY (`person2`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 亲属
-- ----------------------------
INSERT INTO `亲属` VALUES (13, 9);
INSERT INTO `亲属` VALUES (13, 12);
INSERT INTO `亲属` VALUES (9, 13);
INSERT INTO `亲属` VALUES (12, 13);

-- ----------------------------
-- Table structure for 人物
-- ----------------------------
DROP TABLE IF EXISTS `人物`;
CREATE TABLE `人物`  (
  `id` bigint(0) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `gender` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `birth_date` date NULL DEFAULT NULL,
  `nationality` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 人物
-- ----------------------------
INSERT INTO `人物` VALUES (1, '谢霆锋', '男', '1980-08-29', '中国', '华语流行乐男歌手、演员、音乐创作人、制作人、主持人、青年企业家，PO朝霆创始人。');
INSERT INTO `人物` VALUES (2, '王菲', '女', '1969-08-08', '中国', '华语流行乐女歌手、演员 ，中国国家一级演员 。');
INSERT INTO `人物` VALUES (3, '陈冠希', '男', '1980-10-07', '加拿大', '拥有八分之一葡萄牙血统 ，加拿大籍华语男歌手、演员、商人。 ');
INSERT INTO `人物` VALUES (4, '李亚鹏', '男', '1971-09-27', '中国', '毕业于中央戏剧学院表演系，中国内地男演员、公益人士。');
INSERT INTO `人物` VALUES (5, '张柏芝', '女', '1980-05-24', '中国', '出生中国香港，毕业于澳大利亚Rmit Holmes College，中国香港女演员、歌手。');
INSERT INTO `人物` VALUES (6, '周迅', '女', '1974-10-18', '中国', '毕业于浙江艺术学校，中国内地女演员、歌手。');
INSERT INTO `人物` VALUES (7, '张亚东', '男', '1969-03-11', '中国', '中国内地男音乐制作人、歌手、导演。他是一个非常全能的音乐人，在不同的音乐领域和风格上均有建树');
INSERT INTO `人物` VALUES (8, '瞿颖', '女', '1971-07-02', '中国', '毕业于湖南省艺术学校话剧班，国际超模、演员、歌手');
INSERT INTO `人物` VALUES (9, '窦鹏', '男', '1978-01-01', '中国', '毕业于中央音乐学院，中国内地男歌手、音乐制作人');
INSERT INTO `人物` VALUES (10, '朴树', '男', '1973-11-08', '中国', '出生于江苏省南京市，籍贯北京市，中国内地男歌手、音乐制作人、影视演员');
INSERT INTO `人物` VALUES (11, '李大齐', '男', '1970-03-04', '中国', '出生于中国台湾台北，毕业于纽约帕森斯学院，中国台湾男造型师、设计师、演艺DJ');
INSERT INTO `人物` VALUES (12, '窦颖', '女', '1972-01-01', '中国', '中国内地女歌手，吸引力合唱组前成员');
INSERT INTO `人物` VALUES (13, '窦唯', '男', '1969-10-14', '中国', '出生于北京，中国摇滚乐男歌手、实验音乐人');
INSERT INTO `人物` VALUES (14, '张杰', '男', '1982-12-20', '中国', '出生于四川省成都市，中国流行男歌手');
INSERT INTO `人物` VALUES (15, '谢娜', '女', '1981-05-06', '中国', '出生于四川省德阳市中江县，毕业于四川师范大学电影电视学院表演系，中国内地主持人、歌手、演员');

-- ----------------------------
-- Table structure for 好友
-- ----------------------------
DROP TABLE IF EXISTS `好友`;
CREATE TABLE `好友`  (
  `person1` bigint(0) UNSIGNED NOT NULL,
  `person2` bigint(0) UNSIGNED NOT NULL,
  PRIMARY KEY (`person1`, `person2`) USING BTREE,
  INDEX `person2`(`person2`) USING BTREE,
  CONSTRAINT `好友_ibfk_1` FOREIGN KEY (`person1`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `好友_ibfk_2` FOREIGN KEY (`person2`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 好友
-- ----------------------------
INSERT INTO `好友` VALUES (3, 1);
INSERT INTO `好友` VALUES (1, 3);

-- ----------------------------
-- Table structure for 影视作品
-- ----------------------------
DROP TABLE IF EXISTS `影视作品`;
CREATE TABLE `影视作品`  (
  `id` bigint(0) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `director` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `type` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `pub_date` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 影视作品
-- ----------------------------
INSERT INTO `影视作品` VALUES (1, '《无间道》', '麦兆辉', '电影', '2002-12-12');
INSERT INTO `影视作品` VALUES (2, '《证人》', '林超贤', '电影', '2008-11-20');
INSERT INTO `影视作品` VALUES (3, '《乘风破浪的姐姐第二季》', '晏吉', '综艺', '2021-01-22');
INSERT INTO `影视作品` VALUES (4, '《激荡时代》', '文韬', '电视剧', '2010-01-01');
INSERT INTO `影视作品` VALUES (5, '《如果，爱》', '张哲书', '电视剧', '2018-05-27');
INSERT INTO `影视作品` VALUES (6, '《怒火·重案》', '陈木胜', '电影', '2021-07-30');
INSERT INTO `影视作品` VALUES (7, '《飞龙再生》', '陈嘉上', '电影', '2003-08-15');
INSERT INTO `影视作品` VALUES (8, '《快乐大本营》', '刘伟', '综艺', '1997-07-11');

-- ----------------------------
-- Table structure for 恋人
-- ----------------------------
DROP TABLE IF EXISTS `恋人`;
CREATE TABLE `恋人`  (
  `person1` bigint(0) UNSIGNED NOT NULL,
  `person2` bigint(0) UNSIGNED NOT NULL,
  PRIMARY KEY (`person1`, `person2`) USING BTREE,
  UNIQUE INDEX `person1`(`person1`) USING BTREE,
  UNIQUE INDEX `person2`(`person2`) USING BTREE,
  CONSTRAINT `恋人_ibfk_1` FOREIGN KEY (`person1`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `恋人_ibfk_2` FOREIGN KEY (`person2`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 恋人
-- ----------------------------
INSERT INTO `恋人` VALUES (14, 15);
INSERT INTO `恋人` VALUES (15, 14);

-- ----------------------------
-- Table structure for 旧爱
-- ----------------------------
DROP TABLE IF EXISTS `旧爱`;
CREATE TABLE `旧爱`  (
  `person1` bigint(0) UNSIGNED NOT NULL,
  `person2` bigint(0) UNSIGNED NOT NULL,
  PRIMARY KEY (`person1`, `person2`) USING BTREE,
  INDEX `person2`(`person2`) USING BTREE,
  CONSTRAINT `旧爱_ibfk_1` FOREIGN KEY (`person1`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `旧爱_ibfk_2` FOREIGN KEY (`person2`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 旧爱
-- ----------------------------
INSERT INTO `旧爱` VALUES (2, 1);
INSERT INTO `旧爱` VALUES (1, 2);
INSERT INTO `旧爱` VALUES (5, 3);
INSERT INTO `旧爱` VALUES (6, 4);
INSERT INTO `旧爱` VALUES (8, 4);
INSERT INTO `旧爱` VALUES (3, 5);
INSERT INTO `旧爱` VALUES (4, 6);
INSERT INTO `旧爱` VALUES (9, 6);
INSERT INTO `旧爱` VALUES (10, 6);
INSERT INTO `旧爱` VALUES (11, 6);
INSERT INTO `旧爱` VALUES (8, 7);
INSERT INTO `旧爱` VALUES (4, 8);
INSERT INTO `旧爱` VALUES (7, 8);
INSERT INTO `旧爱` VALUES (6, 9);
INSERT INTO `旧爱` VALUES (6, 10);
INSERT INTO `旧爱` VALUES (6, 11);

-- ----------------------------
-- Table structure for 歌手
-- ----------------------------
DROP TABLE IF EXISTS `歌手`;
CREATE TABLE `歌手`  (
  `id` bigint(0) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  CONSTRAINT `歌手_ibfk_1` FOREIGN KEY (`id`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 歌手
-- ----------------------------
INSERT INTO `歌手` VALUES (1);
INSERT INTO `歌手` VALUES (2);
INSERT INTO `歌手` VALUES (3);
INSERT INTO `歌手` VALUES (5);
INSERT INTO `歌手` VALUES (6);
INSERT INTO `歌手` VALUES (7);
INSERT INTO `歌手` VALUES (8);
INSERT INTO `歌手` VALUES (9);
INSERT INTO `歌手` VALUES (10);
INSERT INTO `歌手` VALUES (11);
INSERT INTO `歌手` VALUES (12);
INSERT INTO `歌手` VALUES (13);
INSERT INTO `歌手` VALUES (14);

-- ----------------------------
-- Table structure for 歌曲
-- ----------------------------
DROP TABLE IF EXISTS `歌曲`;
CREATE TABLE `歌曲`  (
  `id` bigint(0) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `singer` bigint(0) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `singer`(`singer`) USING BTREE,
  CONSTRAINT `歌曲_ibfk_1` FOREIGN KEY (`singer`) REFERENCES `歌手` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 歌曲
-- ----------------------------
INSERT INTO `歌曲` VALUES (1, '《传奇》', 2);
INSERT INTO `歌曲` VALUES (2, '《匆匆那年》', 2);
INSERT INTO `歌曲` VALUES (3, '《平凡之路》', 10);
INSERT INTO `歌曲` VALUES (4, '《生如夏花》', 10);
INSERT INTO `歌曲` VALUES (5, '《篝火》', 6);
INSERT INTO `歌曲` VALUES (6, '《悲伤的梦》', 13);
INSERT INTO `歌曲` VALUES (7, '《流年》', 2);
INSERT INTO `歌曲` VALUES (8, '《逆战》', 14);
INSERT INTO `歌曲` VALUES (9, '《剑心》', 14);

-- ----------------------------
-- Table structure for 演员
-- ----------------------------
DROP TABLE IF EXISTS `演员`;
CREATE TABLE `演员`  (
  `id` bigint(0) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  CONSTRAINT `演员_ibfk_1` FOREIGN KEY (`id`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 演员
-- ----------------------------
INSERT INTO `演员` VALUES (1);
INSERT INTO `演员` VALUES (3);
INSERT INTO `演员` VALUES (4);
INSERT INTO `演员` VALUES (5);
INSERT INTO `演员` VALUES (6);
INSERT INTO `演员` VALUES (8);
INSERT INTO `演员` VALUES (12);
INSERT INTO `演员` VALUES (15);

-- ----------------------------
-- Table structure for 离异
-- ----------------------------
DROP TABLE IF EXISTS `离异`;
CREATE TABLE `离异`  (
  `person1` bigint(0) UNSIGNED NOT NULL,
  `person2` bigint(0) UNSIGNED NOT NULL,
  PRIMARY KEY (`person1`, `person2`) USING BTREE,
  INDEX `person2`(`person2`) USING BTREE,
  CONSTRAINT `离异_ibfk_1` FOREIGN KEY (`person1`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `离异_ibfk_2` FOREIGN KEY (`person2`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 离异
-- ----------------------------
INSERT INTO `离异` VALUES (5, 1);
INSERT INTO `离异` VALUES (4, 2);
INSERT INTO `离异` VALUES (13, 2);
INSERT INTO `离异` VALUES (2, 4);
INSERT INTO `离异` VALUES (1, 5);
INSERT INTO `离异` VALUES (12, 7);
INSERT INTO `离异` VALUES (7, 12);
INSERT INTO `离异` VALUES (2, 13);

-- ----------------------------
-- Table structure for 绯闻
-- ----------------------------
DROP TABLE IF EXISTS `绯闻`;
CREATE TABLE `绯闻`  (
  `person1` bigint(0) UNSIGNED NOT NULL,
  `person2` bigint(0) UNSIGNED NOT NULL,
  PRIMARY KEY (`person1`, `person2`) USING BTREE,
  INDEX `person2`(`person2`) USING BTREE,
  CONSTRAINT `绯闻_ibfk_1` FOREIGN KEY (`person1`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `绯闻_ibfk_2` FOREIGN KEY (`person2`) REFERENCES `人物` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 绯闻
-- ----------------------------
INSERT INTO `绯闻` VALUES (6, 1);
INSERT INTO `绯闻` VALUES (1, 6);

SET FOREIGN_KEY_CHECKS = 1;
