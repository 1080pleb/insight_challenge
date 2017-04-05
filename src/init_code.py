#open file, here using sample log_samp.txt of total data log.txt
log_file = open("log_samp.txt", "r")

###vvv FEATURE 1 vvv###
### Write to file top 10 hostnames by count of requests, descending

#set up hostList for task1
hostList = []

for line in log_file:
  hostName = line.split()[0]  #grabs just the hostname/IP address
  
  for entry in hostList:
    if entry[0] == hostName:
      entry[1] = entry[1] + 1
      
    else:
      hostList.append([hostName,1])

#once log file has been run through, must reorder list by highest counts

#need to determine which works/is best
hostList_sorted = hostList.sort(key=itemgetter(1), reverse=True)
hostList_sorted = sorted(hostList, key=lambda host: host[1], reverse=True)
hostList_sorted = sorted(hostList, key=itemgetter(1), reverse=True)

#and then write top 10 to output file
f = open("hosts.txt", "w")
while i < 10:
    f.write(hostList.sorted[i])
    
f.close()
###^^^ FEATURE 1 ^^^###

###vvv FEATURE 2 vvv###
### Write to file top 10 resources requested by data volume, descending

#set up hostList for task1
resourceList = []

for line in log_file:
  resourceName = line.split()[6]  #grabs the resource name
  resourceBytes = line.split()[9] #grabs bytes for resource
  
  for entry in resourceList:
    if entry[0] == resourceName:
      entry[1] = entry[1] + resourceBytes
      
    else:
      resourceList.append([resourceName,resourceBytes])
      
#once log file has been run through, must reorder resource list by highest data volume

#need to determine which works/is best
resourceList_sorted = resourceList.sort(key=itemgetter(1), reverse=True)
resourceList_sorted = sorted(resourceList, key=lambda resource: resource[1], reverse=True)
resourceList_sorted = sorted(resourceList, key=itemgetter(1), reverse=True)

#and then write top 10 to output file
f = open("resources.txt", "w")
while i < 10:
    f.write(resourceList.sorted[i])
    
f.close()

###vvv FEATURE 3 vvv###
### Write to file top 10 most frequently visited 60 minute windows by visit count, decending



###^^^ FEATURE 3 ^^^###
