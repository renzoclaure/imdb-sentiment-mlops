
.PHONY: train predict deploy monitor ingest orchestrate all

train:
	python src/train/train.py

predict:
	python src/serve/serve_model.py

deploy:
	docker build -t sentiment-api .
	docker tag sentiment-api us-central1-docker.pkg.dev/dtc-de-course-456314/sentiment-api-repo/sentiment-api
	docker push us-central1-docker.pkg.dev/dtc-de-course-456314/sentiment-api-repo/sentiment-api
	gcloud run deploy sentiment-api \	  --image us-central1-docker.pkg.dev/dtc-de-course-456314/sentiment-api-repo/sentiment-api \	  --platform=managed \	  --region=us-central1 \	  --allow-unauthenticated

monitor:
	python src/monitor/generate_report.py

upload-monitoring:
	python -c "from monitor.generate_report import upload_report_to_gcs; upload_report_to_gcs('imdb-monitoring-renzo', 'reports/classification_report.html', 'reports/classification_report.html')"

ingest:
	python src/data/upload_to_gcs.py

orchestrate:
	docker-compose up -d

all: ingest train predict deploy monitor upload-monitoring orchestrate

.PHONY: test

test:
	pytest tests/

