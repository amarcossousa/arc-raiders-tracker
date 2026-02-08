from freezegun import freeze_time
from datetime import datetime, timezone

from arc_raiders_tracker.services.event_service import get_active_events
from arc_raiders_tracker.domain.event import Event


@freeze_time("2026-02-08T12:30:00Z")
def test_event_is_active():
    event = Event(
        id="evt",
        name="Active Event",
        map_name="Dam",
        start_time=datetime(2026, 2, 8, 12, 0, tzinfo=timezone.utc),
        end_time=datetime(2026, 2, 8, 13, 0, tzinfo=timezone.utc),
    )

    active = get_active_events([event])

    assert len(active) == 1
