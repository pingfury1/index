-- 2020-05-16

USE web_index;

-- table groups data

INSERT INTO groups (group_name) VALUES ('内部工作台'), ('运维工作台');

-- table items data

SET FOREIGN_KEY_CHECKS = 0;

INSERT INTO items (item_name,item_url,item_notice,item_logo_url,item_manual_name,item_manual_url,group_id)
VALUES
('Gitlab系统','https://about.gitlab.com/','Gitlab内部代码仓库','img/gitlab.png','帮助文档','https://docs.gitlab.com/ee/README.html',1),
('WIKI系统','https://www.atlassian.com/','文档系统','img/wiki.png','帮助文档','',1),
('禅道系统','https://www.zentao.net/','项目管理系统','img/chandao.png','帮助文档','',1),
('账户系统','https://www.openldap.org/','LDAP账户统一管理系统','img/ldap.svg','帮助文档','',1),
('开源运维平台','https://spug.qbangmang.com/login','Spug运维平台源码','img/github.png','演示地址','https://spug.qbangmang.com/login',2),
('监控报警','https://grafana.com/','Zabbix监控报警平台','img/zabbix.png','帮助文档', '',2),
('发布系统','https://jenkins.io/','Jenkins发布系统','img/jenkins.png','帮助文档', '',2),
('跳板机系统','http://www.jumpserver.org/','Jumpserver 跳板机系统','img/jumpserver.png','帮助文档','',2),
('数据库系统','http://yearning.io/','数据库审核平台','img/sql2.png','帮助文档','',2);

SET FOREIGN_KEY_CHECKS = 1;
