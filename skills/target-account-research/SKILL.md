---
name: target-account-research
description: Build an ideal customer profile (ICP) and research target companies that may be relevant to one of the user's offerings, using public evidence (news, filings, case studies, job posts, event agendas), then score and rank them on fit, relevance, evidence and conversation potential while separating verified facts, assumptions and gaps. Use whenever someone asks to find target accounts, build an account list or ICP, check whether a company is a good fit, research a company before outreach, or asks "which companies should we target for X".
---

# Target Account Research

**Purpose:** Find companies where an offering is plausibly relevant, based on evidence, not on "they're in our industry, so they're a lead". Stage 3 (Find Target Accounts).

Read `references/ground-rules.md` and the workspace `company-profile.md` first.

## When to use it

- After a campaign brief exists (focus offering, segment, objective).
- To build or refresh an account list.
- To check one company before engaging its people.
- When a company appears in the news, at an event, or engages with your content.

## Information to ask for

| Needed | Default if not given |
|---|---|
| Campaign focus offering | Ask. Don't assume. |
| Segment: company type, region, size/tier | Ask; suggest options |
| Company names already in mind | — |
| Exclusions: existing customers, competitors, partners, accounts sales already works | Ask; note "unknown" if not given |
| How many accounts | 5–10 per research round |

## Workflow

### Step 1: Ideal customer profile
A small table: company type, region, size, technology or business situation, likely trigger events, roles to reach, and **disqualifiers**. Link each element to a verified offering in `company-profile.md`. Mark elements that are [ASSUMPTION]s to validate with sales.

### Step 2: Long list
Public sources only: company websites and newsrooms, annual reports and investor decks, regulator filings, industry-body case studies, vendor/partner press releases, reputable trade press, job postings, conference speaker lists. Never scrape LinkedIn.

### Step 3: Relevance signals
Look for public evidence such as:
- Transformation, migration, consolidation or vendor-replacement announcements
- Expansion, mergers or acquisitions (two systems to combine → integration pressure)
- Public commitments to automation, AI, cloud, compliance or standards relevant to the offering
- A new platform just bought from a vendor (someone now owns integration and adoption)
- Job postings for roles that would run or buy this kind of work
- Leaders speaking publicly about the problem

Open each source; record what it says, the URL and the date. Older than ~18 months = weak signal; say so. A job post shows activity, not a problem they want *you* to solve.

### Step 4: Score each company (0–3 per criterion, max 12)

| Criterion | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Company fit** (matches ICP) | Outside ICP | Partly | Mostly | Clearly fits |
| **Relevance to a verified offering** | No link | Weak/indirect | Clear link to one offering | Strong link, specific problem area |
| **Public evidence of a relevant initiative** | None | Old or vague | Recent, general | Recent, specific, sourced |
| **Opportunity for a meaningful conversation** | No reachable angle | Generic angle | A real topic to discuss | Specific, timely topic + visible people |

Priority: **A (10–12)** engage this campaign · **B (7–9)** research further / nurture · **C (4–6)** monitor · **D (0–3)** not now.

Explain every score in one line. A score is about *relevance for a conversation*, not buying intent.

### Step 5: Facts, assumptions, gaps
For each account: Verified facts (with source) · Reasonable assumptions (and why) · Needs research (what and where).

### Step 6: Recommend
Rank accounts, pick the top 3–5 for `decision-maker-research`, and say why the others are lower or excluded. If the company has already picked a platform vendor, the angle is usually *around* that platform (integration, data, adoption), not replacing it. Mark that as an [ASSUMPTION] to confirm with sales.

## Output format

```
# Target Accounts — [Campaign] — [date]
## ICP for this campaign (table + disqualifiers)
## Ranked account list
| Rank | Company | Type / region | Fit | Relevance | Evidence | Conversation | Total | Priority | One-line reason |
## Account profiles
### [Company]
- What they do (1–2 lines, sourced)
- Relevant signals: bullet, URL, date
- Possible problem area: [ASSUMPTION] …
- Related offering: [VERIFIED] … (URL)
- Why it may NOT be a fit / risks / sensitive topics to avoid
- Verified facts / Assumptions / Needs research
- Roles to look for (for decision-maker-research)
## Excluded or deprioritised (and why)
## Record this (account-research/<company>.md, tracker "Accounts" sheet)
## Next step
```

## Quality checks

- Every signal has a URL and date you actually opened.
- No company is called a lead, customer or "in market" without evidence.
- Existing relationships are not inferred from logos. Ask the user to check with sales.
- Scores are explained and consistent.
- At least one "why it may not fit" point per account.
- Realistic volume: 8 accounts with real evidence beat 50 thin ones.

## Example prompts

- "Campaign focus is route-planning software. Find 8 mid-size logistics firms in Germany and the Netherlands that might be relevant, and rank them."
- "Is Company X a good fit for our managed security offering? Research them."
- "Build an ICP for our employee-onboarding software targeting hospital groups."

## Common mistakes to avoid

- Treating every company in the industry as a lead.
- Using one old press release as "evidence".
- Guessing problems ("they must have data issues").
- Including competitors, partners or existing customers without checking.
- Referencing a company's crisis (outage, breach, layoffs) as an outreach angle.

## How it connects to the next skill

A and strong B accounts → `decision-maker-research`. Each account → `lead-tracker` "Accounts" sheet. Patterns across accounts → themes for `content-calendar`.
