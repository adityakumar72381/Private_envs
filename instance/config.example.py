# ─────────────────────────────────────────────────────────────
#  Private Configuration for 0x0 / The Null Pointer
#  Modified for Private Instance by Aditya
#  Changes:
#    • API key protection will handle access (so IP/NSFW not needed)
#    • File expiry removed — uploads are permanent until manual deletion
#    • No auto-delete, virus scan, or IP ban logic
#    • Kept local SQLite DB and upload directory setup
# ─────────────────────────────────────────────────────────────

from pathlib import Path

# Use local SQLite DB stored in instance/db.sqlite
SQLALCHEMY_DATABASE_URI = f"sqlite:///{ Path(__file__).parent.absolute() }/db.sqlite"

# Maximum upload size — 256 MB (you can increase)
MAX_CONTENT_LENGTH = 256 * 1024 * 1024  # 256 MB

# No URL shortening limits needed; we keep default safe length
MAX_URL_LENGTH = 4096

# ✅ Disable file expiration — files will stay forever
# Just set both to 0 to disable expiration logic entirely
FHOST_MIN_EXPIRATION = 0
FHOST_MAX_EXPIRATION = 0

# Your domain (optional, for absolute URLs)
# SERVER_NAME = "yourdomain.com"

# File serving setup — keep simple local serving
USE_X_SENDFILE = False
FHOST_USE_X_ACCEL_REDIRECT = False

# Where uploaded files will be stored
FHOST_STORAGE_PATH = "up"

# Limit on max extension length (good default)
FHOST_MAX_EXT_LENGTH = 9

# Secret bytes (used for private URLs)
FHOST_SECRET_BYTES = 16

# MIME → extension mapping (keep common types)
FHOST_EXT_OVERRIDE = {
    "audio/flac": ".flac",
    "image/gif": ".gif",
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/svg+xml": ".svg",
    "video/webm": ".webm",
    "video/x-matroska": ".mkv",
    "application/octet-stream": ".bin",
    "text/plain": ".txt",
    "text/x-diff": ".diff",
}

# ✅ Disable MIME blacklist — private instance doesn’t need upload bans
FHOST_MIME_BLACKLIST = []

# ✅ Disable IP blacklist — since uploads are API key protected
FHOST_UPLOAD_BLACKLIST = None

# ✅ Disable NSFW detection (not needed for private server)
NSFW_DETECT = False
NSFW_THRESHOLD = 0.0

# ✅ Disable virus scanning and quarantine logic
VSCAN_QUARANTINE_PATH = None
VSCAN_INTERVAL = None
VSCAN_IGNORE = []

# ✅ Keep default URL alphabet for short links
URL_ALPHABET = "DEQhd2uFteibPwq0SWBInTpA_jcZL5GKz3YCR14Ulk87Jors9vNHgfaOmMXy6Vx-"

# ✅ Add flag for API key enforcement
REQUIRE_API_KEY = True
API_KEY = "1234"

# ✅ Disable auto delete for good measure
AUTO_DELETE = False

# ✅ Folder to hold quarantined or removed files (manual only)
MANUAL_DELETE_FOLDER = "trash"
