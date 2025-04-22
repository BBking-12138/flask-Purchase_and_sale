DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`(
    `id` INT NOT NULL AUTO_INCREMENT COMMENT '自增ID，主键',
    `username` VARCHAR(50) NOT NULL COMMENT '用户名',
    `sex` ENUM('男', '女', '其他') NOT NULL COMMENT '用户性别',
    `mobile` VARCHAR(20) DEFAULT NULL COMMENT '电话号码',
    `email` VARCHAR(100) DEFAULT NULL COMMENT '电子邮箱',
    `count` VARCHAR(255) NOT NULL COMMENT '登陆账号',
    `password` VARCHAR(512) NOT NULL COMMENT '登录密码',
    `identity` VARCHAR(100) DEFAULT NULL COMMENT '用户身份：管理员 招标单位 投标单位 评标员',
--     `company_name` VARCHAR(100) DEFAULT NULL COMMENT '单位名称',
-- 	`company_address` VARCHAR(100) DEFAULT NULL COMMENT '单位地址',
-- 	`project_name` VARCHAR(100) DEFAULT NULL COMMENT '项目名称',
	`create_time` datetime DEFAULT NULL COMMENT '创建时间',
	`is_deleted` TINYINT(1) DEFAULT 0 COMMENT '是否删除',
    PRIMARY KEY (`id`) USING BTREE,
    INDEX `INX_USERNAME` (username) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='用户';

INSERT INTO `user` VALUES (1, 'root', '男', '111111', '111@111', 'root', 'pbkdf2:sha256:50000$WuO0dDYG$bc6abb402d99663d82737a36898bc862d672465cece851764078845cb0445f25', '管理员', '2025-04-15 19:00:56', '0');

CREATE TABLE `status` (
  `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(30) NOT NULL COMMENT '状态类型',
  `code` VARCHAR(30) NOT NULL COMMENT '状态代码',
  `name` VARCHAR(50) NOT NULL COMMENT '状态名称',
  PRIMARY KEY (`id`),
  UNIQUE KEY `udx_status` (`type`,`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='状态字典表';

-- 初始化状态数据
INSERT INTO `status` (`type`, `code`, `name`) VALUES
-- 项目整体状态
('PROJECT', 'DRAFT', '草稿'),
('PROJECT', 'TENDERING', '招标中'),
('PROJECT', 'BIDDING', '投标中'),
('PROJECT', 'EVALUATING', '评标中'),
('PROJECT', 'COMPLETED', '已完成'),
-- 招标状态
('TENDER', 'PUBLISHED', '已发布'),
('TENDER', 'CLOSED', '已截止'),
-- 投标状态
('BID', 'SUBMITTED', '已投标'),
('BID', 'WITHDRAWN', '已撤回');

DROP TABLE IF EXISTS `project`;
CREATE TABLE `project` (
    `id` INT(10) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
    `project_number` VARCHAR(20) DEFAULT 0 COMMENT '项目编号',
    `project_name` VARCHAR(200) DEFAULT 0 COMMENT '项目名称',
    `project_introduction` TEXT COMMENT '项目简介',
     `notes` VARCHAR(500) DEFAULT NULL COMMENT '备注',
    `tender_unit` VARCHAR(100) DEFAULT NULL COMMENT '招标单位（创建人）',
    `tender_status` tinyint(1) DEFAULT '0' COMMENT '招标状态 0：招标中 1：已招标',
    `bid_unit` VARCHAR(100) DEFAULT NULL COMMENT '投标单位',
    `bid_status` tinyint(1) DEFAULT '0' COMMENT '投标状态 0：投标中 1：已投标',
    `status_id` SMALLINT UNSIGNED NOT NULL COMMENT '项目整体状态ID',
    `is_deleted` tinyint(1) DEFAULT '0' COMMENT '是否已删除,0:未删除;1:已删除',
    `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
	`update_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
     PRIMARY KEY (`id`),
     CONSTRAINT `fk_project_status` FOREIGN KEY (`status_id`) REFERENCES `status` (`id`)
) ENGINE=INNODB AUTO_INCREMENT=1 CHARACTER SET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='项目';

CREATE TABLE `project_evaluator` (
  `project_id` INT(10) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `evaluator_id` INT NOT NULL COMMENT '评标员ID',
  `evaluation_status` SMALLINT UNSIGNED NOT NULL COMMENT '评标状态ID',
  `score` DECIMAL(5,2) DEFAULT NULL COMMENT '评分',
  `evaluation_notes` TEXT COMMENT '评标意见',
  `evaluation_time` DATETIME DEFAULT NULL COMMENT '评标时间',
  PRIMARY KEY (`project_id`, `evaluator_id`),
  CONSTRAINT `fk_eval_project`
    FOREIGN KEY (`project_id`) REFERENCES `project` (`id`),
  CONSTRAINT `fk_eval_user`
    FOREIGN KEY (`evaluator_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='项目-评标员关联表';

INSERT  INTO project
VALUES
    (1,101, '办公用品招标', '笔记本电脑', '弄收缩啊擦受刺激哦','北京市政建设集团', 0, NULL, 0,(SELECT id FROM status WHERE code = 'TENDERING'), 0,'2024-01-15 09:30:00', '2024-01-15 09:30:00'),
    (2,202, '三农i啊女u', '苹果笔记本电脑', 'V在vvv在','上海医疗集团', 1, '腾讯医疗事业部', 1,(SELECT id FROM status WHERE code = 'BIDDING'), 0,'2024-01-15 09:30:00', '2024-01-15 09:30:00');

CREATE TABLE `notice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `notice_title` varchar(255) DEFAULT NULL COMMENT '公告标题',
  `notice_content` varchar(500) DEFAULT NULL COMMENT '公告内容',
  `notice_desc` varchar(255) DEFAULT NULL COMMENT '备注',
  `is_pin` tinyint(1) DEFAULT NULL COMMENT '是否置顶 0:未置顶；1:已置顶',
  `is_deleted` tinyint(1) DEFAULT '0' COMMENT '是否已删除,0:未删除;1:已删除',
  `create_by` int DEFAULT NULL COMMENT '创建人',
  `update_by` int DEFAULT NULL COMMENT '修改人',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COMMENT='通知公告表';

# CREATE TABLE `status` (
#   `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
#   `type` VARCHAR(30) NOT NULL COMMENT '状态类型',
#   `code` VARCHAR(30) NOT NULL COMMENT '状态代码',
#   `name` VARCHAR(50) NOT NULL COMMENT '状态名称',
#   PRIMARY KEY (`id`),
#   UNIQUE KEY `udx_status` (`type`,`code`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='状态字典表';
#
# -- 初始化状态数据
# INSERT INTO `status` (`type`, `code`, `name`) VALUES
# -- 项目整体状态
# ('PROJECT', 'DRAFT', '草稿'),
# ('PROJECT', 'TENDERING', '招标中'),
# ('PROJECT', 'BIDDING', '投标中'),
# ('PROJECT', 'EVALUATING', '评标中'),
# ('PROJECT', 'COMPLETED', '已完成'),
# -- 招标状态
# ('TENDER', 'PUBLISHED', '已发布'),
# ('TENDER', 'CLOSED', '已截止'),
# -- 投标状态
# ('BID', 'SUBMITTED', '已投标'),
# ('BID', 'WITHDRAWN', '已撤回');

# INSERT  INTO project
# VALUES
#     (1,101, '办公用品招标', '笔记本电脑', '弄收缩啊擦受刺激哦','北京市政建设集团', 0, NULL, 0,(SELECT id FROM status WHERE code = 'TENDERING'), 0,'2024-01-15 09:30:00', '2024-01-15 09:30:00'),
#     (2,202, '三农i啊女u', '苹果笔记本电脑', 'V在vvv在','上海医疗集团', 1, '腾讯医疗事业部', 1,(SELECT id FROM status WHERE code = 'BIDDING'), 0,'2024-01-15 09:30:00', '2024-01-15 09:30:00');


# DROP TABLE IF EXISTS `user`;
# CREATE TABLE `user`(
#     `id` INT NOT NULL AUTO_INCREMENT COMMENT '自增ID，主键',
#     `username` VARCHAR(50) NOT NULL COMMENT '用户名',
#     `sex` ENUM('男', '女', '其他') NOT NULL COMMENT '用户性别',
#     `mobile` VARCHAR(20) DEFAULT NULL COMMENT '电话号码',
#     `email` VARCHAR(100) DEFAULT NULL COMMENT '电子邮箱',
#     `count` VARCHAR(255) NOT NULL COMMENT '登陆账号',
#     `password` VARCHAR(512) NOT NULL COMMENT '登录密码',
#     `identity` VARCHAR(100) DEFAULT NULL COMMENT '用户身份：管理员 招标单位 投标单位 评标员',
# --     `company_name` VARCHAR(100) DEFAULT NULL COMMENT '单位名称',
# -- 	`company_address` VARCHAR(100) DEFAULT NULL COMMENT '单位地址',
# -- 	`project_name` VARCHAR(100) DEFAULT NULL COMMENT '项目名称',
# 	`create_time` datetime DEFAULT NULL COMMENT '创建时间',
# 	`is_deleted` TINYINT(1) DEFAULT 0 COMMENT '是否删除',
#     PRIMARY KEY (`id`) USING BTREE,
#     INDEX `INX_USERNAME` (username) USING BTREE
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='用户';
#
# INSERT INTO `user` VALUES (1, 'root', '男', '111111', '111@111', 'root', 'pbkdf2:sha256:50000$WuO0dDYG$bc6abb402d99663d82737a36898bc862d672465cece851764078845cb0445f25', '管理员', '2025-04-15 19:00:56', '0');
