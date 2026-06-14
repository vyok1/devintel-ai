# DevIntel AI - Database Design V1

## Database

PostgreSQL

---

## users

Purpose:
Store user accounts.

Columns:

id (Primary Key)
username
email
password_hash
created_at

---

## repositories

Purpose:
Store GitHub repositories submitted by users.

Columns:

id (Primary Key)
user_id (Foreign Key -> users.id)
github_url
repository_name
repository_type
created_at

---

## analysis_reports

Purpose:
Store AI-generated repository analysis.

Columns:

id (Primary Key)
repository_id (Foreign Key -> repositories.id)
summary
technologies
architecture_summary
complexity_score
created_at

---

## agent_runs

Purpose:
Track execution of AI agents.

Columns:

id (Primary Key)
repository_id (Foreign Key -> repositories.id)
agent_name
status
execution_time
created_at

---

## Relationships

users
↓
repositories
↓
analysis_reports

repositories
↓
agent_runs
