from app import app

if __name__ == '__main__':
    # Use '0.0.0.0' to allow the app to be accessible externally
    app.run(host='0.0.0.0', port=5000)
