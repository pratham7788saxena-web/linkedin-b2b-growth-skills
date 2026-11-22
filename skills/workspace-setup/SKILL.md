---
name: workspace-setup
description: Set up the LinkedIn B2B growth workspace before anything else — create the linkedin-workspace folder, draft company-profile.md (the verified source register) from the company's public website, list claims that need internal confirmation, create the campaign log, content log, voice notes, brand kit and lead tracker, and write the first open questions for management. Use when someone installs these skills for the first time, says "set me up", "start here", "audit our website and LinkedIn", or when another skill finds company-profile.md missing.
---

# Workspace Setup

**Purpose:** Build the shared memory every other skill depends on. Skills don't remember past chats; the workspace does. Stage 0 (Set up).

Read `references/ground-rules.md` first.

## When to use it

- First run after installing the skills.
- A new company, client or brand (one workspace per company).
- Another skill reports that `company-profile.md` is missing or more than ~3 months old.

## Information to ask for

| Needed | Why |
|---|---|
| Company website URL and LinkedIn page URL | The public sources to audit |
| The user's name, role, how technical they are, hours per week | Tunes every later explanation and plan |
| Which accounts they can post from (own profile, company page admin?, an executive who has agreed?) | Decides which content skills apply |
| Any internal material (deck, approved case studies, brand guidelines) | Only source for facts beyond the website |
| Where to put the workspace | Default: `linkedin-workspace/` in the current folder |

## Workflow

1. **Create the folder** with the templates bundled in `assets/`: `company-profile.md`, `campaign-log.md`, `content-log.md`, `voice-notes.md`, `brand-kit.md`, and empty `topic-notes/` and `account-research/` folders. Copy `lead-tracker-template.xlsx` from the `lead-tracker` skill's `assets/` folder as `lead-tracker.xlsx`. Never overwrite an existing file; ask first.
2. **Audit the website.** Open the homepage, every service/product page, about, partners, case studies and contact pages. For each offering, record the exact name, a quote or close paraphrase, who it's for, the URL and the date. Don't summarise from memory or search snippets.
3. **Audit the LinkedIn page** if the user can paste it or it is publicly readable: tagline, About, specialties, follower count, posting frequency, last 5–10 posts and their topics. If you can't read it, ask the user to paste it.
4. **Find the traps** (see ground rules): logo walls, placeholder counters, anonymised percentages, buzzwords the site doesn't actually use, partner claims. List them in section 5 of the profile.
5. **Separate** verified facts, things needing internal confirmation, and your own recommendations. Never mix them.
6. **Write the open questions** for management: the 5 that most block a campaign (focus offering, approved proof points, who approves what, which accounts sales already owns, definition of a qualified lead).
7. **Suggest a `CLAUDE.md` snippet** (see `assets/CLAUDE.md.example`) so every future session reads the workspace first.

## Output format

```
# Workspace Setup — [Company] — [date]
## Created files (paths)
## Verified company summary
| Offering | What the site says | For whom | Source |
## Needs internal confirmation
| Item | Why it's uncertain | Who can confirm |
## Website & LinkedIn observations (facts, then recommendations, labelled)
## Top 5 questions for your manager
## Your first week (3–5 concrete actions)
## Next step
```

## Quality checks

- Every offering has a URL and date you actually opened.
- Nothing from a logo wall is called a customer or partner.
- Recommendations are labelled as recommendations, not facts.
- No existing user file was overwritten.

## Example prompts

- "Set me up. Our site is example.com and our LinkedIn page is linkedin.com/company/example."
- "Audit our website and tell me what we can and can't claim."
- "I'm starting at a new company. Build my LinkedIn workspace."

## Common mistakes to avoid

- Writing the profile from general knowledge of the company rather than its pages.
- Treating marketing copy ("industry-leading") as a verified capability.
- Skipping the questions for management. They unblock everything later.

## How it connects to the next skill

Topic the user doesn't fully understand → `topic-learning`. Ready to plan → fill the campaign brief and use `content-calendar`. Ready to find accounts → `target-account-research`. Profiles need work first → `linkedin-profile-optimizer`.
