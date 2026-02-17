from core.core import Core
from curators.filters import Curator
from labyrinth.routes import Labyrinth
from experiment.test_modules import test_new_idea

# Инициализация модулей
core = Core()
curator = Curator()
labyrinth = Labyrinth()

# Идея для эксперимента
idea = "Паук кормит бабочек"

# Запуск эксперимента
test_new_idea(core, curator, labyrinth, idea)