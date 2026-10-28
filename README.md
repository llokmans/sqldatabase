# sqldatabase

A student grades database in SQLite, built to practise SQL aggregation from Python.

## Files

| File | Job |
| --- | --- |
| `database.py` | Creates the `grades` table (student, subject, grade) |
| `seed.py` | Bulk-inserts sample grades with `executemany` |
| `add.py` | Inserts a single record |
| `analyze.py` | Runs the reports below |

## Reports

- **Leaderboard**: each student's average grade, highest first (`GROUP BY`, `ORDER BY ... DESC`)
- **Pass/fail**: only students averaging 70 or above (`HAVING`)
- **Subject averages**: hardest subject first (`GROUP BY subject`, `ORDER BY ... ASC`)

## Run it

Standard library only.

```
python database.py
python seed.py
python analyze.py
```
