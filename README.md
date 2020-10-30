# lambda-json-to-postgres-loader


Reads files with Snowplow tracking events encoded as one JSON object per line
and writes them into the appropriate tables in postgres. 

Configured by ENV Variables:

* DATABASE
* HOST 
* PORT 
* USERNAME 
* PASSWORD

