---
name: lead-tracker
description: Organise LinkedIn lead-generation work in a simple spreadsheet tracker/CRM — set up the tracker from the bundled template, add or update leads, move people through 11 evidence-based stages (To Research → Researched → Ready for Engagement → Connection Requested → Connected → Conversation Started → Qualified Opportunity → Meeting Proposed → Meeting Booked → Nurture / Not a Fit), log interactions, list today's follow-ups and run weekly hygiene. Use whenever someone asks to set up a lead tracker or CRM sheet, add a lead, update a status, log a message or comment, see who to follow up with, clean up their pipeline, or export leads.
---

# Lead Tracker & CRM Assistant

**Purpose:** One reliable record of who the user is engaging, why, and what happens next. Stage 10 (Track), and the memory that connects all other skills.

Read `references/ground-rules.md` first. A template is bundled at `assets/lead-tracker-template.xlsx` (rebuild it with `scripts/build_tracker_template.py` from the repo root).

## When to use it

- Setting up the system (copy the template into the workspace as `lead-tracker.xlsx`).
- After any research, qualification, outreach or engagement step.
- Every morning: "who do I follow up with today?"
- Weekly: clean-up before `weekly-review`.

## Tracker structure

**Sheet "Leads"**: one row per person.

| Column | What goes in it |
|---|---|
| Lead ID | e.g. L-001 |
| Company | — |
| Target person | Verified names only |
| Job title | As publicly stated |
| Relevant offering | Campaign focus it relates to |
| Evidence of relevance | Short, factual |
| Source (URL + date checked) | — |
| Lead priority | P1–P4 (`lead-qualification`) |
| Score (0–12) | — |
| Owner account | Which profile engages this person (user / executive) |
| Connection status | Not connected / Requested / Connected |
| Stage | One of the 11 stages |
| Last interaction | Date + what |
| Next action | One clear action |
| Follow-up date | Date |
| Conversation status | None / Light / Active / Paused / Closed |
| Campaign | Campaign name |
| Notes | No personal or sensitive data |

Other sheets: **Accounts** (company scores from `target-account-research`), **Activity Log** (date, lead, type, channel, summary, outcome, skill), **Weekly Metrics** (inputs for `weekly-review`, with rate formulas), **Content Calendar** (for `content-calendar`), **Stages** (definitions), **How to use**.

## The 11 stages (with entry rules)

| # | Stage | Enter when… |
|---|---|---|
| 1 | To Research | Account/person identified, not yet checked |
| 2 | Researched | Role and relevance verified with a source |
| 3 | Ready for Engagement | Qualified (P1/P2) with a clear next action |
| 4 | Connection Requested | Request sent |
| 5 | Connected | Request accepted |
| 6 | Conversation Started | They replied with something substantive (not just "thanks") |
| 7 | Qualified Opportunity | A genuine business discussion: a relevant need/initiative shared **and** interest in talking further. **A connection alone never qualifies.** Agree the definition with sales. |
| 8 | Meeting Proposed | A meeting was suggested by either side |
| 9 | Meeting Booked | Date confirmed (hand over per internal process) |
| 10 | Nurture | Relevant but not now; keep warm |
| 11 | Not a Fit | Wrong fit, asked not to be contacted, or sales owns it. Record the reason. |

Rules: stages move forward only on evidence; a like or accept is not a conversation; 2 unanswered follow-ups → Nurture; "not interested" → Not a Fit immediately. Never record an action as done unless the user confirms it.

## Workflow

1. **Set up:** copy the template; confirm column names; agree the *Qualified Opportunity* definition with sales.
2. **Add/update:** from other skills' "Record this" blocks. Check duplicates (same person/company) and owner conflicts.
3. **Log activity:** every request, message, comment, reply, with date.
4. **Daily list:** follow-up date ≤ today, plus P1 leads with no next action.
5. **Weekly hygiene:** stale leads (no action 14+ days), missing sources, missing next actions, roles older than 12 months to re-verify, stage counts for `weekly-review`.

If the workspace folder is connected, edit the .xlsx directly (e.g. with openpyxl, preserving formulas and validations); otherwise give rows to paste or produce an updated file. If the team uses a CRM (HubSpot, Salesforce, Zoho…), map these fields to it instead of duplicating.

## Output format

- Setup: the file + a short "how to use" note.
- Updates: changed rows (before → after) and activity log lines.
- Daily: "Today's follow-ups" (Lead · Stage · Next action · Why · Skill to use).
- Weekly: stage counts, stale leads, data gaps.

## Quality checks

- No invented people, titles or contact details; every lead has a source.
- Every active lead has a next action and follow-up date.
- Stage changes match the entry rules.
- No sensitive personal data.
- The file stays in the user's/company's own storage. Never commit it to a public repo.

## Example prompts

- "Set up my lead tracker."
- "Add these 6 people from today's research as Researched, P2."
- "I sent requests to L-004 and L-007 today, and L-002 replied asking about our onboarding software. Update the tracker."
- "Who do I need to follow up with today?"

## Common mistakes to avoid

- Marking someone qualified because they accepted a request.
- Blank next actions.
- Multiple versions of the tracker.
- Guesses recorded as facts in "Evidence of relevance".

## How it connects to the next skill

Feeds `weekly-review` with activity, engagement and lead metrics, and the daily routine with follow-ups for `linkedin-outreach` and `linkedin-engagement`. New research from `target-account-research`, `decision-maker-research` and `lead-qualification` comes in here.
