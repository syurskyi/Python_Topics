'''
Definition of BaseGFSClient
class BaseGFSClient:
    ___ readChunk(self, filename, chunkIndex
        # Read a chunk from GFS
    ___ writeChunk(self, filename, chunkIndex, content
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient
    """
    @param: chunkSize: An integer
    """
    ___ __init__(self, chunkSize
        BaseGFSClient.__init__(self)
        self.chunk_size = chunkSize
        self.chunk_num = {}

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    ___ read(self, filename
        __ filename not in self.chunk_num:
            r_
        i, content = 0, ''
        w___ i < self.chunk_num[filename]:
            content += self.readChunk(filename, i)
            i += 1
        r_ content

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    ___ write(self, filename, content
        i, j, n = 0, 0, le.(content)
        w___ j < n:
            self.writeChunk(filename, i, content[j : j + self.chunk_size])
            i += 1
            j += self.chunk_size
        self.chunk_num[filename] = i
