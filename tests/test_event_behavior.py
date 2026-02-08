from datetime import datetime, timezone, timedelta

from arc_raiders_tracker.domain.event import Event


def test_event_is_active_true():
    event = Event(
        id="evt",
        name="Active",
        map_name="Dam",
        start_time=datetime(2026, 2, 8, 12, 0, tzinfo=timezone.utc),
        end_time=datetime(2026, 2, 8, 13, 0, tzinfo=timezone.utc),
    )

    now = datetime(2026, 2, 8, 12, 30, tzinfo=timezone.utc)

    assert event.is_active(now) is True


def test_event_is_active_false():
    event = Event(
        id="evt",
        name="Inactive",
        map_name="Dam",
        start_time=datetime(2026, 2, 8, 12, 0, tzinfo=timezone.utc),
        end_time=datetime(2026, 2, 8, 13, 0, tzinfo=timezone.utc),
    )

    now = datetime(2026, 2, 8, 14, 0, tzinfo=timezone.utc)

    assert event.is_active(now) is False

def test_event_time_remaining():
    event = Event(
        id="evt",
        name="Active",
        map_name="Dam",
        start_time=datetime(2026, 2, 8, 12, 0, tzinfo=timezone.utc),
        end_time=datetime(2026, 2, 8, 13, 0, tzinfo=timezone.utc),
    )

    now = datetime(2026, 2, 8, 12, 30, tzinfo=timezone.utc)

    remaining = event.time_remaining(now)

    assert remaining.total_seconds() == 1800



def test_time_remaining_returns_zero_if_event_already_finished():
    event = Event(
        id="evt",
        name="Finished",
        map_name="Dam",
        start_time=datetime(2026, 2, 8, 12, 0, tzinfo=timezone.utc),
        end_time=datetime(2026, 2, 8, 13, 0, tzinfo=timezone.utc),
    )

    now = datetime(2026, 2, 8, 14, 0, tzinfo=timezone.utc)

    remaining = event.time_remaining(now)

    assert remaining == timedelta(0)


