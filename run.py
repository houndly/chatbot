"""
	Entry point for flask application
"""

from app import app

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='0.0.0.0')
