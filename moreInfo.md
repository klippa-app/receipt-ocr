## How to create virtual env for py (eenmalig eerste keer)
python3 -m venv venv

## Werken aan project (elke keer)
# Activeer de environment
source venv/bin/activate

# Installeer een nieuw pakket (indien nodig)
pip install pandas

# Werk aan je code...

# Werk je requirements bij als je iets nieuws hebt geïnstalleerd
pip freeze > requirements.txt

# Verlaat de environment als je klaar bent
deactivate