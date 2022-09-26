time = '06:52'

def get_sec(time_str):
    """Get Seconds from time."""
    h, m = time_str.split(':')
    return int(h) * 60 + int(m)

time_min = get_sec(time)

time_walk = 10
time_running = 6 * 3
time_walk2 = 4 * 10

time2 = time_walk + time_running + time_walk2
time_total = time2 + time_min

frase = "{:02d}:{:02d}".format(time_total//60, time_total%60)

print(frase)