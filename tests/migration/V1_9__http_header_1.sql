-- AUTO-GENERATED BY igluctl DO NOT EDIT
-- Generator: igluctl 0.2.0
-- Generated: 2018-01-16 14:01

CREATE SCHEMA IF NOT EXISTS atomic;

CREATE TABLE IF NOT EXISTS atomic.org_ietf_http_header_1 (
    "schema_vendor"  VARCHAR(128)   NOT NULL,
    "schema_name"    VARCHAR(128)   NOT NULL,
    "schema_format"  VARCHAR(128)   NOT NULL,
    "schema_version" VARCHAR(128)   NOT NULL,
    "root_id"        CHAR(36)             NOT NULL,
    "root_tstamp"    TIMESTAMP            NOT NULL,
    "ref_root"       VARCHAR(255)   NOT NULL,
    "ref_tree"       VARCHAR(1500)  NOT NULL,
    "ref_parent"     VARCHAR(255)   NOT NULL,
    "name"           VARCHAR(4096)        NOT NULL,
    "value"          VARCHAR(4096)        NOT NULL,

    CONSTRAINT http_header_1__root_id_pk PRIMARY KEY(root_id),
    FOREIGN KEY (root_id) REFERENCES atomic.events(event_id)
);
-- DISTSTYLE KEY
-- DISTKEY (root_id)
-- SORTKEY (root_tstamp);

-- COMMENT ON TABLE atomic.org_ietf_http_header_1 IS 'iglu:org.ietf/http_header/jsonschema/1-0-0';
CREATE INDEX http_header_1__root_tstamp_idx ON atomic.org_ietf_http_header_1 (root_tstamp);

