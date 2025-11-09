from datetime import datetime
from random import choice
import pytz


def random_time(
  hr24: bool = True,
  showtimezone: bool = False,
  time_format: str | None = None,
):
  """Tells you the current time in a timezone of its choosing"""
  tz = pytz.timezone(choice(pytz.all_timezones))
  now = datetime.now(tz)

  if time_format is None:
    time_format = f"%A %B %m, %Y, {'%H' if hr24 else '%I'}:%M:%S"
  else:
    if hr24 and "%I" in time_format and "%H" not in time_format:
      time_format = time_format.replace("%I", "%H")
    elif not hr24 and "%H" in time_format and "%I" not in time_format:
      time_format = time_format.replace("%H", "%I")

  if showtimezone and "%Z" not in time_format:
    time_format += " %Z"

  return now.strftime(time_format)
