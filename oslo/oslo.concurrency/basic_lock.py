from oslo_concurrency import lockutils

@lockutils.synchronized('mylock')
def write_file_lock_in_a_process():
    with open('test.txt', 'w') as f:
        f.write("hello")

@lockutils.synchronized('mylock', lock_path="/tmp", external=True)
def write_file_lock_in_all_process():
    with open('test.txt', 'w') as f:
        f.write("hello")

        
        
if __name__ == '__main__':
    write_file_lock_in_a_process()
    write_file_lock_in_all_process()
