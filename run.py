"""
	Entry point for flask application
"""

from app import app

if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0')
