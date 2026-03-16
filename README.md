# 📋 Shift Pocket Logger

A mobile-friendly Flask app for capturing rostering requests in seconds while you're mid-service.

## Why this app?

When someone asks you to:
- swap a shift,
- mark them unavailable for a day, or
- handle another quick roster change,

you can log it immediately on your phone so nothing gets forgotten.

## Features

- **Fast phone-first form** for one-handed use.
- **Request types**: Shift Swap, Unavailable Day, or Other.
- **Priority labels** (low, normal, high).
- **Persistent storage** in a local JSON file (`data/rostering_tasks.json`).
- **Open items list** with one-tap **Mark Done** action.
- **PWA manifest** so you can add it to your phone home screen.

## Run locally

```bash
pip install -r requirements.txt
python web_app.py
```

Then open `http://localhost:5000`.

## API endpoints

- `GET /api/tasks` — list tasks
- `POST /api/tasks` — create a task
- `PATCH /api/tasks/<task_id>/status` — set status (`open` or `done`)

## Testing

```bash
python -m unittest test_web_app.py
```
