from django.db import models


class Subject(models.Model):
    """学科模型
    包含编号、名称、介绍、成立日期和一个标志位表示是否为热门学科。
    """
    no = models.IntegerField(primary_key=True, verbose_name='编号')  # 学科编号，作为主键
    name = models.CharField(max_length=20, verbose_name='名称')  # 学科名称
    intro = models.CharField(max_length=20, default='', verbose_name='介绍')  # 学科介绍
    create_date = models.DateField(null=True, verbose_name='成立日期')  # 成立日期，可以为空
    is_hot = models.BooleanField(default=False, verbose_name='是否热门')  # 是否是热门学科

    def __str__(self):

        return self.name  # 返回学科名称作为模型的字符串表示

    class Meta:
        db_table = 'tb_subject'  # 数据库表名
        verbose_name = '学科'  # 单数形式名称
        verbose_name_plural = '学科'  # 复数形式名称


class Teacher(models.Model):
    """老师模型
    包含编号、姓名、详情、照片、好评数、差评数以及所属学科的外键关联。
    """
    no = models.AutoField(primary_key=True, verbose_name='编号')  # 老师编号，自动增长主键
    name = models.CharField(max_length=20, verbose_name='姓名')  # 老师姓名
    detail = models.CharField(max_length=200, default='', blank=True, verbose_name='详情')  # 老师详情，可以为空
    photo = models.CharField(max_length=1023, default='', verbose_name='照片')  # 老师照片路径
    good_count = models.IntegerField(default=0, verbose_name='好评数')  # 好评数量，默认为0
    bad_count = models.IntegerField(default=0, verbose_name='差评数')  # 差评数量，默认为0
    subject = models.ForeignKey(to=Subject, on_delete=models.PROTECT, db_column='sno',
                                verbose_name='所属学科')  # 所属学科外键

    class Meta:
        db_table = 'tb_teacher'  # 数据库表名
        verbose_name = '老师'  # 单数形式名称
        verbose_name_plural = '老师'  # 复数形式名称
