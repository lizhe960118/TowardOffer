class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map_str = {}
        for i, v in enumerate(strs):
            key = "".join(sorted(v))
            if key not in map_str:
                map_str[key] = [v]
            else:
                map_str[key].append(v)
        result = []
        for value in map_str.values():
            result += [sorted(value)]
        return result


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
