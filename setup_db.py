
import sqlite3
import os
from pathlib import Path

def setup_database():
    """Crea e popola il database"""
    # Percorso del database
    instance_path = Path(__file__).parent / 'instance'
    instance_path.mkdir(exist_ok=True)
    
    db_path = instance_path / 'video_canali.sqlite'
    
    # Se il database esiste già, lo eliminiamo per ricominciare da zero
    if db_path.exists():
        db_path.unlink()
        print("Database esistente rimosso, ne creo uno nuovo...")
    
    # Connessione al database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Leggiamo lo schema dal file schema.sql
        schema_path = Path(__file__).parent / 'youtube' / 'schema.sql'
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = f.read()
        
        # Eseguiamo lo schema
        cursor.executescript(schema)
        conn.commit()
        print("Database creato e popolato con successo!")
        print(f"Database salvato in: {db_path}")
        
        # Verifichiamo i dati inseriti
        cursor.execute("SELECT COUNT(*) FROM canali")
        canali_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM video")
        video_count = cursor.fetchone()[0]
        
        print(f"\nStatistiche:")
        print(f"   Canali: {canali_count}")
        print(f"   Video: {video_count}")
        
    except Exception as e:
        print(f"Errore durante la creazione del database: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
    
    return True

if __name__ == '__main__':
    print("=" * 50)
    print("Setup Database - Video e Canali")
    print("=" * 50)
    print()
    
    success = setup_database()
    
    if success:
        print("\nPronte! Puoi ora avviare l'app con:")
        print("   python run.py")
    else:
        print("\nSetup fallito. Controlla gli errori sopra.")
