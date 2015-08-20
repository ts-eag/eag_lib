from django_cron import CronJobBase, Schedule


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 3 # every 1 mins

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'library.my_cron_job'

    def do(self):
        from django.utils import timezone
        print(timezone.now())

        with open('/Users/re4lfl0w/cron.txt', 'a') as f:
            f.write('1')
            f.write('\n')
        # pass # do your thing here