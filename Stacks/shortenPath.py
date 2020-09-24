def shortenPath(path):
    # Write your code here.
    pathList = path.split("/")
    shortestPath = []

    isAbsolutePath = True if path[0] == "/" else False
    
    for folder in pathList:
        if folder == "" or folder == ".":
            continue
        elif folder == "..":
            if isAbsolutePath and len(shortestPath)==0:
                continue
            elif not isAbsolutePath and len(shortestPath)==0 or shortestPath[-1]=="..":
                shortestPath.append(folder)
            else:
                shortestPath.pop()
        else:
            shortestPath.append(folder)
    
    return "/" + "/".join(shortestPath) if isAbsolutePath else "/".join(shortestPath)
    
print(shortenPath("/foo/../test/../test/../foo//bar/./baz"))
print(shortenPath("../../foo/bar/baz"))