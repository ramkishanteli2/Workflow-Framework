import yaml
from yaml import Loader
import logging

pathList = []


def timeFunction():
    pass


def generateLogFile(data, key):
    pathList.append(key)
    logging.info(key + " Entry")

    if(data['Type'] == 'Task'):

        if(data['Function'] == 'TimeFunction'):

            func_name = data['Inputs']['FunctionInput']
            exe_time = data['Inputs']['ExecutionTime']

            timeFunction(func_name, exe_time)
            path.pop()
    logging.info(convertPath2String(path) + " Exit")
    path.pop()


# Opening yaml file
yaml_file = open('Milestone1_Example.yaml', mode='r')

# Reading data from yaml file
data = yaml.load(yaml_file, Loader=Loader)

# Generating log files using data dictionary obtained from yaml file
basicConfig(filename="logfile.txt", format="%(asctime)s.%(msecs)06d;%(message)s",
            datefmt='%Y-%m-%d %H:%M:%S', filemode='w')

for workflow in data:
    pass
    # incomplete
