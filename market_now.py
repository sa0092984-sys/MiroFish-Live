import os
import sys
import time
from dotenv import load_dotenv

# Path setup
sys.path.append(os.path.join(os.getcwd(), 'backend'))
load_dotenv()

from app.services.simulation_runner import SimulationRunner

def get_market_analysis():
    print("🚀 MIROFISH TERMINAL ENGINE: ONLINE")
    
    sim_id = f"market_test_{int(time.time())}"
    scenario = "Nifty 50 at 23,100. Budget 2026 favors Defence and Green Energy. 5-year horizon."
    
    try:
        runner = SimulationRunner()
        
        # 🛠️ STEP 1: PREPARE (This fixes the 'Configuration does not exist' error)
        print(f"📦 Preparing simulation environment: {sim_id}...")
        
        # We simulate the data the /prepare API usually sends
        config_data = {
            "scenario": scenario,
            "target_goal": "Identify top 3 sectors for 5-year investment.",
            "platforms": ["twitter"],
            "agent_count": 3
        }
        
        # This creates the necessary files in backend/run_state/
        runner.prepare_simulation(sim_id, config_data)
        print("✅ Environment Prepared.")

        # 🛠️ STEP 2: START
        print("🧠 AI Agents are waking up...")
        runner.start_simulation(sim_id, config_data)
        
        print("⏳ Waiting for Agent thoughts (approx 45s)...")
        time.sleep(45)
        
        # 🛠️ STEP 3: CHECK RESULTS
        actions = runner.get_all_actions(sim_id)
        
        if actions:
            print("\n" + "="*40)
            print("📈 INDIAN MARKET ANALYSIS")
            print("="*40)
            for action in actions[:5]:
                print(f"[{action.agent_name}]: {action.result}")
            print("="*40)
        else:
            print("\n🕒 Agents are still analyzing.")
            print(f"💡 Check this folder in 1 minute: backend/run_state/{sim_id}/")

    except Exception as e:
        print(f"❌ Execution Error: {e}")

if __name__ == "__main__":
    get_market_analysis()