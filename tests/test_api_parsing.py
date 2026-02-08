import json
from pathlib import Path

from arc_raiders_tracker.infra.metaforge_client import parse_events


def test_parse_events_from_fixture():
    data = json.loads(
        Path("tests/fixtures/events_schedule.json").read_text()
    )

    events = parse_events(data)

    assert len(events) == 2
    assert events[0].name == "Stella Montis Defense"
    assert events[0].start_time.tzinfo is not None
