#!/usr/bin/env python3
"""
Test specifically for Render deploy pattern: from app import app
"""

import os
import sys

def test_render_import():
    """Test if Render's expected import pattern works"""
    print("🔍 TESTING RENDER IMPORT PATTERN")
    print("=" * 50)
    
    # Set up environment
    os.environ.setdefault('SECRET_KEY', 'test-render-import-pattern')
    os.environ.setdefault('FLASK_ENV', 'production')
    
    try:
        # This is exactly what Render tries to do
        print("📦 Testing: from app import app")
        from app import app
        
        print("✅ Import successful!")
        print(f"✅ App type: {type(app)}")
        print(f"✅ App name: {app.name}")
        
        # Test that it's actually functional
        with app.test_client() as client:
            response = client.get('/')
            print(f"✅ Route test: / -> {response.status_code}")
            
            response = client.get('/health')
            print(f"✅ Route test: /health -> {response.status_code}")
        
        print("\n🎉 SUCCESS: Render's 'gunicorn app:app' should now work!")
        print("🚀 Deploy should be successful!")
        return True
        
    except Exception as e:
        print(f"❌ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_render_import()
    sys.exit(0 if success else 1)
