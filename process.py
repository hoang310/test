
import psutil

'''
print(psutil.users())
psutil.process_iter
'''

i = 0
processes = []
for p in psutil.process_iter(['pid', 'name', 'username', 'memory_info', 'exe']): #'cpu_percent',
    try:
        #print(p)
        processes.append(p.info)
        '''i += 1
        if(i == 5):
            break'''
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

sorted_processes = sorted(processes, key=lambda p: p['memory_info'], reverse=True)

print("==== Da sap xep ====")

for p in sorted_processes:
    i += 1
    print(f"{i:<5} | {p['pid']:>6} | {p['name']:<28} | {str(p['username']):<25} | RAM: {p['memory_info'].rss / (1024*1024):6.1f} MB | {p['exe']} ") #| CPU: {p['cpu_percent']:>5}% 

