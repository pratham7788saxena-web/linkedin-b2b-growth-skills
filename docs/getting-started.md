# Getting Started

## Day 1: foundation (about 1 hour)

| Step | Say to Claude | Skill | You do manually |
|---|---|---|---|
| 1 | "Set me up. Website: …, LinkedIn page: …" | `workspace-setup` | Paste your company page's About text if Claude can't read it |
| 2 | (answer the 5 questions it gives you, after asking your manager) | — | Ask your manager; paste the answers back |
| 3 | "Audit my LinkedIn profile. Here's my headline and About: …" | `linkedin-profile-optimizer` | Update your profile |
| 4 | "Help me fill the brand kit from our guidelines PDF." | `brand-creative-design` | Attach logo files and guidelines |

## Week 1: first campaign

| Day | Say to Claude | Skill |
|---|---|---|
| Mon | "Teach me [topic]. We're running a campaign on it for [segment]." | `topic-learning` |
| Mon | "Fill the campaign brief and plan the next 4 weeks." | `content-calendar` |
| Tue | "Find 8 [segment] companies that might be relevant. Rank them." | `target-account-research` |
| Wed | "Who should I reach at the top 3 accounts? Give me search strings." | `decision-maker-research` |
| Thu | "Here are the people I found. Qualify them." | `lead-qualification` |
| Daily | "Quick: [pasted post]" | `linkedin-engagement` |
| As due | "Write a connection request to [name]. Hook: [link]." | `linkedin-outreach` |
| Fri | "Weekly review: [numbers]." | `weekly-review` |

## A daily routine (30–45 minutes)

1. **5 min:** "Who do I follow up with today?" (`lead-tracker`)
2. **15–20 min:** read target-account posts; comment on 3–5 using `linkedin-engagement` quick mode.
3. **10 min:** send the day's personalised requests or follow-ups (`linkedin-outreach`). You send them.
4. **5 min:** "I sent X, Y replied: … Update the tracker."

## Working across several chats or sessions

Each session only knows what's in the workspace. When something is decided, say **"record this"** so the right workspace file is updated. Starting a new chat? Begin with: *"Read linkedin-workspace/company-profile.md and the active campaign in campaign-log.md, then …"*. A `CLAUDE.md` does this automatically in Claude Code.

## Approvals

Anything about results, customers, partners, numbers, roadmap or an executive's voice is flagged `[NEEDS APPROVAL]`. Set up one approval route (e.g. a team channel), agree deadlines (e.g. company drafts by Wednesday for next week), and record approvals in the tracker's Content Calendar.
