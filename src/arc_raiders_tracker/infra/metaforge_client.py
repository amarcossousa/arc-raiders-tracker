from datetime import datetime, timezone
from typing import List

from arc_raiders_tracker.domain.event import Event


def _parse_datetime(value: str) -> datetime:
    # API retorna formato ISO com Z
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return dt.astimezone(timezone.utc)


def parse_events(data: list) -> List[Event]:
    events = []

    for item in data:
        try:
            event = Event(
                id=item["id"],
                name=item["name"],
                map_name=item.get("map"),
                start_time=_parse_datetime(item["startTime"]),
                end_time=_parse_datetime(item["endTime"]),
            )
            events.append(event)

        except Exception:
            # Resiliência: ignora evento quebrado
            continue

    return events
