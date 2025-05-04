
# Zordie Prime — Platform Integration Module (by Jyotishman)

This directory contains the multi-platform job posting integration and task queuing system built as part of the Zordie Prime AI Automation project.

## 📁 Folder Structure

```
Jyotishman/
├── common/                     # Utility and logging modules
├── langflow/                  # Placeholder for Langflow integration
├── logs/                      # Log output folder
├── platform_integrations/     # Async logic for Twitter, LinkedIn, Telegram
├── task_queue/                # Celery + Redis integration
├── .env                       # Environment configuration
├── .gitignore                 # Git ignore rules
├── requirements.txt           # Python dependencies
├── test_async_post.py         # Unified test script
├── test_async_post_linkedin.py
├── test_async_post_telegram.py
```

---

## 🔧 Key Functionalities

### 1. Platform Integrations
- Implemented async posting logic for:
  - **Twitter** via X API
  - **LinkedIn** via REST API
  - **Telegram** via Bot API
- Modular code: each platform has isolated logic in `platform_integrations/`.
- Uses `httpx.AsyncClient` for concurrent non-blocking calls.

### 2. Celery + Redis Task Queue
- `task_queue/celery_config/`: configuration for Celery app and Redis broker
- `task_queue/tasks/`: defines async tasks for job posting
- Retry + logging on failure

### 3. Logging
- Integrated logging using Python’s `logging` module.
- Each platform logs to `logs/{platform}.log` with clear timestamps.

### 4. Async Testing
- `test_async_post*.py` scripts simulate multi-platform job posts
- Fully async for concurrency testing

### 5. Langflow Placeholder
- Folder `langflow/` created for future integration
- Will allow drag-and-drop UI for non-devs to trigger jobs

### 6. Environment Handling
- `.env` used for secrets and API keys
- `.gitignore` excludes `venv/`, logs, and `.env`

---

##  Developer Notes

- Python 3.11 virtualenv used (`venv311`)
- Tested independently of Langflow, but structured to support it
- Celery worker and Redis server required to run the full pipeline

---

## ✅ Status

| Feature               | Status     |
|----------------------|------------|
| Celery + Redis       | ✅ Working |
| Twitter Integration  | ✅ Tested  |
| LinkedIn Integration | ✅ Tested  |
| Telegram Integration | ✅ Tested  |
| Logging              | ✅ Complete|
| Langflow Setup       | ⚠️ Placeholder |

---

## 🔄 Future Work
- Finalize Langflow blocks to trigger Celery tasks
- Frontend hook to let non-devs operate job posting pipeline

---

**Author:** Jyotishman  
**Task:** Multi-Platform Integration — Zordie Prime Internship  
**Repo:** https://github.com/primehr4/zordie_prime
