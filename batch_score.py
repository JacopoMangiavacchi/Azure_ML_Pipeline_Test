
import argparse
import os
from azureml.core import Run
from azureml.core.model import Model
import pickle, json

def main():
    run = Run.get_context()
    run.log("start batch score", 1)

    print("In batch_score.py")

    parser = argparse.ArgumentParser("scoring")

    parser.add_argument('--model_name', dest="model_name", required=True)
    parser.add_argument("--input", type=str, help="input data", required=True)
    parser.add_argument("--output", type=str, help="output data", required=True)
    parser.add_argument("--param1", type=str, help="param 1")


    args = parser.parse_args()

    print("Model: %s" % args.model_name)
    print("Input: %s" % args.input)
    print("Output: %s" % args.output)
    print("Param1: %s" % args.param1)

    run.log("start batch score", 2)

    # Get the Model
    global pi_estimate
    model_path = Model.get_model_path(model_name = args.model_name)
    with open(model_path, "rb") as f:
        pi_estimate = float(pickle.load(f))

        
    # Get the input Data
    with open(args.input) as json_file:  
        data = json.load(json_file)
    radius = data["radius"]
    
    
    # Use the Model
    area = pi_estimate * radius**2
    run.log("Radius: %s" % radius, 1)
    run.log("Area: %s" % area, 1)
    print("Radius: %s" % radius)
    print("Area: %s" % area)

    
    # create output directory if it does not exist
    os.makedirs(args.output, exist_ok=True)

    
    # Save output on blob storage
    out_filename = os.path.join(args.output, "result.txt")
    with open(out_filename, "w") as result_file:
        result_file.write("Area: %s" % area)
        result_file.flush()
        
    run.complete()


if __name__ == "__main__":
    main()
