def matchingStrings(stringList, queries):
	return [stringList.count(query) for query in queries]

stringList = [
    'kvzakhpdscowt', 'xng', 'xng', 'xng', 'ojwrqfxblftpgarijtny', 
    'kvzakhpdscowt', 'gggyps', 'xng', 'nvsutye', 'cygfagnqvdfltj', 
    'gggyps', 'ojwrqfxblftpgarijtny', 'kvzakhpdscowt', 
    'obxetdfzeznkrbfutns', 'hqpl', 'obxetdfzeznkrbfutns', 
    'uystwsiawmlpi', 'ojwrqfxblftpgarijtny', 'nvsutye', 'boeaaglfoyfl'
]

queries = [
    'uvxgygia', 'xng', 'cygfagnqvdfltj', 'ladzztwkuj', 'obxetdfzeznkrbfutns', 
    'hefmaiyadt', 'hlrdhmqm', 'ojwrqfxblftpgarijtny', 'ojwrqfxblftpgarijtny', 
    'nfxcsa'
]

print(matchingStrings(stringList, queries))
#answer [0, 4, 1, 0, 2, 0, 0, 3, 3, 0]
