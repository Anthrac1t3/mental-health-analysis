DROP TABLE IF EXISTS public.alone;

CREATE TABLE IF NOT EXISTS public.alone
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT alone_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.alone
    OWNER to project;

COMMENT ON TABLE public.alone
    IS 'Tweets found by the keyword "alone"';

DROP TABLE IF EXISTS public.blissful;

CREATE TABLE IF NOT EXISTS public.blissful
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT blissful_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.blissful
    OWNER to project;

COMMENT ON TABLE public.blissful
    IS 'Tweets found by the keyword "blissful"';

DROP TABLE IF EXISTS public.bored;

CREATE TABLE IF NOT EXISTS public.bored
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT bored_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.bored
    OWNER to project;

COMMENT ON TABLE public.bored
    IS 'Tweets found by the keyword "bored"';

DROP TABLE IF EXISTS public.depressed;

CREATE TABLE IF NOT EXISTS public.depressed
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT depressed_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.depressed
    OWNER to project;

COMMENT ON TABLE public.depressed
    IS 'Tweets found by the keyword "depressed"';

DROP TABLE IF EXISTS public.food;

CREATE TABLE IF NOT EXISTS public.food
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT food_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.food
    OWNER to project;

COMMENT ON TABLE public.food
    IS 'Tweets found by the keyword "food"';

DROP TABLE IF EXISTS public.happy;

CREATE TABLE IF NOT EXISTS public.happy
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT happy_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.happy
    OWNER to project;

COMMENT ON TABLE public.happy
    IS 'Tweets found by the keyword "happy"';

DROP TABLE IF EXISTS public.joyful;

CREATE TABLE IF NOT EXISTS public.joyful
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT joyful_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.joyful
    OWNER to project;

COMMENT ON TABLE public.joyful
    IS 'Tweets found by the keyword "joyful"';

DROP TABLE IF EXISTS public.loneliness;

CREATE TABLE IF NOT EXISTS public.loneliness
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT loneliness_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.loneliness
    OWNER to project;

COMMENT ON TABLE public.loneliness
    IS 'Tweets found by the keyword "loneliness"';

DROP TABLE IF EXISTS public.outing;

CREATE TABLE IF NOT EXISTS public.outing
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT outing_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.outing
    OWNER to project;

COMMENT ON TABLE public.outing
    IS 'Tweets found by the keyword "outing"';

DROP TABLE IF EXISTS public.sad;

CREATE TABLE IF NOT EXISTS public.sad
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT sad_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.sad
    OWNER to project;

COMMENT ON TABLE public.sad
    IS 'Tweets found by the keyword "sad"';

DROP TABLE IF EXISTS public.snack;

CREATE TABLE IF NOT EXISTS public.snack
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT snack_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.snack
    OWNER to project;

COMMENT ON TABLE public.snack
    IS 'Tweets found by the keyword "snack"';

DROP TABLE IF EXISTS public.stressed;

CREATE TABLE IF NOT EXISTS public.stressed
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT stressed_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.stressed
    OWNER to project;

COMMENT ON TABLE public.stressed
    IS 'Tweets found by the keyword "stressed"';

DROP TABLE IF EXISTS public.travel;

CREATE TABLE IF NOT EXISTS public.travel
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT travel_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.travel
    OWNER to project;

COMMENT ON TABLE public.travel
    IS 'Tweets found by the keyword "travel"';

DROP TABLE IF EXISTS public.vacation;

CREATE TABLE IF NOT EXISTS public.vacation
(
    time_stamp timestamp with time zone NOT NULL,
    tweet_id bigint NOT NULL,
    content text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default" NOT NULL,
    mood text COLLATE pg_catalog."default",
    CONSTRAINT vacation_pkey PRIMARY KEY (tweet_id, author)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.vacation
    OWNER to project;

COMMENT ON TABLE public.vacation
    IS 'Tweets found by the keyword "vacation"';

