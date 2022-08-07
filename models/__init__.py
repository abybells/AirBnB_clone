#!/usr/bin/env python3
"""
Init method for the models package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
