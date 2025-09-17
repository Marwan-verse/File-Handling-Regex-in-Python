ips = ['192.168.0.1', '192.168.0.1', '10.0.0.5'] #short list of IPs with duplicates
unique_ips = set(ips)   # {'192.168.0.1', '10.0.0.5'}

ips = ['192.168.0.1', '192.168.0.1', '10.0.0.5','192.178.0.1', '192.168.0.1', '10.1.0.5','192.168.0.1', '192.168.0.1', '100.0.0.5','192.178.1.1', '192.168.0.1', '10.1.0.5']
 #random IPs with duplicates
unique_ips = set(ips)  # {'100.0.0.5', '10.0.0.5', '10.1.0.5', '192.168.0.1', '192.178.0.1', '192.178.1.1'}
print(unique_ips) #print unique IPs

 #a set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
 #Python’s set class represents the mathematical notion of a set. The major advantage of using a set,
 #as opposed to a list, is that it has a highly optimized method for checking whether a

#python3 _file_handling_folder/unique_search.py