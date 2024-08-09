import argparse


class Editor:
    def __init__(self, args) -> None:
        self.config_file = args.config
        self.sample_file = args.sample
        self.pairs = {}
        self.sample_lines = []
        self.edited_pairs = []
        self.sorted_lines = []
        self.text = ''

    def read_config(self):
        with open(self.config_file, 'r') as file:
            lines = file.readlines()
        for line in lines:
            self.pairs[line[:line.find('=')]] = line[line.find('=')+1:].strip()

    def read_sample(self):
        with open(self.sample_file, 'r') as file:
            self.sample_lines = [list(line.strip()) for line in file.readlines()]

    def edit_sample(self):
        for line in range(len(self.sample_lines)):
            count = 0
            for symbol in range(len(self.sample_lines[line])):
                if self.sample_lines[line][symbol] in list(self.pairs.keys()):
                    self.sample_lines[line][symbol] = self.pairs[self.sample_lines[line][symbol]]
                    count += 1
            self.edited_pairs.append((''.join(self.sample_lines[line]), count))

    def sort(self):
        self.edited_pairs.sort(reverse=True, key=lambda x: x[1])
        for a, b in self.edited_pairs:
            self.sorted_lines.append(a)

    def print_result_text(self):
        self.text = '\n'.join(self.sorted_lines)
        print(self.text)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', dest='config', help='Configure file')
    parser.add_argument('-s', '--sample', dest='sample', help='Sample file')
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    editor = Editor(args)
    editor.read_config()
    editor.read_sample()
    editor.edit_sample()
    editor.sort()
    editor.print_result_text()

