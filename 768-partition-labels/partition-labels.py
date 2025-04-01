class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        list = [0] * 26
        
        for i,char in enumerate(s):
            list[ord(char) - ord('a')] = i
        
        partition_end = 0
        partition_start = 0
        partition_size = []

        for i,char in enumerate(s):
            partition_end = max(list[ord(char) - ord('a')],partition_end)
            
            if i == partition_end:
                partition_size.append(i-partition_start+1)
                partition_start = partition_end + 1
        return partition_size