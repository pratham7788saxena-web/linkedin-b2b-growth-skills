---
name: linkedin-outreach
description: Write natural, personalised LinkedIn messages for B2B prospects — connection requests, first message after connecting, follow-ups, replies to a prospect's post, sharing a useful resource, starting a business conversation, asking for a meeting when appropriate, and a polite close when someone isn't interested — based only on real public information, with a note explaining the personalisation used. Use whenever someone asks to write a connection request, LinkedIn DM, InMail, follow-up, intro message, meeting request, or "what should I say to this person", even if they only paste a profile or post.
---

# LinkedIn Outreach

**Purpose:** Start and build genuine professional conversations without hard selling or fake familiarity. Stages 8 (Connect) and 9 (Nurture).

Read `references/ground-rules.md` first. The user sends every message themselves. Never suggest automation tools or sequences that send on their behalf.

## When to use it

- `lead-qualification` recommended "send a connection request" or "start a conversation".
- Someone accepted, replied, or engaged with content.
- A follow-up is due in the tracker.
- The user wants to share a resource or propose a meeting.

## Information to ask for

| Needed | Why |
|---|---|
| Person: name, role, company | Accuracy |
| The real hook: a post, talk, article, shared event/group, with link | The only basis for personalisation |
| Message type and history so far | Stage-appropriate tone |
| Campaign focus and any approved resource to share | Relevance |
| The user's real relationship to them (none, met at event…) | No invented familiarity |
| Which account is sending (user / executive) | Voice and ownership |

**No real hook?** Say so and recommend following or commenting first (`linkedin-engagement`) rather than writing a generic message.

## The eight message types

| # | Type | Goal | Length | Selling? |
|---|---|---|---|---|
| 1 | Connection request | Earn an accept | ≤ 300 chars (LinkedIn's limit; keep ~200). Free plans cap personalised notes, so a no-note request after engaging is often better | None |
| 2 | First message after connecting | Thank + open a light, relevant thread | 40–80 words | None |
| 3 | Follow-up (no reply) | Add value once, low pressure | 30–60 words | None |
| 4 | Response to their post (DM) | Continue a topic they raised | 40–80 words | None |
| 5 | Sharing a useful resource | Give something relevant | 40–80 words | Soft: resource, not pitch |
| 6 | Starting a business conversation | Ask their view on the problem; mention your relevant work briefly | 60–100 words | Light, only after rapport |
| 7 | Meeting request | Propose a short, specific call | 50–90 words | Yes, only after a two-way exchange and a clear reason |
| 8 | Graceful close | Thank them when they're not interested; leave the door open | 20–40 words | None |

Rules of thumb: max **2 follow-ups** with no reply, **5–7+ days** apart, then Nurture. Ask for a meeting only after they've replied with interest or asked a question you can help with. Stop immediately if someone declines or asks for no further contact.

## Workflow

1. **Confirm the hook.** Quote the public thing you're referring to (link/date). Older than ~4 weeks → reference lightly or find a newer one.
2. **Pick the message type** from history.
3. **Draft 2 versions** (e.g. curious vs direct). Both natural and concise.
4. **Personalisation note:** what public information was used, why it's relevant, what was deliberately *not* assumed.
5. **Fact check:** any company statement with [VERIFIED] source or [NEEDS APPROVAL].
6. **Timing:** when to send, when to follow up, tracker update.

## Writing rules

- Sound like a real person writing to a peer. No visible template.
- "I noticed you spoke about X", never "I know you're struggling with X".
- No invented familiarity ("great to reconnect", "as we discussed") unless true.
- One idea per message, one question at most.
- No links or attachments in connection requests. No calendar links in a first message.
- Honesty about the user's role is disarming: e.g. "I work in marketing at [company] and I'm learning this space; your talk helped."
- Banned filler: "I hope this finds you well", "synergies", "innovative solutions", "quick 15-minute call to explore".

## Output format

```
## [Message type] — [Name], [Role], [Company]
Hook used: "[quote/description]" — [link] ([date])

**Version A (curious)**
[message]
(characters/words: n)

**Version B (direct)**
[message]

Why this is relevant to them: …
Personalisation used: … | Not assumed: …
Fact check: …
Send: [when] · Follow up: [date, if no reply] · Tracker: stage → [stage]
```

## Quality checks

- Connection request within the limit; no pitch.
- Every personal reference matches a real public source.
- No unverified company claim.
- Readable on a phone in 10 seconds.
- If the recipient asked "how did you know that?", the answer is "your public post/talk".

## Example prompts

- "Write a connection request to [Name], Head of Data at Company X. She spoke at [event] about data quality — here's the link."
- "He accepted my request yesterday. Write a first message."
- "No reply after 8 days. Write a follow-up that shares our blog post on supplier onboarding."
- "We've exchanged three messages about slow month-end close. Is it time to ask for a meeting?"
- "She said they're not looking right now. Write a polite reply."

## Common mistakes to avoid

- Pitching in the connection request.
- Generic flattery ("impressed by your profile").
- A meeting request right after accepting.
- Following up more than twice, or daily.
- Personalising from a private source or a guess.

## How it connects to the next skill

Every message → update `lead-tracker` (stage, last interaction, next action, follow-up date). Genuine interest → re-score in `lead-qualification`. Need something to share → `one-pager-creator` or a recent company post. Results → `weekly-review`.
