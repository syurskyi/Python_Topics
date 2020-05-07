from wanda.config import config


class App:
    def __init__(self, config):
        self.parameter = config['parameter']

    def run(self):
        print(f'my cool parameter: {self.parameter}')


if __name__ == '__main__':
    w = App(config)
    w.run()
