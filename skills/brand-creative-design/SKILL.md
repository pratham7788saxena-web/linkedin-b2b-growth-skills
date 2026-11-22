---
name: brand-creative-design
description: Design on-brand LinkedIn visuals from the user's brand kit — single-image posts, carousels/document posts, profile and company banners, quote and stat cards, one-pager layouts and partner co-branded creatives — with a fixed post frame, three variants by default, claim placeholders for anything unapproved, and a pre-handover checklist for logo, colour, type, contrast and partner-logo rules. Use for any LinkedIn creative, image, banner, carousel design or visual once the words are ready.
---

# Brand Creative Design

**Purpose:** Turn an approved message into a finished visual built on the brand kit. The words come from the content skills; this skill decides how they look. The point is recognition and trust: when every post uses the same frame, logo, colours and type, buyers start to know the brand at a glance. A visual with an unbacked claim loses that trust faster than a plain one gains it.

Read `references/ground-rules.md` first.

## 1. Load the brand kit first

- Read `brand-kit.md` in the workspace and the official logo/font files it points to. Where this skill and the official guidelines disagree, **the guidelines win**.
- No brand kit yet? Offer to fill `brand-kit.md` together from the website and any guidelines PDF. Until then, use a neutral, clearly temporary palette and say so.
- **Never redraw, trace or approximate a logo,** and never re-set a wordmark in another font. Use the official files. If they can't be reached, ask for them instead of improvising.

## 2. Before designing

1. **Check facts** against `company-profile.md` and the active campaign. Any number, client, partner, result or "first/only/leading" claim needs approval. If not approved, show a visible placeholder such as `[RESULT – needs approval]`. Keep clients anonymised unless consent is recorded.
2. **Settle the brief**, one line each: audience, the single message, format and size, and the account (company page, personal, or an executive, who must approve).
3. **Make three variants by default**, e.g. two light and one dark. Vary the layout, not the brand.

## 3. Default frame (override with `brand-kit.md`)

- **1080 × 1080 post** (or 1080 × 1350 portrait): ~80 px safe margin.
- **Header:** logo top-left at a fixed size; an optional topic tag top-right in the label font.
- **Content block:** eyebrow label → headline (≤ 12 words, 2–4 words in the accent colour) → subhead (≤ 2 lines).
- **Footer:** a thin rule, website URL left, "Swipe →" / page count / follow CTA right.
- **One decoration** at most (e.g. a large faint brand mark bleeding off a corner).
- **Type:** max three sizes per creative; nothing under ~22 px on a 1080 canvas; body in carousels ≥ 26 px. No italics-for-emphasis, exclamation marks or emoji unless the kit says otherwise.
- **Colour:** ~60% background, 30% text, 10% accent. Contrast ≥ 4.5:1 for text (3:1 for ≥ 24 px). No light accent colours as text on white.
- **Carousels:** same frame on every slide; one idea per slide; final slide = CTA; export as PDF.
- **Banners:** personal 1584 × 396, company 1128 × 191. Keep text away from the area the profile photo/logo covers.
- **Icons:** one outline icon set, one stroke weight. **Diagrams:** simple boxes and arrows, labels in the label font. **Photos:** real, relevant imagery; no handshake stock photos.

## 4. Partner and third-party logos

- Use the partner's **official partner-programme logo file**, following their published co-branding rules. Never draw, generate, trace, recolour or recreate another company's logo; without an official file, leave a labelled "Partner logo area".
- Say "partner" only if confirmed. Don't name the tier or use programme badges unless their rules allow it.
- Keep the two logos separate (never merged), usually at equal visual weight with clear space and a divider, as the partner's rules specify.
- Write product names exactly as the partner does. Don't imply the partner endorses your results.

## 5. How to build

- **HTML → PNG (works anywhere):** build HTML at the exact pixel size, embed the brand fonts locally, position frame elements absolutely, and render with a headless browser at 2× device scale. Check the fonts didn't fall back to a default serif.
- **Design tools:** Claude design/canvas artifacts, Figma, Canva or similar are fine. Install the kit's colours and fonts as styles first.
- **Image generators** are fine for text-free backgrounds or illustrations only. Add text and logos afterwards in the layout.
- One file/artboard per variant, size in the name (e.g. `post-month-end-close_A-light_1080.png`).

## 6. Check before handing over

- [ ] Official logo file, correct version for the background, at the frame position.
- [ ] Only kit colours and fonts; ≤ 3 type sizes; contrast passes.
- [ ] Headline ≤ 12 words; subhead ≤ 2 lines; nothing below minimum size.
- [ ] Footer and URL present; same frame across carousel slides.
- [ ] Every claim approved or shown as a placeholder; no unconsented client names; no partner tier.
- [ ] Partner logo is the official file or flagged as a placeholder.

## 7. Reply to the user

Keep it short: what was made (variants and sizes), what to swap or confirm, who approves it, and an offer to draft the caption with `company-page-content` or `personal-linkedin-content`.

## Example prompts

- "Design a carousel for our 'month-end close' post. 7 slides, light theme."
- "Make three variants of a stat card for this approved quote."
- "Create a company banner and a founder banner from our brand kit."
- "We're announcing a partnership. Design a co-branded post that follows their partner logo rules."

## Common mistakes to avoid

- Regenerating a logo with an image model.
- A different layout on every post (no recognition).
- Squeezing a 120-word caption onto the image.
- Implying results or partnerships with visuals (badges, "trusted by" strips) that aren't approved.
