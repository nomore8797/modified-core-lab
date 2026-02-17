class Labyrinth:
    def __init__(self):
        self.routes = []

    def generate_routes(self, idea, max_routes=3):
        alternatives = [
            idea + " — сияние нити",
            idea + " — вихрь мыслей",
            idea + " — кубик энергии"
        ][:max_routes]  # ограничение количества маршрутов
        self.routes.extend(alternatives)
        print(f"Сгенерированы маршруты лабиринта: {alternatives}")
        return alternatives
