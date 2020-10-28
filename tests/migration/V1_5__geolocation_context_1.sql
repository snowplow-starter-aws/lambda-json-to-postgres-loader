-- Copyright (c) 2014 Snowplow Analytics Ltd. All rights reserved.
--
-- This program is licensed to you under the Apache License Version 2.0,
-- and you may not use this file except in compliance with the Apache License Version 2.0.
-- You may obtain a copy of the Apache License Version 2.0 at http://www.apache.org/licenses/LICENSE-2.0.
--
-- Unless required by applicable law or agreed to in writing,
-- software distributed under the Apache License Version 2.0 is distributed on an
-- "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the Apache License Version 2.0 for the specific language governing permissions and limitations there under.
--
-- Authors:       Alex Dean
-- Copyright:     Copyright (c) 2014 Snowplow Analytics Ltd
-- License:       Apache License Version 2.0
--
-- Compatibility: iglu:com.snowplowanalytics.snowplow/geolocation_context/jsonschema/1-0-0

CREATE TABLE atomic.com_snowplowanalytics_snowplow_geolocation_context_1 (
	-- Schema of this type
	schema_vendor  varchar(128)    not null,
	schema_name    varchar(128)    not null,
	schema_format  varchar(128)    not null,
	schema_version varchar(128)    not null,
	-- Parentage of this type
	root_id        char(36)        not null,
	root_tstamp    timestamp       not null,
	ref_root       varchar(255)    not null,
	ref_tree       varchar(1500)   not null,
	ref_parent     varchar(255)    not null,
	-- Properties of this type
	latitude                    float not null,
	longitude                   float not null,
	latitude_longitude_accuracy float,
	altitude                    float,
	altitude_accuracy           float,
	bearing                     float,
	speed                       float,

	CONSTRAINT geolocation_context_1__root_id_pk PRIMARY KEY(root_id),
	FOREIGN KEY(root_id) REFERENCES atomic.events(event_id)
);
-- DISTSTYLE KEY
-- Optimized join to atomic.events
-- DISTKEY (root_id)
-- SORTKEY (root_tstamp);

CREATE INDEX geolocation_context_1__root_tstamp_idx ON atomic.com_snowplowanalytics_snowplow_geolocation_context_1 (root_tstamp);