/*
 Navicat Premium Data Transfer

 Source Server         : Local
 Source Server Type    : MySQL
 Source Server Version : 80030 (8.0.30)
 Source Host           : localhost:3306
 Source Schema         : assets

 Target Server Type    : MySQL
 Target Server Version : 80030 (8.0.30)
 File Encoding         : 65001

 Date: 15/05/2023 12:36:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for asset_transactions
-- ----------------------------
DROP TABLE IF EXISTS `asset_transactions`;
CREATE TABLE `asset_transactions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `src_wallet_id` bigint NULL DEFAULT NULL,
  `src_asset_id` bigint NULL DEFAULT NULL,
  `dest_wallet_id` bigint NULL DEFAULT NULL,
  `dest_asset_id` bigint NULL DEFAULT NULL,
  `amount` decimal(16, 8) NULL DEFAULT NULL,
  `gas_fee` decimal(16, 8) NULL DEFAULT NULL,
  `total` decimal(16, 8) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of asset_transactions
-- ----------------------------
INSERT INTO `asset_transactions` VALUES (3, 5, 1, 7, 3, 20000.20000000, 10500.50000000, 30500.70000000);

-- ----------------------------
-- Table structure for assets
-- ----------------------------
DROP TABLE IF EXISTS `assets`;
CREATE TABLE `assets`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `wallet_id` bigint NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `symbol` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `network` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `address` varchar(42) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `balance` decimal(16, 8) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of assets
-- ----------------------------
INSERT INTO `assets` VALUES (1, 5, 'Rumah', 'Rp.', '192.168.1.49:9898', 'Depok', 1998888.23000000);
INSERT INTO `assets` VALUES (3, 7, 'Emas', 'Rp.', '192.168.1.49:9898', 'Jakarta', 90000.20000000);

-- ----------------------------
-- Table structure for wallets
-- ----------------------------
DROP TABLE IF EXISTS `wallets`;
CREATE TABLE `wallets`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of wallets
-- ----------------------------
INSERT INTO `wallets` VALUES (5, 'Rafi Fathur R');
INSERT INTO `wallets` VALUES (6, 'Abi Ahmad');
INSERT INTO `wallets` VALUES (7, 'Ravi Haryo');

SET FOREIGN_KEY_CHECKS = 1;
