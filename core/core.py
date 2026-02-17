python
class Core:
    def __init__(self):
        self.active_routes = []

    def process_idea(self, idea, weight=1.0):
        print(f"Ядро обрабатывает идею: {idea} с весом {weight}")
        return True
