def frange(start, stop=None, step=None):
        #Use float number in range() function
        # if stop and step argument is null set start=0.0 and step = 1.0
        if stop == None:
            stop = start + 0.0
            start = 0.0
        if step == None:
            step = 1.0
        while True:
            if step > 0 and round(start,3) > stop:
                break
            elif step < 0 and start < stop:
                break
            yield round(start,3) # return float number
            start = start + step