"""Mobile-friendly rostering capture app."""
from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


class TaskStore:
    """Simple JSON-backed store for rostering tasks."""

    def __init__(self, file_path: str | None = None) -> None:
        configured_path = file_path or os.getenv("TASKS_FILE", "data/rostering_tasks.json")
        self.file_path = Path(configured_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self._write([])

    def _read(self) -> list[dict[str, Any]]:
        with self.file_path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def _write(self, tasks: list[dict[str, Any]]) -> None:
        with self.file_path.open("w", encoding="utf-8") as handle:
            json.dump(tasks, handle, indent=2)

    def list_tasks(self) -> list[dict[str, Any]]:
        tasks = self._read()
        return sorted(tasks, key=lambda task: task["created_at"], reverse=True)

    def add_task(self, payload: dict[str, str]) -> dict[str, Any]:
        staff_name = (payload.get("staff_name") or "").strip()
        task_type = (payload.get("task_type") or "").strip()
        detail = (payload.get("detail") or "").strip()
        shift_date = (payload.get("shift_date") or "").strip()
        priority = (payload.get("priority") or "normal").strip().lower()

        if not staff_name or not task_type or not detail:
            raise ValueError("Staff name, task type, and detail are required.")

        if task_type not in {"swap", "unavailable", "other"}:
            raise ValueError("Task type must be one of: swap, unavailable, other.")

        if priority not in {"low", "normal", "high"}:
            raise ValueError("Priority must be low, normal, or high.")

        now = datetime.utcnow().isoformat(timespec="seconds") + "Z"
        task = {
            "id": int(datetime.utcnow().timestamp() * 1000000),
            "staff_name": staff_name,
            "task_type": task_type,
            "detail": detail,
            "shift_date": shift_date or None,
            "priority": priority,
            "status": "open",
            "created_at": now,
            "updated_at": now,
        }

        tasks = self._read()
        tasks.append(task)
        self._write(tasks)
        return task

    def update_status(self, task_id: int, status: str) -> dict[str, Any]:
        if status not in {"open", "done"}:
            raise ValueError("Status must be open or done.")

        tasks = self._read()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = status
                task["updated_at"] = datetime.utcnow().isoformat(timespec="seconds") + "Z"
                self._write(tasks)
                return task

        raise KeyError("Task not found.")


store = TaskStore()


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"success": True, "tasks": store.list_tasks()})


@app.route("/api/tasks", methods=["POST"])
def create_task():
    try:
        payload = request.get_json() or {}
        task = store.add_task(payload)
        return jsonify({"success": True, "task": task}), 201
    except ValueError as error:
        return jsonify({"success": False, "error": str(error)}), 400


@app.route("/api/tasks/<int:task_id>/status", methods=["PATCH"])
def update_task_status(task_id: int):
    try:
        payload = request.get_json() or {}
        task = store.update_status(task_id=task_id, status=payload.get("status", ""))
        return jsonify({"success": True, "task": task})
    except ValueError as error:
        return jsonify({"success": False, "error": str(error)}), 400
    except KeyError as error:
        return jsonify({"success": False, "error": str(error)}), 404


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("📋 Shift Pocket Logger")
    print("=" * 60)
    print("\nStarting server at http://localhost:5000")
    print("Open this URL on your phone and add it to your home screen.")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60 + "\n")
    app.run(debug=True, host="0.0.0.0", port=5000)
