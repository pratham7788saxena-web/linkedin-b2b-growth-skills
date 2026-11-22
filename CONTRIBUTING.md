# Contributing

Thanks for helping improve LinkedIn B2B Growth Skills.

## Ground rules for changes

1. **Keep it honest.** Changes must not weaken the never-invent rules, the evidence labels or the "humans send everything" policy. PRs that add scraping, auto-messaging or auto-connecting will be closed.
2. **Keep it generic.** No real company, client or person names in skills or examples. Use clearly fictional examples.
3. **Edit shared files at the source.** Change `shared/ground-rules.md` or `templates/`, then run `python scripts/sync_shared.py`. Don't edit the copies inside `skills/*/references/`.
4. **Keep skills focused.** One job per skill; under ~500 lines in `SKILL.md`; move long detail into `references/`.

## Before opening a PR

```bash
pip install -r scripts/requirements.txt
python scripts/sync_shared.py
python scripts/validate_skills.py
```

## Adding a skill

1. Create `skills/<kebab-name>/SKILL.md` with `name` and `description` frontmatter. The description says *what it does* and *when to use it*, with trigger phrases.
2. Follow the section pattern: Purpose · When to use it · Information to ask for · Workflow · Output format · Quality checks · Example prompts · Common mistakes to avoid · How it connects to the next skill.
3. Run the sync script (it adds `references/ground-rules.md`), then the validator.
4. Add it to the table and diagram in `README.md` and to `CHANGELOG.md`.
