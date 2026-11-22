---
name: decision-maker-research
description: Identify the right decision-makers, influencers and champions inside target companies — mapping roles first, then finding people through public professional sources, verifying current role and company, noting their public activity, and writing a conversation angle per person based only on what they said or did publicly. Includes a manual LinkedIn people-search playbook (Boolean strings, posts search, event agendas, vendor-stack and alumni filters). Use whenever someone asks who to contact at a company, to find decision-makers, research a person or profile before reaching out, map a buying committee, rank a pasted list of LinkedIn search results, or prepare a contact list.
---

# Decision-Maker Research

**Purpose:** Find the right people at a target account and understand what they publicly care about, so any engagement is relevant. Stage 4 (Find the Right People).

Read `references/ground-rules.md` first. Key rule: **never invent a person, name, title, profile URL, responsibility or contact detail.** For search techniques, read `references/people-search-playbook.md`.

## When to use it

- After `target-account-research` ranks an account A or B.
- When the user finds a person (a post, a speaker list) and asks if they're relevant.
- Before any outreach (`linkedin-outreach`) or comment (`linkedin-engagement`) to a specific person.

## Information to ask for

| Needed | Notes |
|---|---|
| Company (and its account notes) | Context for relevance |
| Campaign focus offering | Decides which roles matter |
| Names already found | Verify rather than replace |
| Profile text or search results the user pastes (optional) | The user copies public info from LinkedIn themselves; you don't scrape |
| Which account will reach out (user, executive) | Avoid double contact |

## Workflow

### Step 1: Map roles first, people second
For the campaign focus, list the roles that usually care and classify each:

| Role type | Typical titles (adapt to the offering) | Usually cares about |
|---|---|---|
| Decision-maker | C-level, VP, Head of [function], Director | Strategy, budget, risk, vendor choice |
| Influencer / evaluator | Architect, programme lead, transformation lead, senior engineer | Architecture fit, standards, integration effort |
| User / champion | Manager or lead who lives with the problem daily | Manual work, data quality, incidents, deadlines |
| Gatekeeper / other | Procurement, security, finance | Risk, compliance, cost |

Explain in one line why each role matters *for this campaign*. Titles vary by company and country. Mark the mapping as [INDUSTRY] guidance.

### Step 2: Find people through public, professional sources
Leadership pages, press releases, annual reports, conference speaker pages, articles, podcasts/webinars, public posts the user shares, search results that show a public profile headline. See the playbook for LinkedIn search methods the user runs by hand. No scraping, no profile- or email-harvesting tools.

### Step 3: Verify each person
"Verified" = a public source dated within ~12 months shows name, company and role. If the newest source is older, or sources conflict, mark **[NEEDS RESEARCH: confirm current role on LinkedIn]**. If no name is found for a role, leave it blank and say how the user can find it (e.g. company page → People → search a keyword).

### Step 4: Note public activity
Talks, posts, articles, quotes, projects they've publicly led: topic, link, date. Nothing about private life.

### Step 5: Conversation angle
One sentence on a genuine topic to discuss, based on their public activity and the campaign problem. It must be something they said or did publicly, never a guessed pain point. No public activity → "follow and observe first".

### Step 6: Assign an owner
Senior decision-makers may suit the executive's account (if one is active); practitioners suit the user's. One owner per person.

## Output format

```
# People Map — [Company] — [Campaign] — [date]
## Role map for this campaign
## People found
| Name | Current role (as stated) | Company | Role type | Why relevant | Source + date checked | Verified? | Owner |
## Person notes
### [Name] — [Role]
- Public activity / topics: … (link, date)
- Conversation angle: …
- What we do NOT know: …
- Suggested first step: follow / engage with a post / connect
## Roles with no verified person yet (how to find them)
## Record this (tracker rows)
## Next step
```

## Quality checks

- Zero invented names, titles, URLs, emails or phone numbers.
- Every person has a source link and date checked.
- Old or conflicting information is flagged, not smoothed over.
- "Why relevant" links the role to the campaign problem, not just "senior person".
- Angles come from public activity, not assumed problems.
- 2–5 well-researched people per account beat 15 names.

## Example prompts

- "For Company X (from my account list), who should I reach for our data-platform campaign?"
- "Here's the public part of a LinkedIn profile I copied. Is this person relevant and what could we talk about?"
- "I searched Company Y on LinkedIn. Here are 10 names and headlines. Which 2–3 are the right people and why?"
- "Give me Boolean search strings to find people who run procurement at hospital groups."

## Common mistakes to avoid

- Guessing names from email patterns or inventing plausible titles.
- Assuming the CEO is the right first contact.
- Treating a 3-year-old conference bio as current.
- Writing "they are struggling with X" when they only spoke about X.
- Collecting personal contact details.

## How it connects to the next skill

Each person → `lead-qualification` for a score and next action, and → `lead-tracker` at *Researched*. Their public posts → engagement opportunities for `linkedin-engagement`.
