class Curator:
    def __init__(self):
        self.rules = ["паук", "бабочек", "эксперимент"]

    def filter_idea(self, idea):
        for rule in self.rules:
            if rule.lower() not in idea.lower():
                print(f"Идея заблокирована правилом: {rule}")
                return False, 0.0
        print("Идея одобрена кураторами")
        return True, 1.0  # вес по умолчанию
