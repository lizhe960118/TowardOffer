class Solution:
    def diffWaysToCompute(self, input_str: str) -> List[int]:
        result = []
        if input_str is None or len(input_str)==0:
            return []
        result = self.ComputeHelper(input_str)
        result.sort()
        return result
    
    def ComputeHelper(self, input_str):
        
        if input_str.isdigit():
            return [int(input_str)]
        
        res = list()
        
        for i in range(len(input_str)):
            if input_str[i] in "+-*":
                left_list = self.ComputeHelper(input_str[:i])
                right_list = self.ComputeHelper(input_str[i+1:])
                for left_num in left_list:
                    for right_num in right_list:
                        res.append(self.Calculate(left_num, input_str[i], right_num))
                        
        return res
                        
                        
    def Calculate(self, num_a, operator, num_b):
        if operator == "+":
            return num_a + num_b
        elif operator == "-":
            return num_a - num_b
        else:
            return num_a * num_b
        