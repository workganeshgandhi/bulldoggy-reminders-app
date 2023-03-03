"""
This module builds shared parts for other modules.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import tinydb


# --------------------------------------------------------------------------------
# Connect the Database
# --------------------------------------------------------------------------------

db = tinydb.TinyDB('reminder_db.json')