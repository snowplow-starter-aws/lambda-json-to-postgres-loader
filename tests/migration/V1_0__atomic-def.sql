-- Copyright (c) 2013-2018 Snowplow Analytics Ltd. All rights reserved.
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
-- Version:     0.11.0
-- URL:         -
--
-- Authors:     Yali Sassoon, Alex Dean, Peter van Wesep, Fred Blundun, Konstantinos Servis, Mike Robins
-- Copyright:   Copyright (c) 2013-2018 Snowplow Analytics Ltd
-- License:     Apache License Version 2.0

-- Create the schema
CREATE SCHEMA atomic;

-- Create events table
CREATE TABLE atomic.events (
	-- App
	app_id varchar(255),
	platform varchar(255),
	-- Date/time
	etl_tstamp timestamp,
	collector_tstamp timestamp not null,
	dvce_created_tstamp timestamp,
	-- Event
	event varchar(128),
	event_id char(36) not null unique,
	txn_id int,
	-- Namespacing and versioning
	name_tracker varchar(128),
	v_tracker varchar(100),
	v_collector varchar(100)  not null,
	v_etl varchar(100)  not null,
	-- User and visit
	user_id varchar(255),
	user_ipaddress varchar(128),
	user_fingerprint varchar(128),
	domain_userid varchar(128),
	domain_sessionidx int,
	network_userid varchar(128),
	-- Location
	geo_country char(2),
	geo_region char(3),
	geo_city varchar(75),
	geo_zipcode varchar(15),
	geo_latitude double precision,
	geo_longitude double precision,
	geo_region_name varchar(100),
	-- IP lookups
	ip_isp varchar(100),
	ip_organization varchar(128),
	ip_domain varchar(128),
	ip_netspeed varchar(100),
	-- Page
	page_url varchar(4096),
	page_title varchar(2000),
	page_referrer varchar(4096),
	-- Page URL components
	page_urlscheme varchar(16),
	page_urlhost varchar(255),
	page_urlport int,
	page_urlpath varchar(3000),
	page_urlquery varchar(6000),
	page_urlfragment varchar(3000),
	-- Referrer URL components
	refr_urlscheme varchar(16),
	refr_urlhost varchar(255),
	refr_urlport int,
	refr_urlpath varchar(6000),
	refr_urlquery varchar(6000),
	refr_urlfragment varchar(3000),
	-- Referrer details
	refr_medium varchar(25),
	refr_source varchar(50),
	refr_term varchar(255),
	-- Marketing
	mkt_medium varchar(255),
	mkt_source varchar(255),
	mkt_term varchar(255),
	mkt_content varchar(500),
	mkt_campaign varchar(255),
	-- Custom structured event
	se_category varchar(1000),
	se_action varchar(1000),
	se_label varchar(4096),
	se_property varchar(1000),
	se_value double precision,
	-- Ecommerce
	tr_orderid varchar(255),
	tr_affiliation varchar(255),
	tr_total dec(18,2),
	tr_tax dec(18,2),
	tr_shipping dec(18,2),
	tr_city varchar(255),
	tr_state varchar(255),
	tr_country varchar(255),
	ti_orderid varchar(255),
	ti_sku varchar(255),
	ti_name varchar(255),
	ti_category varchar(255),
	ti_price dec(18,2),
	ti_quantity int,
	-- Page ping
	pp_xoffset_min int,
	pp_xoffset_max int,
	pp_yoffset_min int,
	pp_yoffset_max int,
	-- User Agent
	useragent varchar(1000),
	-- Browser
	br_name varchar(50),
	br_family varchar(50),
	br_version varchar(50),
	br_type varchar(50),
	br_renderengine varchar(50),
	br_lang varchar(255),
	br_features_pdf boolean,
	br_features_flash boolean,
	br_features_java boolean,
	br_features_director boolean,
	br_features_quicktime boolean,
	br_features_realplayer boolean,
	br_features_windowsmedia boolean,
	br_features_gears boolean,
	br_features_silverlight boolean,
	br_cookies boolean,
	br_colordepth varchar(12),
	br_viewwidth int,
	br_viewheight int,
	-- Operating System
	os_name varchar(50),
	os_family varchar(50),
	os_manufacturer varchar(50),
	os_timezone varchar(255),
	-- Device/Hardware
	dvce_type varchar(50),
	dvce_ismobile boolean,
	dvce_screenwidth int,
	dvce_screenheight int,
	-- Document
	doc_charset varchar(128),
	doc_width int,
	doc_height int,

	-- Currency
	tr_currency char(3),
	tr_total_base dec(18, 2),
	tr_tax_base dec(18, 2),
	tr_shipping_base dec(18, 2),
	ti_currency char(3),
	ti_price_base dec(18, 2),
	base_currency char(3),

	-- Geolocation
	geo_timezone varchar(64),

	-- Click ID
	mkt_clickid varchar(128),
	mkt_network varchar(64),

	-- ETL tags
	etl_tags varchar(500),

	-- Time event was sent
	dvce_sent_tstamp timestamp,

	-- Referer
	refr_domain_userid varchar(128),
	refr_dvce_tstamp timestamp,

	-- Session ID
	domain_sessionid char(128),

	-- Derived timestamp
	derived_tstamp timestamp,

	-- Event schema
	event_vendor varchar(1000),
	event_name varchar(1000),
	event_format varchar(128),
	event_version varchar(128),

	-- Event fingerprint
	event_fingerprint varchar(128),

	-- True timestamp
	true_tstamp timestamp,

	CONSTRAINT event_id_0110_pk PRIMARY KEY(event_id)
);

CREATE INDEX collector_tstamp_idx ON atomic.events (collector_tstamp);
-- DISTSTYLE KEY
-- DISTKEY (event_id)
-- SORTKEY (collector_tstamp);


