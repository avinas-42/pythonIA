class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.fd = None

    def __enter__(self):
        self.nb_lines = -1
        try:
            self.nb_lines = sum(1 for line in open(self.filename, 'r'))
        except :
            return None
        
        self.fd = open(self.filename, 'r')
        self.header_line = []
        if self.header:
            first_line = self.fd.readline().split(self.sep)
            for elem in first_line:
                self.header_line.append(elem.lstrip().rstrip())
        
        size = -1
        ret = []
        cpt = 0
        for line in self.fd:
            line = line[:-1]
            if cpt > self.skip_top and cpt < self.nb_lines - self.skip_bottom:
                ret_line = []
                list_elem = line.split(self.sep)
                if size != -1:
                    if size != len(list_elem) :
                        return None
                size = len(list_elem)
                
                for elem in list_elem:
                        ret_line.append(elem.lstrip().rstrip())
                        if elem == "":
                            return None
                ret.append(ret_line)
            cpt += 1
        self.data = ret

        return self

    def __exit__(self, type, value, traceback):
        self.fd.close()
    
    def getdata(self):
    # """ Retrieves the data/records from skip_top to skip bottom.
    # Returns:
    # nested list (list(list, list, ...)) representing the data.
    # """
        return self.data
        

    def getheader(self):
    # """ Retrieves the header from csv file.
    # Returns:
    # list: representing the data (when self.header is True).
    # None: (when self.header is False).
    # """
        if not self.header:
            return None
        return self.header_line