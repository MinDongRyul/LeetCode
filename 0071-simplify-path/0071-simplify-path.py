class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.replace('//', '/')
        paths = path.split('/')
        stack = []
        for path_ in paths:
            if path_ == '..' and stack:
                stack.pop()
            elif path_ == '.' or path_ == '..':
                continue
            elif len(path_) > 0:
                stack.append(path_)
        
        r = ''
        
        if stack:
            for dir_ in stack:
                r += '/' + dir_
            return r
        else:
            return '/'