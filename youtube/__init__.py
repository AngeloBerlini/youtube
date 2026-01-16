import os
from flask import Flask

def create_app():
    # 1. Creiamo l'istanza di Flask
    app = Flask(__name__, instance_relative_config=True)

    # 2. Configurazione di base
    # Qui impostiamo le variabili fondamentali.
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'video_canali.sqlite'),
    )

    # Assicuriamo che la cartella 'instance' esista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 3. Registriamo le funzioni di chiusura del database
    from . import db
    app.teardown_appcontext(db.close_db)
    
    # 4. Creiamo un comando CLI per inizializzare il database
    @app.cli.command('init-db')
    def init_db_command():
        """Inizializza il database."""
        db.init_db()
        print('Database inizializzato.')

    # --- REGISTRAZIONE BLUEPRINTS ---
    from . import main
    app.register_blueprint(main.bp)
    # --------------------------------

    return app