'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    ___ __init__(self, chunkSize):
        BaseGFSClient.__init__(self)
        self.chunk_size = chunkSize
        self.chunk_num = {}

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    ___ read(self, filename):
        __ filename n.. __ self.chunk_num:
            r..
        i, content = 0, ''
        w.... i < self.chunk_num[filename]:
            content += self.readChunk(filename, i)
            i += 1
        r.. content

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    ___ write(self, filename, content):
        i, j, n = 0, 0, l..(content)
        w.... j < n:
            self.writeChunk(filename, i, content[j : j + self.chunk_size])
            i += 1
            j += self.chunk_size
        self.chunk_num[filename] = i
