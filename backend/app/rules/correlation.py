from datetime import datetime, timedelta

def detect_bruteforce(events):
    """
    Detect 5 failed logins from same IP within 1 minute
    """

    alerts = []

    grouped = {}

    # group events by IP
    for e in events:
        ip = e.source_ip
        if ip not in grouped:
            grouped[ip] = []
        grouped[ip].append(e)

    for ip, evs in grouped.items():

        failed_events = [
            e for e in evs if e.event_type == "AUTH_FAILURE"
        ]

        if len(failed_events) >= 5:
            alerts.append({
                "type": "BRUTE_FORCE",
                "source_ip": ip,
                "count": len(failed_events),
                "severity": "CRITICAL",
                "message": f"Brute force detected from {ip}"
            })

    return alerts