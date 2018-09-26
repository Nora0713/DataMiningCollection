import schedule
import time


class Crawler:
    def job(self):
        print("I'm working...")


cr = Crawler()
schedule.every().second.do(cr.job)

while True:
    schedule.run_pending()
    time.sleep(1)
