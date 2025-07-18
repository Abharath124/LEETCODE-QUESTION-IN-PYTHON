class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        valid_times = []

        for hr in range(12):  
            for min in range(60): 
                if bin(hr).count('1') + bin(min).count('1') == turnedOn:
                    formatted_time = "{}:{:02d}".format(hr, min)
                    valid_times.append(formatted_time)

        return valid_times
