
import argparse
import os

from azureml.core import Run
run = Run.get_context()
run.log("start batch score", 1)

print("In batch_score.py")
print("As a data scientist, this is where I use my scoring code.")

parser = argparse.ArgumentParser("scoring")

parser.add_argument("--input", type=str, help="input data")
parser.add_argument("--output", type=str, help="output data")
parser.add_argument("--param1", type=str, help="param 1")


args = parser.parse_args()

print("Input: %s" % args.input)
print("Output: %s" % args.output)
print("Param1: %s" % args.param1)

run.log("Input: %s" % args.input, 1)
run.log("Output: %s" % args.output, 1)
run.log("Param1: %s" % args.param1, 1)

run.log("start batch score", 2)
run.log("end batch score", 1)

run.complete()
