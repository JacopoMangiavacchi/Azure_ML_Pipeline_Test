import pickle, json
from azureml.core.model import Model

def init():
    global pi_estimate
    model_path = Model.get_model_path(model_name = "pi_estimate")
    with open(model_path, "rb") as f:
        pi_estimate = float(pickle.load(f))

def run(raw_data):
    try:
        radius = json.loads(raw_data)["radius"]
        result = pi_estimate * radius**2
        return json.dumps({"area": result})
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
