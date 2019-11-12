-- 数据的准备
    -- 创建一个数据库
    create database python_test charset = utf8;

    -- 使用一个数据库
    use python_test;

    -- 显示使用的当前数据是哪个？
    select database();

    -- 创建一个数据表
    create table students(
        id int unsigned primary key auto_increment not null,
        name varchar(20) default '',
        age tinyint unsigned default 0,
        height decimal(5,2),
        gender enum("男","女","中性","保密") default '保密',
        cls_id int unsigned default 0,
        is_delete bit default 0
    );

    create table classes(
        id int unsigned primary key auto_increment not null,
        name varchar(30) not null
    );

    -- 准备数据
    -- 向students表插入数据
    insert into students values(0,'小明',18, 180.00, 2, 1, 0),
                                (0,'小月月',18, 180.00, 2, 2, 1),
                                (0,'彭于晏',29, 185.00, 1, 1, 0),
                                (0,'刘德华',59, 175.00, 1, 2, 1),
                                (0,'黄蓉',38, 160.00, 2, 1, 0),
                                (0,'凤姐',28, 150.00, 4, 2, 0),
                                (0,'王祖贤',18, 172.00, 2, 1, 1),
                                (0,'周杰伦',36, NULL, 1, 1, 0),
                                (0,'程坤',27, 181.00, 1, 2, 0),
                                (0,'刘亦菲',25, 166.00, 2, 2, 0),
                                (0,'金星',33, 162.00, 3, 3, 1),
                                (0,'静香',12, 180.00, 2, 1, 0),
                                (0,'郭靖',12, 170.00, 1, 1, 0),
                                (0,'周杰',34, 176.00, 2, 5, 0);

    -- 向classes表中插入数据
    insert into classes values(0,'python_01期'),(0,'python_02期');
-- 查询

    -- 查询所有字段
    -- select * from 表名;
    select * from students;
    select * from classes;
    select id, name from classes;

    -- 查询指定字段
    select name, age from students;
    select students.name, students.age from students;

    -- 使用 as 给字段起别名
    select name as 姓名, age as 年龄 from students;

    -- 可以通过 as 给表起别名
    select s.name, s.age from students as s;
    -- 起别名后，失败的使用select students.name, students.age from students as s;

    -- 消除重复行
    -- distinct 字段
    select distinct gender from students;

-- 条件查询
    -- 比较运算符
        -- select ... from 表名 where ...
        -- >
        -- 查询大于18岁的信息
        select * from students where age>18;

        -- <  >=  <=  !=/<>

        -- =
        -- 查询年龄为18岁的所有学生的名字
        select * from students where age = 18;

    -- 逻辑运算符
        -- and
        -- 18到28之间的所有学生信息
        select * from students where age>18 and age<28;

        -- or

        -- not  使用括号解决优先级问题

    -- 模糊查询
        -- like
        -- % 替换1个或多个
        -- _ 替换一个
        -- 查询姓名中以 小开始的名字
        select name from students where name like "小%";
        -- 查询姓名中包含 小字 的名字
        select name from students where name like "%小%";

        -- 查询有2个字的名字
        select name from students where name like "__";

        -- 查询至少有2个字的名字
        select name from students where name like "__%";


        -- rlike  正则
        -- 查询以周开始的姓名
        select name from students where name rlike "^周.*";

        -- 查询以周开始、伦结尾的姓名
        select name from students where name rlike "^周.*伦$";

    -- 范围查询
        -- in

        -- not in
        select name, age from students where age not in (12, 18, 34);

        -- between ... and ... 表示在一个连续范围之内，  包括边界值

        -- not between ... and ... 表示不在一个连续范围之内  属于一种用法不能在not后加括号

    -- 空判断
        -- 判空 is null

        -- 判非空 is not null


-- 排序

    -- order by 字段
    -- asc 从小到大排列， 即升序
    select * from students where (age between 18 and 34) and gender=1 order by age asc;
    -- desc 从大到小排序， 即降序


    -- order by 多个字段
    select * from students where (age between 18 and 34) and gender=1 order by age desc,id desc;

-- 聚合函数
    -- 总数
    -- count
    select count(*) as 男性人数 from students where gender=1;


    -- 最大值
    -- max

    -- 最小值
    -- min

    -- 求和
    -- sum

    -- 平均值
    -- avg

    -- 四舍五入 round(123.23, 1) 保留一位小数
    select round(sum(age)/count(*), 2) from students;

-- 分组   与聚合搭配使用才有意义

    -- group by
    -- select ... from students group by gender;
    select gender from students group by gender;

    -- 计算每种性别中的数量
    select gender, count(*) from students group by gender;  -- 此时的count(*) 是为每个分组计算数量

    -- 计算每种性别中的数量，同时显示姓名
    select gender, group_concat(name) from students group by gender;

    -- 计算男性的数量，同时显示姓名
    -- group_contact(...)
    select gender,count(*), group_concat(name,'_',age,"_", id) from students where gender=1 group by gender;

    -- having 过滤
    -- 查询平均年龄超过30岁的性别，以及姓名 having avg(age) > 30
    select gender, group_concat(name), avg(age) from students group by gender having avg(age)>30;


-- 分页   一般在sql语句最后排
    -- limit start， count
    select * from students where gender=1 limit 2, 2;
    -- 限制分页数量
    select * from students where gender=1 limit 2;



-- 链接查询    多个表之间的关联查询
    -- 内链接
    -- inner join ... on
    select * from students inner join classes;  -- 语法正确，但查询结果非正常

    -- 查询 有能够对应班级的学生以及班级信息
    select * from students inner join classes on students.cls_id=classes.id;

    -- 按照要求显示班级和姓名
    select students.*, classes.name from students inner join classes on students.cls_id=classes.id;

    -- 给数据表起名字
    select s.*, c.name from students as s inner join classes as c on s.cls_id=c.id;

    -- 左链接 left join
    select * from students as s left join classes as c on s.cls_id=c.id;
    select * from students as s left join classes as c on s.cls_id=c.id having c.id is null;

    -- 右链接 right join


-- 自关联   多个表合为一张表，并在这个表内部实现关联，例如：省市县三级关联

    select province.atitle, city.atitle from areas as province inner join areas as city on city.pid = province.aid having province.atitle='河北省';


-- 子查询
    -- 标量子查询

    -- 查询最高的男生信息
    select * from students where height = (select max(height) from students);







