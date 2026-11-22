#!/usr/bin/env python3
"""Build the lead tracker template used by the lead-tracker skill.

Usage:  python scripts/build_tracker_template.py
Output: skills/lead-tracker/assets/lead-tracker-template.xlsx
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "skills" / "lead-tracker" / "assets" / "lead-tracker-template.xlsx"
ROWS = 500

HEADER_FILL = PatternFill("solid", fgColor="1F3A5F")
HEADER_FONT = Font(bold=True, color="FFFFFF")
EXAMPLE_FONT = Font(italic=True, color="7F7F7F")

STAGES = [
    ("To Research", "Account/person identified, not yet checked"),
    ("Researched", "Role and relevance verified with a source"),
    ("Ready for Engagement", "Qualified (P1/P2) with a clear next action"),
    ("Connection Requested", "Request sent"),
    ("Connected", "Request accepted"),
    ("Conversation Started", "They replied with something substantive"),
    ("Qualified Opportunity", "Genuine business discussion: relevant need/initiative shared AND interest in talking further. A connection alone never qualifies."),
    ("Meeting Proposed", "A meeting was suggested by either side"),
    ("Meeting Booked", "Date confirmed; hand over per internal process"),
    ("Nurture", "Relevant but not now; keep warm"),
    ("Not a Fit", "Wrong fit, not interested, or owned by sales. Record the reason."),
]


def header(ws, cols, widths=None):
    ws.append(cols)
    for i, cell in enumerate(ws[1], start=1):
        cell.fill, cell.font = HEADER_FILL, HEADER_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        ws.column_dimensions[cell.column_letter].width = (widths or {}).get(i, 18)
    ws.freeze_panes = "B2"
    ws.row_dimensions[1].height = 32


def listval(ws, rng, values):
    dv = DataValidation(type="list", formula1=values, allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(rng)


def main():
    wb = Workbook()

    # How to use
    ws = wb.active
    ws.title = "How to use"
    lines = [
        "LinkedIn B2B Lead Tracker - how to use",
        "",
        "1. Leads: one row per person. Only verified names/titles, always with a source URL and date checked.",
        "2. Every active lead needs a Next action and a Follow-up date.",
        "3. Move Stage only on evidence (see Stages). A connection or a like is never a qualified lead.",
        "4. Log every request, message, comment and reply in Activity Log.",
        "5. Each week fill one Weekly Metrics row and run the weekly-review skill.",
        "6. Plan content in Content Calendar (content-calendar skill).",
        "7. No personal phone numbers/emails or private information. Keep this file in your own storage; never commit it to a public repo.",
        "8. Delete the example rows before use.",
    ]
    for line in lines:
        ws.append([line])
    ws["A1"].font = Font(bold=True, size=14)
    ws.column_dimensions["A"].width = 120

    # Leads
    ws = wb.create_sheet("Leads")
    cols = ["Lead ID", "Company", "Target person", "Job title", "Relevant offering",
            "Evidence of relevance", "Source (URL + date checked)", "Lead priority", "Score (0-12)",
            "Owner account", "Connection status", "Stage", "Last interaction", "Next action",
            "Follow-up date", "Conversation status", "Campaign", "Notes"]
    header(ws, cols, {6: 36, 7: 34, 13: 28, 14: 30, 18: 30})
    ws.append(["L-000", "EXAMPLE - delete", "(verified name only)", "(as publicly stated)",
               "e.g. AP Automation", "e.g. Spoke at [event] about invoice processing delays",
               "https://... (checked YYYY-MM-DD)", "P2", 8, "Me", "Not connected", "Researched",
               "-", "Comment on next relevant post", "YYYY-MM-DD", "None", "Campaign name", "Example only"])
    for c in ws[2]:
        c.font = EXAMPLE_FONT
    listval(ws, f"H2:H{ROWS}", '"P1,P2,P3,P4"')
    listval(ws, f"J2:J{ROWS}", '"Me,Executive,Other colleague"')
    listval(ws, f"K2:K{ROWS}", '"Not connected,Requested,Connected"')
    listval(ws, f"L2:L{ROWS}", f"=Stages!$B$2:$B${len(STAGES) + 1}")
    listval(ws, f"P2:P{ROWS}", '"None,Light,Active,Paused,Closed"')

    # Accounts
    ws = wb.create_sheet("Accounts")
    cols = ["Account ID", "Company", "Type / region", "Fit (0-3)", "Relevance (0-3)", "Evidence (0-3)",
            "Conversation (0-3)", "Total", "Priority (A-D)", "Key signals (URL + date)",
            "Related offering (source)", "Why it may not fit", "Needs research", "Campaign",
            "Sales already engaged?"]
    header(ws, cols, {10: 40, 11: 30, 12: 30, 13: 30})
    for r in range(2, ROWS + 1):
        ws[f"H{r}"] = f'=IF(COUNT(D{r}:G{r})=0,"",SUM(D{r}:G{r}))'
        ws[f"I{r}"] = (f'=IF(H{r}="","",IF(H{r}>=10,"A",IF(H{r}>=7,"B",IF(H{r}>=4,"C","D"))))')
    for col in "DEFG":
        dv = DataValidation(type="whole", operator="between", formula1="0", formula2="3", allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(f"{col}2:{col}{ROWS}")
    listval(ws, f"O2:O{ROWS}", '"Unknown,No,Yes - do not contact"')

    # Activity Log
    ws = wb.create_sheet("Activity Log")
    header(ws, ["Date", "Lead ID", "Activity type", "Account / channel", "Summary", "Outcome", "Skill used"],
           {5: 50, 6: 30})
    listval(ws, f"C2:C{ROWS * 4}",
            '"Research,Follow,Comment,Connection request,Message,Follow-up,Resource shared,Meeting request,Reply received,Meeting booked"')
    listval(ws, f"D2:D{ROWS * 4}", '"Personal profile,Company page,Executive profile,Other"')

    # Weekly Metrics
    ws = wb.create_sheet("Weekly Metrics")
    cols = ["Week starting", "Campaign", "Personal posts", "Company posts", "Executive posts",
            "Comments made", "Accounts researched", "People identified", "Connection requests sent",
            "Accepted", "Acceptance rate", "Messages sent", "Replies", "Reply rate",
            "Conversations started", "Qualified opportunities", "Meetings proposed", "Meetings booked",
            "Followers gained", "Relevant engagement (target roles/accounts)", "Notes"]
    header(ws, cols, {20: 30, 21: 40})
    for r in range(2, 105):
        ws[f"K{r}"] = f'=IF(OR(I{r}="",I{r}=0),"",J{r}/I{r})'
        ws[f"N{r}"] = f'=IF(OR(L{r}="",L{r}=0),"",M{r}/L{r})'
        ws[f"K{r}"].number_format = ws[f"N{r}"].number_format = "0%"

    # Content Calendar
    ws = wb.create_sheet("Content Calendar")
    header(ws, ["Date", "Channel", "Target audience", "Topic", "Customer problem", "Main message",
                "Format", "CTA", "Research / approval needed", "Campaign pillar", "Skill", "Status",
                "Approval note", "Link once published"], {5: 30, 6: 34, 9: 30, 13: 30})
    listval(ws, f"B2:B{ROWS}",
            '"Personal profile,Company page,Executive (approved only),Article,One-pager"')
    listval(ws, f"L2:L{ROWS}", '"Idea,Drafting,In approval,Approved,Scheduled,Published"')

    # Stages
    ws = wb.create_sheet("Stages")
    header(ws, ["#", "Stage", "Enter when..."], {1: 5, 2: 24, 3: 100})
    for i, (name, rule) in enumerate(STAGES, start=1):
        ws.append([i, name, rule])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
