import random

def ecosystem_manager_game():
    # 1. Biological Setup (Initial Populations)
    # Producers (Plants), Consumers (Rabbits), Predators (Wolves)
    pop = {
        "Plants": 500,
        "Rabbits": 50,
        "Wolves": 5
    }
    
    years = 0
    print("--- 🌲 THE ECHO-SYSTEM: FOOD WEB DYNAMICS 🌲 ---")
    print("Goal: Maintain a stable ecosystem for 5 years.")
    print("Warning: If any population hits zero, the ecosystem collapses!")

    # 2. Game Loop
    while years < 5:
        years += 1
        print(f"\n--- YEAR {years} ---")
        print(f"Stats: Plants: {pop['Plants']} | Rabbits: {pop['Rabbits']} | Wolves: {pop['Wolves']}")
        
        # 3. Environmental Events
        event = random.choice(["Drought", "Perfect Rain", "Disease", "Normal"])
        if event == "Drought":
            pop["Plants"] -= 100
            print("☀️ DROUGHT! Plant growth has plummeted.")
        elif event == "Perfect Rain":
            pop["Plants"] += 150
            print("🌧️ PERFECT RAIN! The producers are thriving.")
        elif event == "Disease":
            pop["Rabbits"] = int(pop["Rabbits"] * 0.7)
            print("🦠 DISEASE! A rabbit virus has thinned the herd.")

        # 4. Trophic Interaction Logic
        # Each rabbit eats 5 plants. Each wolf eats 4 rabbits.
        eaten_plants = pop["Rabbits"] * 5
        eaten_rabbits = pop["Wolves"] * 4
        
        pop["Plants"] -= eaten_plants
        pop["Rabbits"] -= eaten_rabbits
        
        # Natural reproduction
        pop["Rabbits"] += int(pop["Plants"] * 0.1) # Rabbits grow based on food
        pop["Wolves"] += int(pop["Rabbits"] * 0.1) # Wolves grow based on food
        
        # 5. Stability Check
        if pop["Plants"] <= 0 or pop["Rabbits"] <= 0 or pop["Wolves"] <= 0:
            print("\n💀 ECOSYSTEM COLLAPSED! A trophic level was wiped out.")
            return

        # 6. Management Action
        print("\nMANAGEMENT ACTION:")
        print("1) Reintroduce Wolves (Add 2 Wolves)")
        print("2) Plant Seedlings (Add 100 Plants)")
        print("3) Do Nothing (Wait for next season)")
        
        choice = input("Choice (1-3): ")
        if choice == "1":
            pop["Wolves"] += 2
        elif choice == "2":
            pop["Plants"] += 100

    print(f"\n🏆 SUCCESS! You maintained the balance for {years} years.")
    print(f"Final Diversity: Plants({pop['Plants']}), Rabbits({pop['Rabbits']}), Wolves({pop['Wolves']})")

ecosystem_manager_game()
