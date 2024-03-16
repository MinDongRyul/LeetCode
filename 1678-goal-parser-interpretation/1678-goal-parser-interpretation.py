class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        repl_dict = {'()':'o', 
                     '(al)':'al'}
        
        for key in repl_dict.keys():
            command = command.replace(key, repl_dict[key])

        return command