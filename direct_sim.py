import os
import sys
from dotenv import load_dotenv

# This ensures Python can find the backend folders
sys.path.append(os.path.join(os.getcwd(), 'backend'))

# UPDATED IMPORTS: These names must match your file exactly
from app.services.graph_builder import GraphService # Changed from GraphBuilder
from app.services.simulation_runner import SimulationService # Changed from SimulationRunner

load_dotenv()

def run_market_simulation():
    print("🚀 Starting Direct MiroFish Simulation...")
    
    market_scenario = """
    Nifty 50 at 23,100. Union Budget 2026 significantly increases spending 
    on Defence, Green Energy, and Railways. 
    """
    
    print("🧠 AI is analyzing the Indian Share Market...")
    
    # Initialize the services
    builder = GraphService()
    runner = SimulationService()
    
    # Run the logic
    try:
        ontology = builder.generate_ontology(market_scenario)
        print("✅ Market Entities Identified.")
        
        results = runner.run_simulation(market_scenario, "Predict best 3 sectors for 5 years.")
        print("\n--- 📈 SIMULATION RESULTS ---")
        print(results)
    except Exception as e:
        print(f"❌ Error during simulation: {e}")

if __name__ == "__main__":
    run_market_simulation()