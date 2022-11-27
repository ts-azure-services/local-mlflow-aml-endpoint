install:
	#conda create -n mlf python=3.8 -y; conda activate mlf
	pip install scikit-learn
	pip install pandas
	pip install mlflow
	pip install matplotlib

infra:
	./setup/create-aml-resources.sh

local_run:
	# mlflow ui // can trigger the view post experiments
	# mlflow server --backend-store-uri sqlite:///mlflow.db //Model Registry needs a backend
	python ./scripts/ames_regression.py

aml_deploy:
	rm -rf ./model
	python ./scripts/find_model_files.py # copy artifacts to a common folder, overwrite conda.yaml
	./inference/deploy.sh

get_prediction:
	python ./scripts/make_test_data.py
	cat ./data/test_data.json
