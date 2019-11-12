create database jing_dong charset = utf8;
use jing_dong;
create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(150) not null,
    cate_name varchar(40) not null,     -- 分类
    brand_name varchar(40) not null,    -- 品牌
    price decimal(10,3) not null,
    is_show bit not null default 1,     -- 是否显示
    is_saleoff bit not null default 0   -- 是否卖光
);


insert into goods values (0, 'r510vc 15.6英寸笔记本', '笔记本', '华硕', '3399', default, default);
insert into goods values(0, 'y400n 14.0英寸笔记本电脑', '笔记本', '联想', '4999', default, default);
insert into goods values(0, 'g150th 15.6英寸游戏本', '笔记本', '雷神', '8499', default, default);
insert into goods values(0, 'x550cc 15.6英寸笔记本', '笔记本', '华硕', '2799', default, default);
insert into goods values(0, 'x240 超极本', '超级本', '联想', '4880', default, default);
insert into goods values(0, 'u330p 13.3英寸超级本', '超级本', '联想', '4299', default, default);
insert into goods values(0, 'svp13226scb 触控超级本', '超级本', '索尼', '7999', default, default);
insert into goods values(0, 'ipad mini 7.9英寸平板电脑', '平板电脑', '苹果', '1998', default, default);
insert into goods values(0, 'ipad air 9.7英寸平板电脑', '平板电脑', '苹果', '3388', default, default);
insert into goods values(0, 'ipad mini 配备 retina 显示屏', '平板电脑', '苹果', '2788', default, default);
insert into goods values(0, 'ideacentre c340 20英寸一体电脑', '台式机', '联想', '3499', default, default);
insert into goods values(0, 'vostro 3800-r1206 台式电脑', '台式机', '戴尔', '2899', default, default);
insert into goods values(0, 'imac me086ch/a 21.5英寸一体电脑', '台式机', '苹果', '9188', default, default);
insert into goods values(0, 'at7-7414lp 台式电脑 linux）', '台式机', '宏碁', '3699', default, default);
insert into goods values(0, 'z220sff f4f06pa工作站', '服务器/工作站', '惠普', '4288', default, default);
insert into goods values(0, 'poweredge ii服务器', '服务器/工作站', '戴尔', '5388', default, default);
insert into goods values(0, 'mac pro专业级台式电脑', '服务器/工作站', '苹果', '28888', default, default);
insert into goods values(0, 'hmz-t3w 头戴显示设备', '笔记本配件', '索尼', '6999', default, default);
insert into goods values(0, '商务双肩背包', '笔记本配件', '索尼', '99', default, default);
insert into goods values(0, 'x3250 m4机架式服务器', '服务器/工作站', 'ibm', '6888', default, default);
insert into goods values(0, '商务双肩背包', '笔记本配件', '索尼', '99', default, default);


select *
from (select cate_name, max(price) as max_price from goods group by cate_name) as g_new
    left join goods as g
    on g_new.cate_name = g.cate_name and g_new.max_price=g.price;


update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name=c.id;


alter table goods change cate_name cate_id int unsigned not null;

alter table goods add foreign key (cate_id) references goods_cates(id);

insert into goods(name, cate_id, brand_name,price) values ('LaserJet Pro P1606dn 黑白激光打印机',12, 4, '1849');

-- 创建并插入数据
create table goods_brands(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
) select brand_name as name from goods group by brand_name;

-- 通过goods_brands数据表来更新goods数据表
update goods as g inner join goods_brands as b on g.brand_name=b.name set g.brand_name=b.id;

-- 通过alter table语句修改表结构（即brand_name的属性）
alter table goods change brand_name brand_id int unsigned not null ;

-- 插入外键
alter table goods add foreign key (brand_id) references goods_brands(id);



-- 创建视图
select g.*, c.name as cate_name, b.name as brand_name from goods as g left join goods_cates as c on g.cate_id = c.id left join goods_brands as b on g.brand_id = b.id;

-- 事务     原子性，一致性， 隔离性， 持久性
begin;

commit;

-- 索引     类似python中的字典    提高查询效率
-- 索引的使用
-- show index from 表名;
-- create index xxxxx(索引名) on xxx(表名) ((字段（10));  -- 10为字段属性长度

-- 账户管理
    -- 添加账户
    create user "youngc"@"%" identified by "ycmysql";
    grant select on `jing_dong.*` to "youngc"@"%" ;     -- select 表示查询权限  insert  表示插入权限  -- update  修改权限  -- delete  删除权限
    grant select,insert,update on `*.*` to "youngc"@"%" ;
    -- 添加所有权限
    grant all privileges on *.* to "youngc"@"%";        -- all privileges 表示所有权限

    -- 修改密码
    update user set authentication_string=password("mysql") where user="root";  -- 目前无法修改