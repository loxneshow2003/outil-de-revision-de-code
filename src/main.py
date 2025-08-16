# Outil de Révision de Code

# Importation des bibliothèques nécessaires
import json
import sys

class CodeReviewTool:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def generate_comments(self, code):
        comments = []
        for rule in self.rules:
            if not rule['check'](code):
                comments.append(rule['comment'])
        return comments

    def save_rules(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.rules, f)

    def load_rules(self, filename):
        with open(filename, 'r') as f:
            self.rules = json.load(f)

if __name__ == '__main__':
    tool = CodeReviewTool()
    # Exemple de règles
    tool.add_rule({
        'check': lambda code: 'bad_style' not in code,
        'comment': 'Le code ne respecte pas le style prévu.'
    })
    sample_code = 'def example_function(): pass  # bad_style'
    comments = tool.generate_comments(sample_code)
    for comment in comments:
        print(comment)