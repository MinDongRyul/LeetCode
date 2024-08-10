from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_dict = Counter(tasks)
        task_dict = sorted(task_dict.items(), key=lambda x : x[1], reverse=True)
        # max task num
        max_task_num = task_dict[0][1]
        # max idle num
        idle = (max_task_num - 1) * n
        
        for task in task_dict[1:]:
            idle -= min(task[1], max_task_num-1)
            if idle < 0:
                return len(tasks)
            
        return len(tasks) + idle