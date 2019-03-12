class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if num is None or len(num) < 3:
            return False
        self.flag = False
        self.Helper(num, [])
        return self.flag

    def Helper(self, cur_str, path):
        if len(path) >= 3  and path[-1] != path[-2] + path[-3]:
            return

        if len(cur_str) == 0:
            if len(path) >= 3:
                self.flag = True
            return 
       
        for i in range(len(cur_str)):
            tmp_str = cur_str[:i+1]
            
            if tmp_str[0] == '0' and len(tmp_str) != 1:
                continue

            cur_num = int(tmp_str)
            self.Helper(cur_str[i+1:], path + [cur_num])
            
        return 