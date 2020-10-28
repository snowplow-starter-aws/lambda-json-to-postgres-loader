export PYTHONUNBUFFERED := 1
PYTHON=python3.7

.PHONY: virtualenv
virtualenv:
	$PYTHON -m pip  install virtualenv

.PHONY: .venv
.venv:
	virtualenv .venv

.PHONY: activate
activate: .venv
	. .venv/bin/activate

dev: .venv
	( \
       . .venv/bin/activate; \
       pip install -r snowplow_json_to_postgres_loader/requirements.dev.txt; \
    )


install: .venv
	( \
       . .venv/bin/activate; \
       pip install -r snowplow_json_to_postgres_loader/requirements.txt; \
    )

test: .venv
	( \
       . .venv/bin/activate; \
       AWS_PROFILE=homepage-production pytest; \
    )


.PHONY: run
run:
	AWS_PROFILE=homepage-production sam local invoke SnowplowJsonToPostgresFunction -e events/event.json

.PHONY: build.image
build.image:
	AWS_PROFILE=homepage-production sam build

.PHONY: package
package: build.image
	AWS_PROFILE=homepage-production sam package --s3-bucket petersiemen-lambda-artifacts \
 		--s3-prefix snowplow-json-to-postgres-loader --output-template-file output-template.yaml
