Date objects
------------

1.  ​20130305. Use `D.timedelta()` to calculate days between dates:

        import datetime as D
        def make_date_obj(date):
            return D.date(int(date[0:4]), int(date[5:7]), int(date[8:]))

        today = D.date.today()
        today - D.timedelta(days_back) # produces date object for a date ``days_back'' back

2.  ​20130305. Produce sequence of dates up to `days_back` days back:

        days_of_history = 7
        for days_back in range(0, days_of_history):
            the_date = today - D.timedelta(days_back)

3.  ​20130319. Time elapsed as H:MM:SS.ssssss:

        datetime.timedelta(seconds=time.time() - start_time)

[end]
