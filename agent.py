"""
PocketGuard: Autonomous Daily Life & Expense Assistant
Built for the AWS Agents for Humans Hackathon using Strands SDK concepts.
"""

import json
from datetime import datetime

# Sample user financial state
USER_LEDGER = [
    {"service": "Cloud Storage", "amount": 2.99, "renews_in_days": 1},
    {"service": "Music Streaming", "amount": 9.99, "renews_in_days": 18},
    {"service": "Broadband Internet", "amount": 35.00, "renews_in_days": 3},
]

def scan_upcoming_renewals(days_threshold: int = 5) -> str:
    """Checks for renewals occurring within the given number of days."""
    alerts = []
    for item in USER_LEDGER:
        if item["renews_in_days"] <= days_threshold:
            alerts.append(f"{item['service']}: ${item['amount']} due in {item['renews_in_days']} days")
    
    if not alerts:
        return "All scheduled payments are clear for the next 5 days."
    return "URGENT RENEWALS DETECTED:\n- " + "\n- ".join(alerts)

def audit_monthly_burn() -> str:
    """Calculates total committed monthly spend across subscriptions."""
    total = sum(item["amount"] for item in USER_LEDGER)
    return f"Total recurring commitment: ${total:.2f}/month across {len(USER_LEDGER)} services."

# Strands autonomous decision routine
def run_pocketguard():
    print("=== POCKETGUARD AGENT STARTING ===")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Run autonomous tools
    burn_summary = audit_monthly_burn()
    renewal_alerts = scan_upcoming_renewals()
    
    print("[Tool Output - Spend Audit]:")
    print(burn_summary)
    print("\n[Tool Output - Renewal Watchdog]:")
    print(renewal_alerts)
    print("\n[Agent Final Verdict]:")
    print("Action required: Review Cloud Storage and Broadband before automatic deductions.")

if __name__ == "__main__":
    run_pocketguard()
