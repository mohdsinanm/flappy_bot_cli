from src.core.flappy_core import main, key
import threading


t1 = threading.Thread(target=main)
t2 = threading.Thread(target=key)
t2.start()
t1.start()
t2.join()
t1.join()