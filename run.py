from youtube import create_app


app = create_app()

# Se questo file viene eseguito direttamente, avvia il server
if __name__ == '__main__':
    app.run(debug=True, port = 7655)
