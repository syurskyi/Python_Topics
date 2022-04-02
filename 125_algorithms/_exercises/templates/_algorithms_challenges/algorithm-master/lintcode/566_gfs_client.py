'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


c_ GFSClient(BaseGFSClient
    """
    @param: chunkSize: An integer
    """
    ___ - , chunkSize
        BaseGFSClient.- )
        chunk_size = chunkSize
        chunk_num    # dict

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    ___ read  filename
        __ filename n.. __ chunk_num:
            r..
        i, content = 0, ''
        w.... i < chunk_num[filename]:
            content += readChunk(filename, i)
            i += 1
        r.. content

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    ___ write  filename, content
        i, j, n = 0, 0, l..(content)
        w.... j < n:
            writeChunk(filename, i, content[j : j + chunk_size])
            i += 1
            j += chunk_size
        chunk_num[filename] = i
