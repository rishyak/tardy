import typer
from .core import random_time

DEFAULT_TIME_FORMAT = "%A %B %m, %Y, %H:%M:%S"
DEFAULT_TIME_FORMAT_12_HOUR = "%A %B %m, %Y, %I:%M:%S"

tardy = typer.Typer()


@tardy.command()
def tell(
  hr24: bool = True,
  showtimezone: bool = False,
  time_format: str = DEFAULT_TIME_FORMAT,
):
  if not hr24 and time_format == DEFAULT_TIME_FORMAT:
    time_format = DEFAULT_TIME_FORMAT_12_HOUR

  print(
    random_time(
      hr24=hr24,
      showtimezone=showtimezone,
      time_format=time_format,
    )
  )


if __name__ == "__main__":
  tardy()
