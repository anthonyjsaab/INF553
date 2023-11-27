# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArticaleGrant(models.Model):
    artical = models.OneToOneField('PubmedArticle', models.DO_NOTHING, primary_key=True)  # The composite primary key (artical_id, grant_id) found, that is not supported. The first column is selected.
    grant = models.ForeignKey('GrantInfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'articale_grant'
        unique_together = (('artical', 'grant'),)


class ArticleAuthor(models.Model):
    article = models.ForeignKey('PubmedArticle', models.DO_NOTHING, primary_key=True)  # The composite primary key (article_id, author id) found, that is not supported. The first column is selected.
    author_id = models.ForeignKey('PubmedAuthor', models.DO_NOTHING, db_column='author id')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'article_author'


class ArticleCoi(models.Model):
    article = models.ForeignKey('PubmedArticle', models.DO_NOTHING, blank=True, null=True)
    coi_id = models.IntegerField(primary_key=True)
    coi_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_coi'


class GrantInfo(models.Model):
    grant_id = models.IntegerField(primary_key=True)
    grant_val = models.TextField()

    class Meta:
        managed = False
        db_table = 'grant_info'


class PubmedAffiliation(models.Model):
    affil_id = models.IntegerField(primary_key=True)
    norm_affil = models.TextField()

    class Meta:
        managed = False
        db_table = 'pubmed_affiliation'


class PubmedArticle(models.Model):
    article_id = models.IntegerField(primary_key=True)
    title = models.TextField()
    journal_title = models.TextField(db_column='journal title')  # Field renamed to remove unsuitable characters.
    field_doi = models.TextField(db_column=' doi')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    pubmed_link = models.TextField(db_column='pubmed link')  # Field renamed to remove unsuitable characters.
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pubmed_article'


class PubmedAuthor(models.Model):
    author_id = models.IntegerField(primary_key=True)
    author_name = models.TextField()
    field_affil = models.ForeignKey(PubmedAffiliation, models.DO_NOTHING, db_column=' affil_id', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'pubmed_author'
