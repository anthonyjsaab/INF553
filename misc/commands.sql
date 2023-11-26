--Peter Farah
--Anthony Saab
CREATE TABLE articale_grant
(
    artical_id integer NOT NULL,
    grant_id integer NOT NULL,
	CONSTRAINT articale_grant_pkey PRIMARY KEY (artical_id, grant_id)
);
CREATE TABLE article_author
(
    article_id integer NOT NULL,
    "author id" integer NOT NULL,
	CONSTRAINT article_author_pkey PRIMARY KEY (article_id, "author id")
);
CREATE TABLE grant_info
(
    grant_id integer NOT NULL,
    grant_val text NOT NULL,
    CONSTRAINT grant_info_pkey PRIMARY KEY (grant_id)
);
CREATE TABLE pubmed_affiliation
(
    affil_id integer NOT NULL,
    norm_affil text NOT NULL,
    CONSTRAINT "pubmed affiliation_pkey" PRIMARY KEY (affil_id)
);
CREATE TABLE pubmed_author
(
    author_id integer NOT NULL,
    author_name text NOT NULL,
    " affil_id" integer,
    CONSTRAINT "pubmed author_pkey" PRIMARY KEY (author_id)
);
CREATE TABLE pubmed_article
(
    "article_id" integer NOT NULL,
    title text NOT NULL,
    "journal title" text NOT NULL,
    " doi" text NOT NULL,
    "pubmed link" text NOT NULL,
    year integer NOT NULL,
    CONSTRAINT pubmed_article_pkey PRIMARY KEY ("article_id")
);
CREATE TABLE article_coi
(
    article_id integer,
    coi_id integer NOT NULL,
    coi_text text,
    CONSTRAINT article_coi_pkey PRIMARY KEY (coi_id)
);
COPY article_author FROM '/home/PUBMED_DATA/article_author.csv' CSV HEADER;
COPY article_coi FROM '/home/PUBMED_DATA/article_coi.csv' CSV HEADER;
COPY articale_grant FROM '/home/PUBMED_DATA/article_grant.csv' CSV HEADER;
COPY grant_info FROM '/home/PUBMED_DATA/grant_info.csv' CSV HEADER;
COPY pubmed_affiliation FROM '/home/PUBMED_DATA/pubmed_affiliation.csv' CSV HEADER;
COPY pubmed_article FROM '/home/PUBMED_DATA/pubmed_article.csv' CSV HEADER;
COPY pubmed_author FROM '/home/PUBMED_DATA/pubmed_author.csv' CSV HEADER;
ALTER TABLE articale_grant
    ADD CONSTRAINT articale_grant_artical_id_fkey FOREIGN KEY (artical_id)
        REFERENCES pubmed_article ("article_id") MATCH SIMPLE,
    ADD CONSTRAINT articale_grant_grant_id_fkey FOREIGN KEY (grant_id)
        REFERENCES grant_info (grant_id) MATCH SIMPLE;

ALTER TABLE article_author
    ADD CONSTRAINT " author id" FOREIGN KEY ("author id")
        REFERENCES pubmed_author (author_id) MATCH SIMPLE,
    ADD CONSTRAINT article_author_article_id_fkey FOREIGN KEY (article_id)
        REFERENCES pubmed_article ("article_id") MATCH SIMPLE;

ALTER TABLE pubmed_author
	ADD CONSTRAINT "pubmed author_ affil_id_fkey" FOREIGN KEY (" affil_id")
        REFERENCES pubmed_affiliation (affil_id) MATCH SIMPLE;

ALTER TABLE article_coi
        ADD CONSTRAINT article_coi_article_id_fkey FOREIGN KEY (article_id)
        REFERENCES public.pubmed_article (article_id) MATCH SIMPLE