class LibraryManagerError(Exception):
    """Base exception for library_manager"""

class BackupError(LibraryManagerError):
    pass

class RestoreError(LibraryManagerError):
    pass

class OtaError(LibraryManagerError):
    pass
