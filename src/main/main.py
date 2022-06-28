import sys
import argparse

class DeepSeaSharcq:
    def __init__(self):
        return NotImplementedError
    def predict(self, data_path: str):
        return NotImplementedError
    def train(self, data_path: str):
        return NotImplementedError
    def evaluate(self, data_path: str):
        return NotImplementedError
def main():
    my_parser = argparse.ArgumentParser(description='cli for deepseasharcq')(description='List the content of a folder')

    dss = DeepSeaSharcq()
    
if __name__ == '__main__':
    main()