#!/usr/bin/env python3
"""
Alternative entry point for Render deployment
This file exists to avoid conflicts with the app/ folder
"""

import os
import sys

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import the application factory
from app import create_app

# Create the application instance
app = create_app()

# For development server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
