#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WSGI Entry Point for Amiraldo Portfolio Flask Application
=========================================================

This module serves as the main entry point for the Flask application.
It imports the Flask app factory and creates an application instance.
"""

import os
from app import create_app

# Create Flask application instance
app = create_app()

if __name__ == '__main__':
    """
    Run the application directly with Python
    Only used for development - in production use gunicorn
    """
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Get debug mode from environment
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    # Run the application
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
