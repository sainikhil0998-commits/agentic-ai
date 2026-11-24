# Study Planner Agent

A beginner-friendly, rule-based Python agent that builds a study plan from a time budget. It uses a fixed task list and runs locally with Python 3 and zero extra packages.

## Run it

```powershell
python agent.py
```

On Windows, you can also run `py agent.py`.

## Example

Enter 35 minutes. The agent picks SQL joins (25 minutes), skips Python basics because it needs 20 minutes, then picks Git commands (10 minutes). There are zero minutes left.

## How it decides

The agent sorts tasks by priority. It checks the remaining time before adding each task, updates that budget after each addition, and lists deferred tasks at the end. Its decisions come from Python rules. It does not use a language model or API key.

Change the sample tasks inside `main()` to make the planner your own. Each task has a name, priority (1 is highest), and duration in minutes.
