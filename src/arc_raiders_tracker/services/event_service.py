from datetime import datetime, timezone



def get_active_events(events):
    now = datetime.now(timezone.utc)

    return [
        event
        for event in events
        if event.start_time <= now <= event.end_time
    ]

