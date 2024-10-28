# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

"""
Approach
Persist the chars that didn't got appended in 
the buffer but are still in the cache. 
Keep reloading cache when a new buffer needs to be read

Complexity
Time complexity:
Sum of all lengths in queries (assume n) + 
cache size : O(n) to copy n chars

Space complexity:
Persisting 4 chars, but that is constant. 
Buf size is also constant : O(1)
"""

class Solution:
    def __init__(self):
        self.oldReads = deque()
        self.bufPointer = 0

    def read(self, buf, n):
        buf4 = [""] * 4 

        i = 0
        lettersAdded = 0
        while n > 0: # read 1 character until n == 0
            if self.oldReads: # old reads is nonempty
                buf[lettersAdded] = self.oldReads.popleft()
                n -= 1
                lettersAdded += 1
            elif i < 4 and buf4[i] != "": # our Class' buf is nonempty
                buf[lettersAdded] = buf4[i]
                i += 1
                n -= 1
                lettersAdded += 1
            else: # need to read 4 more characters from the read4 API. Don't read yet just call the API 
                buf4 = [""] * 4 
                read4(buf4)
                i = 0
                if buf4[0] == "": # no more characters left to read
                    break

        if i < 4 and buf4[i] != "":
            while i < 4 and buf4[i] != "":
                self.oldReads.append(buf4[i])
                i += 1
        
        return lettersAdded