import sys, importlib.util

# load the current saved version of progress
# if wheel setup has been run and FAverageProgressBar has been installed through pip
sys.path.append('../FAverageProgressBar')
spec = importlib.util.spec_from_file_location('progress', '../FAverageProgressBar/progress.py')
progress = importlib.util.module_from_spec(spec)
spec.loader.exec_module(progress)

import time
# import FAverageProgressBar
# from FAverageProgressBar import progress
def loop_with_delay(delay, repeat, *loop_info):
    for i in range(repeat):
        progress.progress(i, repeat, loop_info[0])
        time.sleep(delay)
    # print(f'Complete')

    # output run stats

def nested_loop(delay, repeat, nested):
    if nested == 0: return
    for i in range(repeat):
        progress.progress(i, repeat)
        nested_loop(delay, repeat, nested - 1)
        time.sleep(delay)
    return

def static_nested(delay, repeat):
    # print('first loop outside')
    for i in range(10):
        # print('inside outer loop, before progress()')
        progress.progress(i, 10, f'outer loop {i} of 10')
        # print('inside outer loop, after progress()')
        for j in range(5):
            # print('inside inner loop, before progress()')
            progress.progress(j, 5, f'inner loop {j} of 5')
            # print('inside inner loop, after progress()')
            time.sleep(delay)

def main():
    # FAverageProgressBar.progress_info()
    # progress()
    repeat, delay = 10, .2
    # static
    print(f'Running {repeat} times with a {delay} second delay')

    # loop_with_delay(delay, repeat, 'regular')
    # nested_loop(delay, repeat, 2)

    # static loop
    static_nested(delay, repeat)

    # print('stuff')
    # progress.line_clear(2)
# if name == __main__:
main()
