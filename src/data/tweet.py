import datetime
from dataclasses import dataclass


@dataclass
class Tweet:
    id: int
    date: datetime.date
    time: datetime.time
    wr: int
    cm: int
    spin: int