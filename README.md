# GetUp Solutions — Technical Assessment Submission

This repository has my complete submission for the **GetUp Solutions AI Automation Specialist** technical test (Part 1 & Part 2).

## Files in This Repo

- [`part1_written_answers.md`](part1_written_answers.md) — Written answers (in 2–4 simple sentences each) for all 8 questions in Technical Test Part 1.
- [`policy_qa.py`](policy_qa.py) — Python script for Technical Test Part 2 that matches staff questions to internal policies using simple keyword matching, cites supporting policy IDs, and returns a clear fallback when no policy matches.
- [`test_policy_qa.py`](test_policy_qa.py) — Unit tests verifying all three required checks.

## How to Run the Demo & Tests (Part 2)

Requires Python 3.10+ (no external packages or API keys needed).

### Run the three demonstration checks

```bash
python policy_qa.py
```

Output:

```text
Question: Who approves a roster change?
{
  "answer": "A coordinator must approve a roster change before it takes effect. (Source: P01)",
  "source_ids": [
    "P01"
  ]
}

Question: When should I record an incident?
{
  "answer": "Staff must record an incident in the incident register before the end of the shift. (Source: P02)",
  "source_ids": [
    "P02"
  ]
}

Question: How much can staff claim for travel?
{
  "answer": "Sorry, I could not find an answer to that question in the available internal policies.",
  "source_ids": []
}
```

### Run the unit tests

```bash
python -m unittest -v test_policy_qa.py
```

## One Sentence on What I Would Improve Before a Client Rollout

Before rolling this out to a client, I would replace basic keyword matching with a combined keyword and semantic search over versioned policy documents, add strict JSON-schema checks with confidence limits, and log every query so staff questions are answered accurately without making up anything outside the policy.
