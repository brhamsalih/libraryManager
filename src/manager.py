import os
from .exceptions import BackupError, RestoreError

class LibraryManager:
    """
    Comprehensive library manager:
    - Snapshot-style backup & restore for directories (OTA-safe)
    - File system tools: create/remove directories, copy files/dirs, list files, get names
    """

    def __init__(self, target_dir: str, root: str = "/", backup_root: str = ".backup"):
        self.root = root.rstrip("/")
        self.target_dir = target_dir.rstrip("/")
        self.backup_root = backup_root.rstrip("/")
        self.backup_path = self.backup_root + "/" + self.target_dir

    # ---------- Backup & Restore ----------
    def has_backup(self) -> bool:
        path = self.backup_path
        if not self.exists(path):
            return False
        try:
            return len(os.listdir(path)) > 0
        except OSError:
            return False

    def clear_backup(self):
        if self.exists(self.backup_path):
            self.remove_dir(self.backup_path)
        self.make_dir(self.backup_path)
        return True

    def backup(self):
        if not self.exists(self.target_dir):
            raise BackupError(f"Target dir not found: {self.target_dir}")
        if self.exists(self.backup_root):
            self.remove_dir(self.backup_root)
        self.make_dir(self.backup_root)
        self.copy_dir_to(self.target_dir, self.backup_root)

    def restore(self):
        if not self.has_backup():
            raise RestoreError("No valid backup to restore")
        self.remove_dir(self.target_dir)
        self.copy_dir_to(self.backup_root, self.root)

    # ---------- FS Tools ----------
    @staticmethod
    def exists(path: str) -> bool:
        try:
            os.stat(path)
            return True
        except OSError:
            return False

    @staticmethod
    def is_dir(path: str) -> bool:
        try:
            return os.stat(path)[0] & 0x4000
        except OSError:
            return False

    @staticmethod
    def make_dir(path: str) -> bool:
        """Create directory including parents"""
        parts = path.replace("\\", "/").split("/")
        cur = ""
        for p in parts:
            if not p:
                continue
            cur += "/" + p
            if not LibraryManager.exists(cur):
                os.mkdir(cur)
        return True

    @staticmethod
    def remove_dir(path: str) -> bool:
        """Remove directory recursively"""
        if LibraryManager.exists(path):
            for item in os.listdir(path):
                p = path + "/" + item
                if LibraryManager.is_dir(p):
                    LibraryManager.remove_dir(p)
                else:
                    os.remove(p)
            os.rmdir(path)
        return True

    @staticmethod
    def copy_file_to(src: str, dst: str) -> bool:
        """Copy file to a destination folder"""
        name = LibraryManager.get_filename(src)
        dst_file = dst.rstrip("/") + "/" + name
        with open(src, "rb") as fsrc:
            data = fsrc.read()
        with open(dst_file, "wb") as fdst:
            fdst.write(data)
        return True

    @staticmethod
    def _copy_file(src: str, dst: str) -> bool:
        """Copy file from src to dst path directly"""
        with open(src, "rb") as fsrc:
            data = fsrc.read()
        with open(dst, "wb") as fdst:
            fdst.write(data)
        return True

    @staticmethod
    def copy_dir_to(src: str, dst: str) -> bool:
        """Copy directory recursively"""
        name = LibraryManager.get_name(src)
        dir_dst = dst.rstrip("/") + "/" + name
        LibraryManager.make_dir(dir_dst)
        for item in os.listdir(src):
            s = src + "/" + item
            d = dir_dst + "/" + item
            if LibraryManager.is_dir(s):
                LibraryManager.copy_dir_to(s, dir_dst)
            else:
                LibraryManager._copy_file(s, d)
        return True

    @staticmethod
    def list_files(path: str):
        if LibraryManager.exists(path):
            return os.listdir(path)
        return []

    @staticmethod
    def get_filename(path: str) -> str:
        return path.replace("\\", "/").split("/")[-1]

    @staticmethod
    def get_name(path: str) -> str:
        filename = LibraryManager.get_filename(path)
        return filename.rsplit(".", 1)[0]
    
lm = LibraryManager("data/")
# lm.make_dir("data/new_folder")
# lm.copy_file_to("file.txt", "data/new_folder")
# lm.backup()
# lm.restore()

# lm.copy_file_to("main.py","data")
# lm._copy_file("main.py","data/ota.py")

