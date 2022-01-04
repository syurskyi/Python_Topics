'''
Created on Feb 19, 2018

@author: tongq
'''
c_ Solution(object):
    ___ removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res    # list
        isComment = F..
        isLineComment = F..
        line = ''
        ___ src __ source:
            j = 0
            isLineComment = F..
            w.... j < l..(src):
                c = src[j]
                __ j < l..(src)-1 a.. src[j:j+2] __ '//' a.. n.. isComment:
                    __ line a.. n.. isComment:
                        res.a..(line)
                    isLineComment = T..
                    line = ''
                ____ j < l..(src)-1 a.. src[j:j+2] __ '/*' a.. n.. isLineComment a.. n.. isComment:
                    j += 1
                    isComment = T..
                ____ j < l..(src)-1 a.. src[j:j+2] __ '*/' a.. isComment:
                    j += 1
                    isComment = F..
                ____ n.. isComment a.. n.. isLineComment:
                    line += c
                __ j __ l..(src)-1 a.. n.. isComment:
                    __ line:
                        res.a..(line)
                    line = ''
                j += 1
        r.. res
    
    ___ test
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
            result = removeComments(source)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
