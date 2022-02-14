import threading
from .models import *
from faker import Faker
fake = Faker()

import time
import random

class CreateStudentThread(threading.Thread):
    
    def __init__(self , total):
        self.total = total
        threading.Thread.__init__(self)
    
    def run(self):
        try:
            channel_layer = get_channel_layer()
            current_total = 0

            for i in range(self.total):
                current_total += 1
                
                print(f'We are inside first thread {i}')
                time.sleep(1)
        except Exception as e:
            print(e)