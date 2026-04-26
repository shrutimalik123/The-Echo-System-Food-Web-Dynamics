# 🌲 The Echo-System - Food Web Dynamics Sim

A biological strategy simulation that challenges you to maintain the delicate balance of a forest ecosystem. As the Ecosystem Manager, you must monitor the populations of Producers (Plants), Primary Consumers (Rabbits), and Apex Predators (Wolves). Your goal is to survive environmental disasters and prevent a "Trophic Collapse"—where the extinction of one species leads to the total failure of the food web.

This project focuses on teaching:
* **Trophic Levels:** Understanding the flow of energy from Producers up to Apex Predators.
* **The 10% Rule:** Simulating biological efficiency where population growth is limited by the energy available at the level below.
* **Carrying Capacity:** Managing populations so they don't outstrip their available food resources.
* **Stochastic Events:** Using `random.choice` to simulate unpredictable environmental factors like droughts and diseases.

---

## ✨ Features

* **Real-Time Population Modeling:** Tracks the growth and decline of three interconnected species based on consumption and reproduction rates.
* **Environmental Variance:** Random weather and health events force the player to adapt their management strategy every year.
* **Trophic Cascade Simulation:** Correctly models how "Top-Down" (predator) and "Bottom-Up" (producer) changes affect the entire web.
* **Active Intervention:** Allows the player to manually reintroduce species or boost plant growth to stabilize a failing system.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `ecosystem_manager.py`.
2.  **Open Terminal:** Navigate to the folder containing the file.
3.  **Run the Script:**
    ```bash
    python ecosystem_manager.py
    ```

### 3. Gameplay Instructions
1.  **Monitor the Stats:** Keep a close eye on the ratio of Plants to Rabbits to Wolves.
2.  **Survive the Events:** Adapt to Droughts (which kill plants) or Diseases (which kill rabbits).
3.  **Take Action:**
    * **Reintroduce Wolves (1):** Use this if the rabbit population is exploding and eating all the plants.
    * **Plant Seedlings (2):** Use this if a drought has left the primary consumers with nothing to eat.
    * **Do Nothing (3):** Use this if the system is currently in equilibrium.
4.  **The Goal:** Reach Year 5 without any population hitting zero.



---

## 🧠 Code Structure Highlights

### Energy Transfer Logic
This block simulates the "10% Rule." The number of new offspring for a predator is directly tied to the abundance of its prey, representing the conversion of consumed biomass into reproductive energy.

```python
# Population growth based on energy availability
pop["Rabbits"] += int(pop["Plants"] * 0.1) 
pop["Wolves"] += int(pop["Rabbits"] * 0.1)

