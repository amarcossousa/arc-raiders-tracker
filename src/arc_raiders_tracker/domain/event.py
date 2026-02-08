from dataclasses import dataclass
from datetime import datetime, timezone, timedelta


@dataclass
class Event:
    id: str
    name: str
    map_name: str
    start_time: datetime
    end_time: datetime

    def __post_init__(self):
        # Garantir timezone UTC
        if self.start_time.tzinfo != timezone.utc:
            raise ValueError("start_time must be UTC")

        if self.end_time.tzinfo != timezone.utc:
            raise ValueError("end_time must be UTC")

        # Garantir integridade temporal
        if self.start_time >= self.end_time:
            raise ValueError("start_time must be before end_time")
    
    def is_active(self, now: datetime) -> bool:
        return self.start_time <= now <= self.end_time
    

    def time_remaining(self, now: datetime):
        return self.end_time - now
    
    def time_remaining(self, now: datetime) -> timedelta:
        remaining = self.end_time - now
        if remaining.total_seconds() < 0:
            return timedelta(0)
        return remaining



