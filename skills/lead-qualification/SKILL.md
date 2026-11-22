---
name: lead-qualification
description: Score and prioritise B2B prospects (people at target accounts) on company fit, role relevance, evidence of a relevant initiative, and ability to start a genuine conversation, then recommend exactly one next action each — research further, follow their content, comment on a post, send a connection request, start a conversation, nurture, or do not prioritise. Use whenever someone asks which leads to focus on, to qualify or rank prospects, decide who to contact first, re-prioritise a tracker, or review a list of people from research or events.
---

# Lead Qualification

**Purpose:** Decide where limited time goes. Stage 5 (Qualify). A high score means *"worth a thoughtful conversation now"*. **It does not mean the person is ready to buy.**

Read `references/ground-rules.md` first.

## When to use it

- After `decision-maker-research` produces a people list.
- After an event or webinar, or when people engage with your content.
- Weekly, to re-prioritise the tracker when new evidence appears.

## Information to ask for

- The people list (from research or the tracker) with their account scores.
- Campaign focus and objective.
- Interaction history (engaged, accepted, replied?).
- Whether sales already owns any of these accounts.

## Workflow

### Step 1: Score four criteria (0–3 each, max 12)

| Criterion | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Company fit** (account priority) | D | C | B | A |
| **Role relevance** | Unrelated | Adjacent | Influencer/user for the problem | Owner/decision-maker for the problem |
| **Evidence of relevant initiative** (public, sourced) | None | Company-level, vague or old | Company-level, recent | The person spoke/posted about it recently |
| **Ability to start a genuine conversation** | No activity, no shared context | Some activity, generic | Recent relevant post/talk to respond to | Recent relevant activity + shared context (event, group, engaged with your content) |

One-line reason per score. Missing information → score 0 or 1 and mark [NEEDS RESEARCH]. Don't fill gaps with guesses.

### Step 2: Priority
- **P1 (10–12)**: engage this week
- **P2 (7–9)**: warm up first (follow, comment), then connect
- **P3 (4–6)**: nurture / monitor
- **P4 (0–3)**: do not prioritise now

### Step 3: Exactly one next action

| Action | Use when |
|---|---|
| Research further | Key facts missing or unverified |
| Follow their content | Relevant but nothing recent to respond to |
| Comment on a relevant post | They posted something relevant in the last ~2 weeks (→ `linkedin-engagement`) |
| Send a connection request | A real, specific reason exists (→ `linkedin-outreach`) |
| Start a conversation | Already connected and a genuine topic exists (→ `linkedin-outreach`) |
| Keep for nurturing | Relevant but timing/evidence weak |
| Do not prioritise | Poor fit, sales owns it, or no relevance |

Explain why, and what would move the person up.

If personalised connection notes are limited on the user's plan, the default sequence is: engage first → connect (with or without a note) → message after acceptance.

### Step 4: Sanity check
- One company dominating the top? Spread effort unless it's clearly the best.
- More than ~15 "connect this week"? Trim to what the user can personalise properly.

## Output format

```
# Lead Qualification — [Campaign] — [date]
Reminder: scores show conversation relevance, not buying readiness.
| Person | Company | Role | Fit | Role | Evidence | Conversation | Total | Priority | Next action | Why | What would raise it |
## Notes on P1 leads (2–3 lines each, with sources)
## Gaps to research
## Record this (tracker: priority, next action, follow-up date)
## Next step
```

## Quality checks

- Every score has a reason and, where relevant, a source.
- No one is called "hot", "ready to buy" or a "qualified opportunity" from LinkedIn activity alone.
- Each person has one clear next action with a suggested date.
- Weekly workload is realistic.
- People sales already owns are flagged, not pursued.

## Example prompts

- "Here are the 9 people from Company X and Y. Qualify them and tell me who to approach first."
- "This Director liked our company post. Re-score her and suggest the next step."
- "Re-prioritise my tracker for this week."

## Common mistakes to avoid

- Confusing seniority with relevance.
- Treating a like, follow or accepted request as buying intent.
- Recommending "connect" for everyone.
- Scoring from assumptions rather than evidence.

## How it connects to the next skill

Comment → `linkedin-engagement`. Connect / start a conversation → `linkedin-outreach`. Follow / nurture → stay visible through `personal-linkedin-content` and `company-page-content`. All priorities → `lead-tracker`.
