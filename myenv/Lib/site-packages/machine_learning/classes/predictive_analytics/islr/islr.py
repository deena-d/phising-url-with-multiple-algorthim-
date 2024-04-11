# -*- coding: utf-8 -*-

from _thread import start_new_thread
# from islr import function_estimation as func_es_threads */

class islr:
    
    @classmethod
    def function_estimation():
        thread_started = False
        thread_started = start_new_thread(func_es_threads.thread_1,())
        start_new_thread(func_es_threads.thread_2,())
        while not thread_started:
            pass
    
    @classmethod    
    def hello_world(cls):
        a = "Hello world islr"
        print(a);
        
    @classmethod    
    def hello_world2(cls):
        a = "Hello world islr"
        print(a);
        
if __name__ == '__main__':
    islr.hello_world()
