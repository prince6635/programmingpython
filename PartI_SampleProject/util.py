import os

def generatePathUnderDataFolder(fileName):
    rel_path = "data/" + fileName
    # abs_file_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), rel_path)
    abs_file_path = os.path.join(os.path.dirname(__file__), rel_path)
    # print(abs_file_path)
    return abs_file_path
