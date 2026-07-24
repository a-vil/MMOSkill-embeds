import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

INDEX_FILE = Path(__file__).resolve().parent / "halberd_index.json"


def _ensure_dir() -> None:
    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)


def load_index() -> dict:
    _ensure_dir()
    if not INDEX_FILE.exists():
        return {"guilds": {}}
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        logger.error("halberd_index.json corrupted, resetting to empty index")
        return {"guilds": {}}
    except OSError:
        logger.error("Failed to read halberd_index.json", exc_info=True)
        return {"guilds": {}}


def save_index(data: dict) -> None:
    _ensure_dir()
    try:
        with open(INDEX_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except OSError:
        logger.error("Failed to write halberd_index.json", exc_info=True)


def save_skill(guild_id: int, skill_key: str, name: str, tier: str, channel_id: int, message_id: int) -> None:
    data = load_index()
    gid = str(guild_id)
    if gid not in data["guilds"]:
        data["guilds"][gid] = {"index": None, "skills": {}}
    data["guilds"][gid]["skills"][skill_key] = {
        "name": name,
        "tier": tier,
        "channel_id": channel_id,
        "message_id": message_id,
    }
    save_index(data)


def save_index_message(guild_id: int, channel_id: int, message_id: int) -> None:
    data = load_index()
    gid = str(guild_id)
    if gid not in data["guilds"]:
        data["guilds"][gid] = {"index": None, "skills": {}}
    data["guilds"][gid]["index"] = {
        "channel_id": channel_id,
        "message_id": message_id,
    }
    save_index(data)


def get_guild_data(guild_id: int) -> dict:
    data = load_index()
    return data.get("guilds", {}).get(str(guild_id), {"index": None, "skills": {}})
