from app import create_app

app = create_app()

if __name__ == '__main__':
    app.config['PREFERRED_URL_SCHEME'] = 'http'
    app.run(host='0.0.0.0', debug=True)
