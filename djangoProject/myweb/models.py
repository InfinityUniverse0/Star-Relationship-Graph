from django.db import models


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class 主演(models.Model):
    person = models.ForeignKey('人物', models.DO_NOTHING, db_column='person', primary_key=True)
    works = models.ForeignKey('影视作品', models.DO_NOTHING, db_column='works')

    class Meta:
        managed = True
        db_table = '主演'
        unique_together = (('person', 'works'),)


    def __repr__(self):
        return f'<主演: {self.person.name}|{self.works.name}>'


class 亲属(models.Model):
    person1 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person1',
                                primary_key=True, related_name='亲属1')
    person2 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person2'
                                , related_name='亲属2')

    class Meta:
        managed = True
        db_table = '亲属'
        unique_together = (('person1', 'person2'),)

    def __repr__(self):
        return f'<亲属: {self.person1.name}|{self.person2.name}>'


class 人物(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=8, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = '人物'

    def __repr__(self):
        return f'<人物: {self.name}>'


class 好友(models.Model):
    person1 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person1',
                                primary_key=True, related_name='好友1')
    person2 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person2'
                                , related_name='好友2')

    class Meta:
        managed = True
        db_table = '好友'
        unique_together = (('person1', 'person2'),)

    def __repr__(self):
        return f'<好友: {self.person1.name}|{self.person2.name}>'


class 影视作品(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    director = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=64, blank=True, null=True)
    pub_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = '影视作品'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<影视作品: {self.name}>'


class 恋人(models.Model):
    person1 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person1',
                                primary_key=True, related_name='恋人1')
    person2 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person2',
                                unique=True, related_name='恋人2')

    class Meta:
        managed = True
        db_table = '恋人'
        unique_together = (('person1', 'person2'),)

    def __repr__(self):
        return f'<恋人: {self.person1.name}|{self.person2.name}>'


class 旧爱(models.Model):
    person1 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person1',
                                primary_key=True, related_name='旧爱1')
    person2 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person2'
                                , related_name='旧爱2')

    class Meta:
        managed = True
        db_table = '旧爱'
        unique_together = (('person1', 'person2'),)

    def __repr__(self):
        return f'<旧爱: {self.person1.name}|{self.person2.name}>'


class 歌手(models.Model):
    id = models.ForeignKey('人物', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = True
        db_table = '歌手'

    def __str__(self):
        return self.id.name

    def __repr__(self):
        return f'<歌手: {self.id.name}>'


class 歌曲(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    singer = models.ForeignKey('人物', models.DO_NOTHING, db_column='singer')

    class Meta:
        managed = True
        db_table = '歌曲'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<歌曲: {self.name}>'


class 演员(models.Model):
    id = models.ForeignKey('人物', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = True
        db_table = '演员'

    def __str__(self):
        return self.id.name

    def __repr__(self):
        return f'<演员: {self.id.name}>'


class 离异(models.Model):
    person1 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person1',
                                primary_key=True, related_name='离异1')
    person2 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person2'
                                , related_name='离异2')

    class Meta:
        managed = True
        db_table = '离异'
        unique_together = (('person1', 'person2'),)

    def __repr__(self):
        return f'<离异: {self.person1.name}|{self.person2.name}>'


class 绯闻(models.Model):
    person1 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person1',
                                primary_key=True, related_name='绯闻1')
    person2 = models.ForeignKey('人物', models.DO_NOTHING, db_column='person2'
                                , related_name='绯闻2')

    class Meta:
        managed = True
        db_table = '绯闻'
        unique_together = (('person1', 'person2'),)

    def __repr__(self):
        return f'<绯闻: {self.person1.name}|{self.person2.name}>'
