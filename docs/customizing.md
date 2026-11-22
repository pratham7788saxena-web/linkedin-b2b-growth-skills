# Customising

## Change a rule for every skill

Edit `shared/ground-rules.md`, then:

```bash
python scripts/sync_shared.py
python scripts/validate_skills.py
```

## Common changes

| Want to change | Where |
|---|---|
| Evidence labels, banned phrases, tone | `shared/ground-rules.md` → Style / labels |
| Weekly volumes (posts, requests, comments) | `skills/content-calendar/SKILL.md` Step 3 |
| Account scoring criteria or thresholds | `skills/target-account-research/SKILL.md` Step 4 (and the Accounts formula in `scripts/build_tracker_template.py`) |
| Person scoring | `skills/lead-qualification/SKILL.md` Step 1 |
| Pipeline stages | `skills/lead-tracker/SKILL.md` and `STAGES` in `scripts/build_tracker_template.py`, then rebuild |
| Industry roles and titles | `skills/decision-maker-research/SKILL.md` Step 1 |
| Search strings and local titles | `skills/decision-maker-research/references/people-search-playbook.md` |
| Message types and lengths | `skills/linkedin-outreach/SKILL.md` |
| Default post frame and sizes | `skills/brand-creative-design/SKILL.md` §3, or better, your workspace `brand-kit.md` |

## Adapting to an industry

Add an industry reference file to the skills that need it, for example `skills/topic-learning/references/industry-sources.md` listing your standards bodies, analysts and trade press, and `skills/decision-maker-research/references/roles-<industry>.md` with typical titles. Mention the file in the skill's "Read … first" line.

## Keeping your fork private-safe

Add your employer, client and colleague names to `scripts/blocklist.txt`. The validator then fails if any of them slip into a skill.

## Using a real CRM

If your team uses HubSpot, Salesforce, Zoho or similar, keep the stage definitions and map the tracker columns to CRM fields. Don't run two systems.
