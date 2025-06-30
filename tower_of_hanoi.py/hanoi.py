def hanoi(disk, source, middle, destination):
    
    if disk == 0:
        print(f"Disk {disk} from {source} to {destination}")
        return
        
    hanoi(disk-1, source, destination, middle)
    print(f"Disk {disk} from {source} to {destination}")
    hanoi(disk-1, middle, source, destination)
    
    
    

print(hanoi(3,'A', 'B', 'C'))