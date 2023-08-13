
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for login
-- ----------------------------
DROP TABLE IF EXISTS `login`;
CREATE TABLE `login`  (
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `remember` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT ''
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of login
-- ----------------------------
INSERT INTO `login` VALUES ('admin', 'password', '1');
INSERT INTO `login` VALUES ('hzp', '123', '');
INSERT INTO `login` VALUES ('123', '123', '');

-- ----------------------------
-- Table structure for questions
-- ----------------------------
DROP TABLE IF EXISTS `questions`;
CREATE TABLE `questions`  (
  `id` int(11) NOT NULL,
  `question` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `option1` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `option2` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `option3` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `option4` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `correct_answer` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of questions
-- ----------------------------
INSERT INTO `questions` VALUES (1, 'Who was the first man landed on the moon?', 'Yuri Gagarin', 'Neil Armstrong', 'Buzz Aldrin', 'Alan Shepard', 'Neil Armstrong');
INSERT INTO `questions` VALUES (2, 'Which is the fastest plane in the world', 'X-43', 'X-15A-2', 'YF-12', 'Mig-25', 'X-43');
INSERT INTO `questions` VALUES (3, 'Which country first proposed a plan to explore the inner Earth?', 'USSR', 'US', 'UK', 'IRAQ', 'USSR');
INSERT INTO `questions` VALUES (4, 'When was the first computer invented?', '1946', '1971', '1942', '1960', '1946');

-- ----------------------------
-- Table structure for register
-- ----------------------------
DROP TABLE IF EXISTS `register`;
CREATE TABLE `register`  (
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `confirm_password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `age` int(11) NOT NULL,
  `mail` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of register
-- ----------------------------
INSERT INTO `register` VALUES ('hzp', '123', '123', 'Male', 20, '1968596879@qq.com');
INSERT INTO `register` VALUES ('123', '123', '123', 'Male', 20, '1948586958@qq.comnan');

SET FOREIGN_KEY_CHECKS = 1;