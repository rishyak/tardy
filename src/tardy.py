from datetime import datetime
from random import choice
from typing import Optional
import pytz
import typer

tardy = typer.Typer()


@tardy.command()
def tell(hr24: bool = True, showtimezone: bool = False):
  """Tells you the current time in a timezone of its choosing"""
  tz = pytz.timezone(choice(pytz.all_timezones))
  now = datetime.now(tz)

  time_format = f"%A %B %m, %Y, {'%H' if hr24 else '%I'}:%M:%S"
  if showtimezone:
    time_format += f" %Z"

  print(now.strftime(time_format))


if __name__ == "__main__":
  tardy()
