import argparse
import logging

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
    # handle arguments from command line
    my_parser = argparse.ArgumentParser(description='cli for deepseasharcq')
    my_parser.add_argument('ai_action', type=str, help = 'experiment or train or evaluate')
    my_parser.add_argument('path', help='path to data to use', type=str)
    args = my_parser.parse_args()

    # run ai program
    dss = DeepSeaSharcq()
    if args.ai_action == 'train':
        dss.train(args.path)
    elif args.ai_action == 'predict':
        dss.predict(args.path)
    else:
        logging.error('invalid ai_action input: choose "train" or "predict" and provide "path" for data to use')

if __name__ == '__main__':
    main()