'''
Created on Feb 19, 2018

@author: tongq
'''
class Solution(object):
    ___ removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res    # list
        isComment = False
        isLineComment = False
        line = ''
        ___ src __ source:
            j = 0
            isLineComment = False
            w.... j < l..(src):
                c = src[j]
                __ j < l..(src)-1 a.. src[j:j+2] __ '//' a.. n.. isComment:
                    __ line a.. n.. isComment:
                        res.a..(line)
                    isLineComment = True
                    line = ''
                ____ j < l..(src)-1 a.. src[j:j+2] __ '/*' a.. n.. isLineComment a.. n.. isComment:
                    j += 1
                    isComment = True
                ____ j < l..(src)-1 a.. src[j:j+2] __ '*/' a.. isComment:
                    j += 1
                    isComment = False
                ____ n.. isComment a.. n.. isLineComment:
                    line += c
                __ j __ l..(src)-1 a.. n.. isComment:
                    __ line:
                        res.a..(line)
                    line = ''
                j += 1
        r.. res
    
    ___ test(self):
        testCases = [
            [
                "/*Test program */",
                "int main()", "{ ",
                "  // variable declaration ",
                "int a, b, c;",
                "/* This is a test",
                "   multiline  ",
                "   comment for ",
                "   testing */",
                "a = b + c;", "}",
            ],
            [
                "a/*comment",
                "line",
                "more_comment*/b",
            ],
            [
                "class test{",
                "public: ",
                "   int x = 1;",
                "   /*double y = 1;*/",
                "   char c;", "};"
            ],
            [
                "main() {",
                "/* here is commments",
                "  // still comments */",
                "   double s = 33;",
                "   cout << s;", "}"
            ],
            [
                "void func(int k) {",
                "// this function does nothing /*",
                "   k = k*2/4;",
                "   k = k/2;*/",
                "}",
            ],
            [
                "a//*b/*/c",
                "blank",
                "d/*/e/*/f"
            ],
            [
                "a/*/b//*c",
                "blank",
                "d//*e/*/f"
            ],
        ]
        ___ source __ testCases:
            print('source: %s' % source)
            result = self.removeComments(source)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
