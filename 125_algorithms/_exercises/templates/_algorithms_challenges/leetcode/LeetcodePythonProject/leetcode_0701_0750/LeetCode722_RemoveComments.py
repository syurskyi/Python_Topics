'''
Created on Feb 19, 2018

@author: tongq
'''
class Solution(object
    ___ removeComments(self, source
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        isComment = False
        isLineComment = False
        line = ''
        ___ src in source:
            j = 0
            isLineComment = False
            w___ j < le.(src
                c = src[j]
                __ j < le.(src)-1 and src[j:j+2] __ '//' and not isComment:
                    __ line and not isComment:
                        res.append(line)
                    isLineComment = True
                    line = ''
                ____ j < le.(src)-1 and src[j:j+2] __ '/*' and not isLineComment and not isComment:
                    j += 1
                    isComment = True
                ____ j < le.(src)-1 and src[j:j+2] __ '*/' and isComment:
                    j += 1
                    isComment = False
                ____ not isComment and not isLineComment:
                    line += c
                __ j __ le.(src)-1 and not isComment:
                    __ line:
                        res.append(line)
                    line = ''
                j += 1
        r_ res
    
    ___ test(self
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
        ___ source in testCases:
            print('source: %s' % source)
            result = self.removeComments(source)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
