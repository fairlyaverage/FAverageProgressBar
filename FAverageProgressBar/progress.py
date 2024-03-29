import time, math
# def progress():
#     LINE_UP, LINE_CLEAR = '\033[1A', '\x1b[2K'
#     TAIL, HEAD, progress = '-', '>', ''
#     i = 0
#     while True:
#         progress=''
#         time.sleep(1)
#         i+=1
#         for k in range(i):
#             progress += TAIL
#         progress += HEAD
#         print(LINE_UP, end=LINE_CLEAR)
#         print(f"{progress}")

EMPTY = '░'
FULL = '█'

# ex: [██████████░░░░░░░░░░] 50.0%
#     container = []
# print(f"[{progress}{remainder}] {percent}")
# LINE_UP end with LINE_CLEAR

def get_runtime():
    if progress_info_intervals: return sum(progress_info_intervals)
    return False

def get_progress_info_intervals():
    if progress_info_intervals: return progress_info_intervals.copy()
    return False

class Progress:
    whole = None
    part = None
    progress_info_log = []
    progress_info_intervals = []

    # initialize values; negatives need to be updated
    def __init__():
        whole = -1
        part = -1

        pass

    def get_runtime():
        if progress_info_intervals: return sum(progress_info_intervals)
        return False

    def update(part, whole):
        current_time = time.time()
        average_interval = math.inf
        time_to_completion = math.inf
        estimated_time_to_completion = math.inf
        elapsed = 0
        progress_info_log.append(current_time)

        # if at least two log entries exist, delta is the difference between the most recent two
        if len(progress_info_log) > 1: progress_info_intervals.append(current_time - progress_info_log[-2])
        else: progress_info_intervals.append(0) # intervals will be 0 + difference

        elapsed = get_runtime()
        if len(progress_info_intervals) > 1: average_interval = sum(progress_info_intervals[1:]) / (len(progress_info_intervals) - 1) # ignore the first, must be a second element
        estimated_time_to_completion = (whole - part) * average_interval # whole doesn't need to be passed on update
        estimated_total_time = elapsed + estimated_time_to_completion
        return average_interval, elapsed, estimated_time_to_completion, estimated_total_time

def progress_info():
    global progress_info_log, progress_info_intervals
    progress_info_log = []
    progress_info_intervals = []

    # [ 123512059, 123521359, 1235213512 ]
    # want [1] - [0] = interval

# original
def update_progress_info(part, whole):
    current_time = time.time()
    average_interval = math.inf
    time_to_completion = math.inf
    estimated_time_to_completion = math.inf
    elapsed = 0

    progress_info_log.append(current_time)

    # add interval delta
    if len(progress_info_log) > 1: progress_info_intervals.append(current_time - progress_info_log[-2])
    else: progress_info_intervals.append(0)

    elapsed = get_runtime()
    average_interval = progress_info_intervals[-1] # elapsed / len(progress_info_intervals) # not actually avg, just last
    estimated_time_to_completion = (whole - part) * average_interval
    # progress_info_log.append(current_time - progress_info_log[-1])
    estimated_total_time = elapsed + estimated_time_to_completion
    # print(f"intervals = {progress_info_intervals}\n progress_log={progress_info_log}\n")
    return average_interval, elapsed, estimated_time_to_completion, estimated_total_time

def line_clear(n=1):
    LINE_UP, LINE_CLEAR = f'\033[1A', f'\x1b[2K'
    for i in range(n):
        print(LINE_CLEAR, end=LINE_UP)

def progress(part, whole, *loop_info):
    # print(f'TEST\nTEST\nTEST\n')
    # whole -= 1 # if exclusive range e.g. i in range(10) only goes from 0-9
    if part == 0: progress_info()
    MAX = 50 # + '[] 100.0%' 8-9 extra chars
    # special characters
    EMPTY = '░'
    FULL = '█'
    # LINE_UP, LINE_CLEAR = '\033[1A', '\x1b[2K'

    percent = round((part / whole) * 100, 1) # float .1
    average_interval, elapsed, estimated_time_to_completion, estimated_total_time = update_progress_info(part, whole)

    # progress indicator
    # ██████████ adjusted to 50 chars
    complete = FULL * math.floor(percent * .5) # *.5 because fixing for 50 characters x/50 = 50/100
    # ░░░░░░░░░░ adjusted to 50 chars
    remaining = EMPTY * math.ceil((100 - percent) * .5) # see above

    # optional loop info
    loop_label = ''
    if loop_info: # skip if empty
        # format before release
        # print(f'{loop_info[0]}: ', end='')
         if (len(loop_info) > 0): loop_label = f' [{loop_info[0]}]'

    output = f'[{complete}{remaining}] {percent}% | avg: {(average_interval*1000):.0f}ms elapsed: {(elapsed):.0f}s remaining: {(estimated_time_to_completion):.3f}s / {(estimated_time_to_completion / 60):.0f}m / {(estimated_time_to_completion / (60 * 60)):.0f}h total: {(estimated_total_time):.3f}s{loop_label}'
    if (part > 0): line_clear()
    # print(f'\n{output}', end='')
    print(f'{output}')

    if part == whole - 1: line_clear()

# delta = 60 # sec, for debug
# for i in range(delta):
#     time.sleep(0.725)
#     progress(i, delta)

