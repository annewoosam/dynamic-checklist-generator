--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.1
-- Dumped by pg_dump version 9.5.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: animals; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE animals (
	animal_id integer NOT NULL,
	template_id integer NOT NULL,
	name character varying(50) NOT NULL,
	animal_species character varying(25) NOT NULL,
	birth_year integer
);


ALTER TABLE animals OWNER TO "vagrant";

--
-- Name: animals_animal_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE animals_animal_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE animals_animal_id_seq OWNER TO "vagrant";

--
-- Name: animals_animal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE animals_animal_id_seq OWNED BY animals.animal_id;


--
-- Name: templates; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE templates (
	template_id integer NOT NULL,
	templatename character varying(100) NOT NULL,
	createdby character varying(100) NOT NULL,
	createdon integer NOT NULL
);


ALTER TABLE templates OWNER TO "vagrant";

--
-- Name: templates_template_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE templates_template_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE templates_template_id_seq OWNER TO "vagrant";

--
-- Name: templates_template_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE templates_template_id_seq OWNED BY templates.template_id;


--
-- Name: animal_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY animals ALTER COLUMN animal_id SET DEFAULT nextval('animals_animal_id_seq'::regclass);


--
-- Name: template_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY templates ALTER COLUMN template_id SET DEFAULT nextval('templates_template_id_seq'::regclass);


--
-- Data for Name: animals; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY animals (animal_id, template_id, name, animal_species, birth_year) FROM stdin;
1	1	Fluffy	cat	2010
2	2	Squiggles	snake	2016
\.


--
-- Name: animals_animal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('animals_animal_id_seq', 12, true);


--
-- Data for Name: templates; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY templates (template_id, templatename, createdby, createdon) FROM stdin;
1	Compliance Testing	Anne Woo-Sam	2020
2	Client Guide	Anne Woo-Sam	2020
\.


--
-- Name: templates_template_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('templates_template_id_seq', 5, true);


--
-- Name: animals_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY animals
	ADD CONSTRAINT animals_pkey PRIMARY KEY (animal_id);


--
-- Name: templates_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY templates
	ADD CONSTRAINT templates_pkey PRIMARY KEY (template_id);


--
-- Name: animals_human_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY animals
	ADD CONSTRAINT animals_human_id_fkey FOREIGN KEY (template_id) REFERENCES templates(template_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

