# People-Search Playbook (beyond "search the job title")

The user runs these searches by hand in LinkedIn and pastes results back. No scrapers, auto-connect tools or email finders.

## 1. Search by what people work on, not their title
Many relevant people have plain titles ("Senior Manager") and put the real work in their headline or About. Use the Keywords field, then filter **Current company**.

LinkedIn Boolean notes: `AND` / `OR` / `NOT` in capitals; phrases in straight quotes; brackets group terms. No wildcards (`*`), so list plurals yourself.

Template: owner / programme lead
```
("<topic phrase>" OR "<synonym>" OR "<related term>") AND (head OR director OR "vice president" OR VP OR "general manager" OR lead OR architect) NOT (sales OR "account manager" OR recruiter OR intern)
```

Template: champions who feel the daily pain
```
("<daily-work term>" OR "<team name>" OR "<tool category>") AND (manager OR lead OR head) NOT (sales OR recruiter)
```

Example (data platform campaign):
```
("data platform" OR "data engineering" OR "data governance" OR lakehouse) AND (head OR director OR VP OR lead OR architect) NOT (sales OR recruiter OR intern)
```

## 2. Search by the vendor stack they just bought
If an account announced a new platform, the people running it own integration, migration and adoption. Add the product name to Keywords with the company in Current company, e.g. `"<Vendor Product>" AND (implementation OR migration OR platform)`.

## 3. Past-company filter: vendor and consultancy alumni
Current company = the account; Past company = major vendors or consultancies in your space. Alumni often own vendor management or integration, and already understand how services partners work.

## 4. Posts search: find who talks, not who holds the title
LinkedIn search → **Posts** → keyword → Date posted: past month → Author company: the account.
Someone who posted on the topic in the last 30 days is a better first contact than a silent VP.

## 5. Reactions and comments on the announcement
Open the company's or vendor's post about the signal you recorded. Colleagues who comment or reshare with "proud of the team" are often the project team. Read only; log names as *To Research*.

## 6. Industry bodies and programmes
Standards bodies, working groups, award programmes and industry "catalyst"/pilot projects often list participants by name and company.

## 7. Event agendas (this year and next)
Speaker pages give name, exact title and session topic, which is a ready-made conversation angle. Next year's agenda is often already published.

## 8. Local titles and languages
Titles differ by market. Add local terms when results look thin, for example:
- Germany: `Leiter`, `Bereichsleiter`, `Abteilungsleiter`
- Australia: `"Executive General Manager"`, `"General Manager"`
- Gulf region: `"Senior Director"`, `"Senior Manager"`
- Also try the local-language word for "head" or the function name.

## 9. Job posts as an org map
Search the account's Jobs for your topic. Ads often name the team, the tools and sometimes "Meet the hiring team". A role being hired = a live programme. It's a signal of activity, not of a problem they want you to solve.

## 10. If Sales Navigator is available
Save A accounts as an Account list. Lead filters: Function, Seniority (Director, VP, CXO), Keywords from section 1. Useful signals: "Posted on LinkedIn in past 30 days" and "Changed jobs in past 90 days" (new leaders often review partners early). Sections 1–9 work in free LinkedIn.

## Free-account tips
Free accounts limit monthly searches. Search narrow (one company + one keyword set) and save repeat searches. Per account:
1. Company page → People → type one keyword at a time.
2. People search → Current company + Title Boolean + `NOT (sales OR recruiter OR intern)`.
3. Posts → keyword → past month → Author company.
4. Paste the 5–10 best headlines into Claude: "Which 2–3 are the right people, why, and who should contact each?"

## Verification before anything goes in the tracker
1. Name, company and title appear on a public source dated within ~12 months, or the row is "To Research: confirm current role".
2. Record source URL and date checked.
3. The conversation angle comes from something the person said or did publicly.
4. 2–3 well-researched people per account.

## Suggested weekly rhythm
Mon: 2 accounts × sections 1–2 · Tue: posts search for all A accounts · Wed: events and industry bodies · Thu: verify and add to tracker · Fri: weekly review.
