import json
import tempfile
import unittest
from pathlib import Path

import web_app


class TestWebAppTaskAPI(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.tasks_file = Path(self.temp_dir.name) / "tasks.json"

        web_app.store = web_app.TaskStore(str(self.tasks_file))
        web_app.app.config["TESTING"] = True
        self.client = web_app.app.test_client()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_create_and_list_tasks(self):
        payload = {
            "staff_name": "Casey",
            "task_type": "swap",
            "detail": "Swap Friday dinner with Jordan",
            "shift_date": "2026-03-20",
            "priority": "high",
        }

        create_response = self.client.post("/api/tasks", json=payload)
        self.assertEqual(create_response.status_code, 201)
        created = create_response.get_json()["task"]
        self.assertEqual(created["staff_name"], "Casey")
        self.assertEqual(created["status"], "open")

        list_response = self.client.get("/api/tasks")
        self.assertEqual(list_response.status_code, 200)
        tasks = list_response.get_json()["tasks"]
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["detail"], payload["detail"])

    def test_validation_error_for_missing_fields(self):
        response = self.client.post("/api/tasks", json={"staff_name": ""})
        self.assertEqual(response.status_code, 400)
        self.assertIn("required", response.get_json()["error"].lower())

    def test_mark_task_done(self):
        create_response = self.client.post(
            "/api/tasks",
            json={
                "staff_name": "Taylor",
                "task_type": "unavailable",
                "detail": "Unavailable Sunday lunch",
                "priority": "normal",
            },
        )
        task_id = create_response.get_json()["task"]["id"]

        patch_response = self.client.patch(
            f"/api/tasks/{task_id}/status",
            json={"status": "done"},
        )
        self.assertEqual(patch_response.status_code, 200)
        self.assertEqual(patch_response.get_json()["task"]["status"], "done")


if __name__ == "__main__":
    unittest.main()
