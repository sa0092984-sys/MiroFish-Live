import os
from app import create_app

# Use the official factory to build the app with all routes pre-configured
app = create_app()

if __name__ == "__main__":
    # Ensure all required upload directories exist before the engine starts
    os.makedirs('backend/uploads/reports', exist_ok=True)
    os.makedirs('backend/uploads/graphs', exist_ok=True)
    os.makedirs('backend/uploads/simulations', exist_ok=True)
    os.makedirs('backend/static', exist_ok=True)
    
    print("🚀 MiroFish Engine: All systems go. Starting on Port 5001...")
    app.run(host="0.0.0.0", port=5001, debug=True)