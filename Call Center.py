import datetime
uniqueid =1
def idplus():
    global uniqueid
    uniqueid = uniqueid +1

class Call(object):
    def __init__(self, name, number, reason):
        self.id = uniqueid
        self.name = name
        self.number = number
        self.reason = reason
        self.time = datetime.datetime.now()
        idplus()        
    def display(self):
        print self.id, self.name, self.number, self.reason, self.time

class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.queue = len(self.calls)
    def adds(self, callid):
        self.calls.append(callid)
    def remove(self, callid):
        self.calls.remove(callid)
    def info(self):
        for i in self.calls:
            print i.name, i.number, i.time
        print self.queue
    def findRemove(self, callnum):
        for i in self.calls:
            if i.number == callnum:
                self.remove(i)
    def sortCalls(self):
        sorted(self.calls, key=lambda Call: Call.id)

call1 = Call("Mike", "206-555-5555", "Upset")
call2 = Call("Jim", "425-555-1111", "Payment")
call3 = Call("Katy", "206-123-4567", "Cancel")

center1 = CallCenter([call1, call2, call3])

call4 = Call("Lucy", "360-598-8976", "Change Service")
center1.info()
center1.adds(call4)
center1.info()
center1.remove(call1)
center1.info()
center1.findRemove("425-555-1111")
center1.info()
center1.sortCalls()
center1.info()
center1.adds(call1)
center1.info()
center1.sortCalls()
center1.info()


    