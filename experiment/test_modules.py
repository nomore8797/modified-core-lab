def test_new_idea(core, curator, labyrinth, idea):
    print(f"\n=== Запуск эксперимента: {idea} ===")
    approved, weight = curator.filter_idea(idea)
    if approved:
        core.process_idea(idea, weight)
        labyrinth.generate_routes(idea)
