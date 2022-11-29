# local-mlflow-aml-endpoint
This repo demonstrates a workflow to develop a local ML model using [mlflow](https://mlflow.org) and then
leverage Azure ML to setup a real-time inference endpoint. To use this workflow, ensure that you have the
latest Azure ML CLI v2 installed (refer this [link](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?tabs=public)).

## Steps
1. Create a local virtual environment and install needed libraries using the `make install` command.
2. Create the Azure ML environment using the `make infra` command:
  1. Ensure you have a `sub.env` file with your subscription listed as a single line command as `SUB_ID=<your
     subscription>`.
3. Then, start a local mlflow backend server, and in a separate terminal, trigger a local run, using `make local_run`.
4. Once you have the local model artifacts, run `aml_deploy`. This will do a few things:
  1. Consolidate all the model artifacts in a `model` directory.
  2. Overwrite the `conda.yaml` file with a more extensive definition.
  3. Trigger a number of Azure CLI commands to register the model in AML and trigger a managed real-time
     deployment. (This can also be manually done through the Portal as detailed [here](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models?tabs=fromlocal%2Cmir%2Ccli).
5. Once the endpoint is up, the last series of commands - `make get_prediction` - can help generate some test data
   from the original dataset which can be manually tested through the Portal 'Test' feature for the
   managed online endpoint.
