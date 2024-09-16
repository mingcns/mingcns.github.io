from datetime import date, timedelta

SPRING_LENGTH = timedelta(weeks = 16, days = 1)
SPRING_HALF_LENGTH = timedelta(weeks = 6, days = 6)
FALL_LENGTH = timedelta(weeks = 15, days = 2)


def umnBreakTime(year):
	d = date(year, 9, 1)
	while d.isoweekday() != 1:
		d += timedelta(days = 1)
	laborDay = d
	fallStart = d + timedelta(days = 1)
	fallEnd = fallStart + FALL_LENGTH

	# Jan 15 is the earliest possible MLK
	d = date(year + 1, 1, 15)
	while d.isoweekday() != 1:
		d += timedelta(days = 1)
	mlkDay = d
	springStart = mlkDay + timedelta(days = 1)
	springBreakMonday = springStart + SPRING_HALF_LENGTH
	springEnd = springStart + SPRING_LENGTH

	d = date(year + 1, 9, 1)
	while d.isoweekday() != 1:
		d += timedelta(days = 1)
	nextLaborDay = d
	nextFallStart = nextLaborDay + timedelta(days = 1)

	return [
		f'Fall {year} first day: {fallStart.isoformat()}',
		f'Fall {year} last day:  {fallEnd.isoformat()}',
		f'{year} Winter break days: {(mlkDay - fallEnd).days}',
		f'Spring {year + 1} first day: {springStart.isoformat()}',
		f'{year + 1} Spring break Monday: {springBreakMonday.isoformat()}',
		f'Spring {year + 1} last day: {springEnd.isoformat()}',
		f'{year + 1} Summer break days: {(nextLaborDay - springEnd).days}'
	]

for y in range(2024, 2028):
	for i in umnBreakTime(y):
		print(i)
	print()