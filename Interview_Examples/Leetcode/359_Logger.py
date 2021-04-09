class Logger(object):

    def __init__(self):

        self.dictionary_of_messages = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """



        answers = []

        if message not in self.dictionary_of_messages:
            self.dictionary_of_messages[message] = timestamp
            answers.append(True)
        elif message == None:
            answers.append(None)
        elif message in self.dictionary_of_messages:
            #  1 - 11 = 10 =>
            if abs(timestamp - self.dictionary_of_messages[message]) >= 10:
                answers.append(True)
                self.dictionary_of_messages[message] = timestamp
            else:
                answers.append(False)

        print(self.dictionary_of_messages)
        return answers

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

if __name__ == "__main__":

    logger = Logger()
    result = logger.shouldPrintMessage(1, "foo")
    print(result)
    result = logger.shouldPrintMessage(2, "bar")
    print(result)
    result = logger.shouldPrintMessage(3, "foo")
    print(result)
    result = logger.shouldPrintMessage(8, "bar")
    print(result)
    result = logger.shouldPrintMessage(20, "bar")
    print(result)